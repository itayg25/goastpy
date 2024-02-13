package main

import (
	"C"
	"encoding/json"
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"io/ioutil"
	"os"
	"reflect"
	"strings"
)

func main() {
	sourceCode, err := ioutil.ReadFile(os.Args[1])
	if err == nil {
		result := parseSourceCode(string(sourceCode))
		fmt.Printf("%s\n", result)
	} else {
		fmt.Printf("%s\n", err)
	}

}

// parseSourceCode takes a string containing Go code and returns a JSON representation
// of the abstract syntax tree (AST) in byte format.
func parseSourceCode(code string) []byte {
	fileSet := token.NewFileSet()
	file, _ := parser.ParseFile(fileSet, "main.go", code, parser.ParseComments)
	astMap := traverseAST(fileSet, file)
	result, _ := json.Marshal(astMap)
	return result
}

// traverseAST recursively walks through the AST nodes and creates a map representation
// of the nodes' properties, including their position in the source code.
func traverseAST(fileSet *token.FileSet, node interface{}) map[string]interface{} {
	if node == nil {
		return nil
	}

	astMap := make(map[string]interface{})

	if _, ok := node.(*ast.Scope); ok {
		return nil
	}

	if _, ok := node.(*ast.Object); ok {
		return nil
	}

	val := reflect.ValueOf(node)
	if val.IsNil() {
		return nil
	}
	if val.Kind() == reflect.Ptr {
		val = val.Elem()
	}
	nodeType := val.Type()
	astMap["_type"] = nodeType.Name()

	for i := 0; i < nodeType.NumField(); i++ {
		field := nodeType.Field(i)
		val := val.Field(i)
		if strings.HasSuffix(field.Name, "Pos") {
			continue
		}
		switch field.Type.Kind() {
		case reflect.Array, reflect.Slice:
			list := make([]interface{}, 0, val.Len())
			for i := 0; i < val.Len(); i++ {
				if item := traverseAST(fileSet, val.Index(i).Interface()); item != nil {
					list = append(list, item)
				}
			}
			astMap[field.Name] = list
		case reflect.Ptr, reflect.Interface:
			if child := traverseAST(fileSet, val.Interface()); child != nil {
				astMap[field.Name] = child
			}
		case reflect.String:
			astMap[field.Name] = val.String()
		case reflect.Int:
			if field.Type.Name() == "Token" {
				astMap[field.Name] = token.Token(val.Int()).String()
			} else {
				astMap[field.Name] = val.Int()
			}
		case reflect.Bool:
			astMap[field.Name] = val.Bool()
		default:
			fmt.Fprintln(os.Stderr, field)
		}
	}
	if n, ok := node.(ast.Node); ok {
		start := fileSet.Position(n.Pos())
		end := fileSet.Position(n.End())
		astMap["Loc"] = map[string]interface{}{"Start": start, "End": end}
	}
	return astMap
}
