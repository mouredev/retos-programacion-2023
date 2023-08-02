numerosAbaco={
"O---OOOOOOOO":"1",
"OO---OOOOOOO":"2",
"OOO---OOOOOO":"3",
"OOOO---OOOOO":"4",
"OOOOO---OOOO":"5",
"OOOOOO---OOO":"6",
"OOOOOOO---OO":"7",
"OOOOOOOO---O":"8",
"OOOOOOOOO---":"9",
"---OOOOOOOOO":"0"
}

def Abaco(a):
	numero=0
	for i in a:	

		for j in numerosAbaco:
			if j==i:
				numero=(numero*10)+int(numerosAbaco[j])
				break

	return numero




a=[
"O---OOOOOOOO",
"OOO---OOOOOO",
"---OOOOOOOOO",
"OO---OOOOOOO",
"OOOOOOO---OO",
"OOOOOOOOO---",
"---OOOOOOOOO"
]

print (Abaco(a))
