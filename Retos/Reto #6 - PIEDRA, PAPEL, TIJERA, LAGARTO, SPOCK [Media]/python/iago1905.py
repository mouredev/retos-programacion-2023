resultado = ["player1", "player2", "empate"]
opciones = ["🗿", "📄", "✂", "🦎", "🖖"]
jugadas = [("🗿","✂"), ("🗿","🦎"), ("📄","🗿"), ("📄","🖖"), ("✂","📄"), ("✂","🦎"), ("🦎","📄"), ("🦎","🖖"), ("🖖","🗿"), ("🖖","✂")]
contador = [0,0]
for i in jugadas:
    if i[0] == "🗿":
        if i[1] == "✂" or i[1] == "🦎":
           contador[0] += 1
        elif i[1] == "📄" or i[1] == "🖖":
            contador[1] += 1 
    if i[0] == "📄":
        if i[1] == "🗿" or i[1] == "🖖":
           contador[0] += 1
        elif i[1] == "✂" or i[1] == "🦎":
            contador[1] += 1
    if i[0] == "✂":
        if i[1] == "📄" or i[1] == "🦎":
           contador[0] += 1
        elif i[1] == "🗿" or i[1] == "🖖":
            contador[1] += 1
    if i[0] == "🦎":
        if i[1] == "📄" or i[1] == "🖖":
           contador[0] += 1
        elif i[1] == "🗿" or i[1] == "✂":
            contador[1] += 1
    if i[0] == "🖖":
        if i[1] == "🗿" or i[1] == "✂":
           contador[0] += 1
        elif i[1] == "📄" or i[1] == "🦎":
            contador[1] += 1
            
if contador[0] > contador[1]:
    print(resultado[0])
elif contador[0] < contador[1]:
    print(resultado[1])
else:
    print(resultado[2])