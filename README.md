# GoAstPy - Python Wrapper for Go AST Parser

`GoAstPy` is a Python wrapper for the built-in Go Abstract Syntax Tree (AST) parser. It allows you to parse and manipulate Go source code from within your Python applications. This package is perfect for developers working with Go code analysis, code generation, or automated refactoring tools in Python.

## 🚀 Installation

```bash
pip install goastpy
```

## 📚 Usage

```python
import goastpy

if __name__ == '__main__':
    code = '''
    package main

    import "fmt"

    func main() {
        fmt.Println("Hello, World!")
    }
    '''
    parsed_code = goastpy.GoAst(code)
    print(parsed_code.ast)
```

With GoAstPy, you can quickly and easily parse Go source code, extract information about its structure, and work with it in your Python projects.

## 🛠️ Building the Go Shared Library

```bash
cd ./goastpy
go build -o goastparser.so -buildmode=c-shared main.go goastparser_export.go

```
This command generates a shared library file (goastparser.so) that is used by the Python wrapper to interface with the Go AST parser.

## 🔖 GitHub Tags

- `golang`
- `python`
- `ast`
- `go-ast-parser`
- `code-analysis`
- `code-generation`
- `refactoring`

## 📖 License

This project is licensed under the MIT License.

## 🌟 Contributing

We welcome contributions from the community! If you find a bug or have a feature request, please [open an issue](https://github.com/itayg25/GoAstPy/issues) or submit a [pull request](https://github.com/itayg25/GoAstPy/pulls). Let's make `GoAstPy` even better together!

