# gopyast

python wrapper for the built-in go ast parser 


## installation

```bash
pip install goastpy
```

## usage:

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

## building the c-shared golang files:

```bash

cd ./goastpy

go build -o goastparser.so -buildmode=c-shared main.go goastparser_export.go

```
