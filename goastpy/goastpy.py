import json

from goastpy import goastparser_wrapper


class GoAst:
    def __init__(self, go_code):
        self.__ast_json = self.parse_source_code_to_json(go_code)
        self.ast = json.loads(self.__ast_json)

    @staticmethod
    def parse_source_code_to_json(code):
        """Wrap the Go function parseSourceCode and return the result as a string."""
        #

        result = goastparser_wrapper.GoAstLib.lib().ParseSourceCode(code.encode('utf-8'))
        return result.decode('utf-8')


def main():
    code = '''
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
'''
    parsed_code = GoAst(code)
    print(parsed_code.ast)


if __name__ == '__main__':
    main()
