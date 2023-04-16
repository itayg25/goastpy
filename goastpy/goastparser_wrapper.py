import os
import sys
import ctypes
import subprocess
from ctypes import c_char_p
import json

GO_LIBRARY = "goastparser.so"


def find_go_executable():
    go_executable = "go" + (".exe" if sys.platform == "win32" else "")
    for path in os.environ["PATH"].split(os.pathsep):
        executable_path = os.path.join(path.strip('"'), go_executable)
        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
            return executable_path
    raise FileNotFoundError("Go executable not found in the system's PATH")


def build_go_library_if_not_exists():
    if not os.path.exists(GO_LIBRARY):
        print("Building Go shared library...")
        try:
            go_executable = find_go_executable()
        except FileNotFoundError as e:
            print(f"Error finding Go in path: {e}, trying to use default homebrew path")
            go_executable = '/opt/homebrew/bin/go'
        try:
            subprocess.check_call([go_executable, "build", "-o", GO_LIBRARY, "-buildmode=c-shared", "main.go",
                                   "goastparser_export.go"])
        except subprocess.CalledProcessError as e:
            print(f"Error building Go shared library: {e}")
            raise


def load_go_library():
    return ctypes.CDLL('./' + GO_LIBRARY)


def configure_go_function(go_lib):
    go_lib.ParseSourceCode.restype = c_char_p
    go_lib.ParseSourceCode.argtypes = [c_char_p]


class GoAst:
    def __init__(self, go_code):
        self.__ast_json = self.parse_source_code_to_json(go_code)
        self.ast = json.loads(self.__ast_json)

    @staticmethod
    def parse_source_code_to_json(code):
        """Wrap the Go function parseSourceCode and return the result as a string."""
        build_go_library_if_not_exists()

        goastparser_lib = load_go_library()
        configure_go_function(goastparser_lib)

        result = goastparser_lib.ParseSourceCode(code.encode('utf-8'))
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
