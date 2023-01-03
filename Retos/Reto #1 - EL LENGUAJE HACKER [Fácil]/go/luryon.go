package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(hackerLang("Hello World"))
}

func hackerLang(text string) string {
	//This solution uses the ASCII Table values of every character.
	resp := bytes.Buffer{}
	for _, char := range text {
		// In case character are in range of UpperCase Letters
		// are replaced by the LowerCase letter.
		// 65 = A and Z = 90 in ASCII Table
		if 65 <= char && char <= 90 {
			char = char + 32
		}
		switch char {
		case 97:
			resp.WriteString("4")
		case 98:
			resp.WriteString("I3")
		case 99:
			resp.WriteString("[")
		case 100:
			resp.WriteString(")")
		case 101:
			resp.WriteString("3")
		case 102:
			resp.WriteString("|=")
		case 103:
			resp.WriteString("&")
		case 104:
			resp.WriteString("#")
		case 105:
			resp.WriteString("1")
		case 106:
			resp.WriteString(",_|")
		case 107:
			resp.WriteString(">|")
		case 108:
			resp.WriteString("1")
		case 109:
			resp.WriteString("/\\/\\")
		case 110:
			resp.WriteString("^/")
		case 111:
			resp.WriteString("0")
		case 112:
			resp.WriteString("|*")
		case 113:
			resp.WriteString("(_,)")
		case 114:
			resp.WriteString("I2")
		case 115:
			resp.WriteString("5")
		case 116:
			resp.WriteString("7")
		case 117:
			resp.WriteString("(_)")
		case 118:
			resp.WriteString("\\/")
		case 119:
			resp.WriteString("\\/\\/")
		case 120:
			resp.WriteString("><")
		case 121:
			resp.WriteString("j")
		case 122:
			resp.WriteString("2")
		}
	}

	return resp.String()
}
