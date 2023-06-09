import re

def espanol_to_aurebesh(texto, espanol= False):
    
    dicc_aurebesh = {"A":"Aurek", "B":"Besh", "C":"Cresh", "D":"Dorn", 
                    "E":"Esk", "F":"Forn", "G":"Grek", "H":"Herf", "I":"Isk",
                    "J":"Jenth", "K":"Krill", "L":"Leth", "M":"Mern", "N":"Nern",
                    "O":"Osk", "P":"Peth", "Q":"Qek", "R":"Resh", "S":"Senth",
                    "T":"Trill", "U":"Usk", "V":"Vev", "W":"Wesk", "X":"Xesh",
                    "Y":"Yirt", "Z":"Zerek", "": ""}
    
    aurebesh = ""
    if espanol == False:
        for palabra in texto:
            if palabra.upper() in dicc_aurebesh.keys():
                aurebesh += dicc_aurebesh[palabra.upper()]
            else:
                aurebesh += palabra
            
        return aurebesh
    else:
        patron = r'[:space:]*[A-Z]*[a-z]*'
        palabras = re.findall(patron,texto)
        
        for palabra in palabras:
            
            if palabra in dicc_aurebesh.values():
                aurebesh += list(dicc_aurebesh.keys())[list(dicc_aurebesh.values()).index(palabra)]
                if list(dicc_aurebesh.keys())[list(dicc_aurebesh.values()).index(palabra)] == "":
                    aurebesh += " "
            else: 
                aurebesh += palabra
        return aurebesh.capitalize()
    
print(espanol_to_aurebesh("Que la fuerza te acompane")) 
print(espanol_to_aurebesh("QekUskEsk LethAurek FornUskEskReshZerekAurek TrillEsk AurekCreshOskMernPethAurekNernEsk", espanol=True))   
print(espanol_to_aurebesh("HerfOskLethAurek BeshReshAurekIskSenth", espanol=True))

