Option Explicit

Function RgbToHex(r, g, b)
    RgbToHex = "#" & Right("0" & Hex(r), 2) & Right("0" & Hex(g), 2) & Right("0" & Hex(b), 2)
End Function

Function HexToRgb(hexValue)
    If Left(hexValue, 1) = "#" Then
        hexValue = Right(hexValue, Len(hexValue) - 1)
    End If
    Dim r, g, b
    r = CInt("&H" & Left(hexValue, 2))
    g = CInt("&H" & Mid(hexValue, 3, 2))
    b = CInt("&H" & Right(hexValue, 2))
    HexToRgb = "r: " & r & ", g: " & g & ", b: " & b
End Function

WScript.Echo "Ejemplos de uso:"

WScript.Echo "RGB to HEX (midnight blue):"
WScript.Echo RgbToHex(25, 25, 112)

WScript.Echo "HEX to RGB (royal blue):"
WScript.Echo HexToRgb("#4169E1")
