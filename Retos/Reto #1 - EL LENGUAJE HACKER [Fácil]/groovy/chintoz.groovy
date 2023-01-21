def map = ['A': '4', 'B': 'I3', 'C': '[', 'D': ')', 'E': '3', 'F': '|=', 'G': '&', 'H': '#',
           'I': '1', 'J': ',_|', 'K': '>|', 'L': '1', 'M': '/\\/\\', 'N': '^/', 'O': '0', 'P': '|*', 'Q': '(_,)',
           'R': 'I2', 'S': '5', 'T': '7', 'U': '(_)', 'V': '\\/', 'W': '\\/\\/', 'X': '><', 'Y': 'j', 'Z': '2']
def encode = { it.chars.collect { it as String }.collect { map.getOrDefault(it.toUpperCase(), it) }.join() }

print 'Introduce la cadena a convertir: '
def input = System.in.newReader().readLine() as String
println "Cadena convertida: " + encode(input)