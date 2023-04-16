package main

import "C"

//export ParseSourceCode
func ParseSourceCode(code *C.char) *C.char {
	goCode := C.GoString(code)
	result := parseSourceCode(goCode)
	return C.CString(string(result))
}
