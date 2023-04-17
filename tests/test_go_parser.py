from goastpy import goastpy


class TestParser:

    def test_001_hello_world_code(self):
        code = '''
        package main

        import "fmt"

        func main() {
            fmt.Println("Hello, World!")
        }
        '''
        ast = goastpy.GoAst(code)
        assert ast is not None
