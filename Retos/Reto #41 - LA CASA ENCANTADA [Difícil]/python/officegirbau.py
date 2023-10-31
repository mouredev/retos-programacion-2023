import random
import time
import sys

def imprimir_como_maquina(texto):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(0.01)  # Ajusta el valor de retraso según tus preferencias
    print()  # Salto de línea al final para que el próximo mensaje aparezca en una nueva línea


#colorins
verd= "\033[32m"
blau= "\033[34m"
groc = "\033[33m"
vermell = "\033[31m"
blanc = "\033[0m"

# Función para crear una matriz de 4x4 con habitaciones aleatorias
def crear_mansio():
    matriz_mansio = [["⬜️" for _ in range(4)] for _ in range(4)]
    
    # Colocar la puerta en (0, 0)
    matriz_mansio[0][0] = "🚪"
    
    # Obtener una ubicación aleatoria para el caramelo
    fila_caramelo, columna_caramelo = (random.randint(0, 3), random.randint(0, 3))
    
    # Asegurar que el caramelo no esté en (0, 0)
    while (fila_caramelo, columna_caramelo) == (0, 0):
        fila_caramelo, columna_caramelo = (random.randint(0, 3), random.randint(0, 3))
    
    matriz_mansio[fila_caramelo][columna_caramelo] = "🍭"
    
    # Definir ubicaciones de los dos fantasmas
    fila_fantasma1, columna_fantasma1 = (random.randint(0, 3), random.randint(0, 3))
    fila_fantasma2, columna_fantasma2 = (random.randint(0, 3), random.randint(0, 3))
    
    # Asegurar que los fantasmas no estén en (0, 0) ni en la ubicación del caramelo
    while (fila_fantasma1, columna_fantasma1) == (0, 0) or (fila_fantasma1, columna_fantasma1) == (fila_caramelo, columna_caramelo):
        fila_fantasma1, columna_fantasma1 = (random.randint(0, 3), random.randint(0, 3))
    
    while (fila_fantasma2, columna_fantasma2) == (0, 0) or (fila_fantasma2, columna_fantasma2) == (fila_caramelo, columna_caramelo) or (fila_fantasma2, columna_fantasma2) == (fila_fantasma1, columna_fantasma1):
        fila_fantasma2, columna_fantasma2 = (random.randint(0, 3), random.randint(0, 3))
    
    matriz_mansio[fila_fantasma1][columna_fantasma1] = "👻"
    matriz_mansio[fila_fantasma2][columna_fantasma2] = "👻"
    
    return matriz_mansio



def desencriptar_diccionari(enigmatic):
    diccionari_desencriptat = {}
    for paraula_encriptada, pregunta_encriptada in enigmatic.items():
        paraula = ''.join([chr(ord(caracter) - 1) for caracter in paraula_encriptada])
        pregunta = ''.join([chr(ord(caracter) - 1) for caracter in pregunta_encriptada])
        diccionari_desencriptat[paraula] = pregunta
    return diccionari_desencriptat

def mostrar_matriu(matriu):
    for fila in matriu:
        print(fila)
    print() 

def avaluar_casella(posicio_jugador, diccionari, fantasmes):
    # trasnportem la variable comptador
    global comptador
    # Després que el jugador encerti una pregunta i avanci a una nova casella:
    fila, columna = posicio_jugador
    casella = habitacions[fila][columna]
    recorregut_jugador[fila][columna] = habitacions[fila][columna]

    if casella == "🍭":
        imprimir_como_maquina(f"{verd}🍭¡Has encontrado el caramelo!🍭 Ganaste el juego!!.🍭\n{blanc}")
        mostrar_matriu(recorregut_jugador)
        imprimir_como_maquina(f'{vermell}⬜️MANSION⬜️DESCUBIERTA⬜️{blanc}')
        mostrar_matriu(habitacions)
        

        # Calcula el temps transcorregut
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Imprimeix el temps transcorregut
        imprimir_como_maquina(f"{verd}🍭Tiempo empleado: {int(elapsed_time)} segundos🍭{blanc}")
        if comptador == 0:
            imprimir_como_maquina(f'{verd}felicidades!! Ningún error. Hasta la próxima👻{blanc}')
        else:
            calabaza = '🎃'
            imprimir_como_maquina(f'{vermell} has cometido {calabaza*int(comptador)} errores muajajajaja{blanc}')
            return False 

    elif casella == "⬜️":
        while True:
            
            # Triar una clau (que és la resposta) aleatòria del diccionari
            resposta_casella = random.choice(list(diccionari.keys()))

            # Obtenir la pregunta associada a la resposta i eliminar del diccionari
            pregunta_casella = diccionari.pop(resposta_casella)  
            imprimir_como_maquina(f"Pregunta: {groc}{pregunta_casella}\n{blau}PISTA: {len(resposta_casella)} letras\n{blanc}")
            resposta_jugador = input("Tu respuesta: ").lower()

            if resposta_jugador.lower().replace(' ','') == resposta_casella.lower():
                imprimir_como_maquina(f"{verd}Respuesta correcta. Puedes continuar explorando!!.👻{blanc}")
                mostrar_matriu(recorregut_jugador)
                break
            else:
                imprimir_como_maquina(f"{vermell}🎃 ...Respuesta incorrecta.🎃 La respuesta correcta era {verd} {resposta_casella} {vermell}Vuelve a intentar.{blanc}")
                
                comptador +=1
    elif casella == "👻":
        while True:
            
            # Triar una clau (que és la resposta) aleatòria del diccionari
            resposta_casella = random.choice(list(fantasmes.keys()))

            # Obtenir la pregunta associada a la resposta i eliminar del diccionari
            pregunta_casella = fantasmes.pop(resposta_casella)
            imprimir_como_maquina(f"Pregunta 👻 fantasma : {groc}{pregunta_casella}\n{blau}PISTA: {len(resposta_casella)} letras\n{blanc}")
            resposta_jugador = input("Tu respuesta: ").lower()

            if resposta_jugador.lower().replace(' ','') == resposta_casella.lower():
                imprimir_como_maquina(f"{verd}Respuesta correcta. Puedes continuar explorando!!.👻{blanc}")
                imprimir_como_maquina(f'{groc}Lo encontraras en {blau}{fantlink[resposta_casella]}{blanc}')
                mostrar_matriu(recorregut_jugador)
                break
            else:
                imprimir_como_maquina(f"{vermell}🎃 ...Respuesta incorrecta.🎃 La respuesta correcta era {verd} {resposta_casella} {vermell}Vuelve a intentar.{blanc}")
                
                comptador +=1

    return True

def moviments(fila, columna):
    options = ["norte", "este", "sur", "oeste", "salir"]
    
    
    if fila == 0 or (fila == 1 and columna == 0):
        options.remove("norte")
    if fila == len(habitacions) - 1:
        options.remove("sur")
    if columna == 0 or (fila == 0 and columna == 1):
        options.remove("oeste")
    if columna == len(habitacions[0]) - 1:
        options.remove("este")
    
    return options

def moure_jugador(posicio_jugador):
    fila, columna = posicio_jugador
    while True:
        opcions_moviment = moviments(fila,columna)
        imprimir_como_maquina(f"{blau}Opciones de movimiento disponibles:")
        print(f'{verd}{opcions_moviment}')
        direccio = input(f"{vermell}( ´◔ ω ◔`) {blau}Hacia dónde quieres ir? {blanc}").lower()

        if direccio == "salir":
            imprimir_como_maquina(f"{vermell}👻..Has decidido abandonar el juego..👻 bye!!{blanc}")
            return None  

        elif direccio in opcions_moviment:
            fila, columna = posicio_jugador

            if direccio == "norte":
                fila -= 1
            elif direccio == "sur":
                fila += 1
            elif direccio == "oeste":
                columna -= 1
            elif direccio == "este":
                columna += 1

            nova_posicio = (fila, columna)
            
            posicio_jugador = nova_posicio
            return posicio_jugador

        else:
            imprimir_como_maquina(f"{vermell}(㇏(•̀ᵥᵥ•́)) Movimiento no válido. Vuelve a intentar.{groc}⚡{blanc}")


# Inicializa la posición del jugador
posicio_jugador = (0, 0)  # (fila, columna)
# recorregut jugador
recorregut_jugador = [["🚪" for _ in range(4)] for _ in range(4)]
#  diccionaris encriptats
fantaslink = {'npvsfefw': 'iuuqt;00npvsfefw/dpn0', 'iemfpo': 'iuuqt;00iefmfpo/ofu0', 'ipmbnvoep': 'iuuqt;00ipmbnvoep/jp0', 'fmmbepefmnbm': 'iuuqt;00xxx/fmmbepefmnbm/dpn0', 'njevefw': 'iuuqt;00njev/efw0', 'tpzebmup': 'iuuqt;00xxx/zpvuvcf/dpn0Atpzebmup', 'gsjljefmup': 'iuuqt;00xxx/gsjljefmup/dpn0', 'epudtw': 'iuuqt;00xxx/zpvuvcf/dpn0AEpuDTW', 't5wjubs': 'iuuqt;00ibdl5v/jp0', 'dbsnfobotjp': 'iuuqt;00xxx/dbsnfobotjp/efw0'}
fantasma = {'npvsfefw': 'Àrvjêo!mb!ujfof!nât!mbshb@', 'iemfpo': 'Àdpo!rvjfo!qvfeft!bqsfoefs!jogpsnâujdp!b!sjunp!ef!ifbwz@', 'ipmbnvoep': 'Àrvjêo!mb!ujfof!nât!bodib@', 'fmmbepefmnbm': 'Àrvê!tjuf!dpouspmb!fm!ibdlfs!nât!gbnptp!ef!Ftqbòb@', 'njevefw': 'Àrvê!dsbdl!efm!kbwbtdsjqu!ujfof!vo!hfnfmp!fo!Mb!Sftjtufodjb@', 'tpzebmup': 'Àrvê!qsphsbnbeps!bshfoujop!ujfof!vob!wfmpdjebe!efm!ibcmb!efm!251&@', 'gsjljefmup': 'Àrvê!tfsîb!Kptê!Npub!tj!gvfsb!qsphsbnbeps@', 'epudtw': 'Àrvjêo!tfsâ!fm!qsjnfs!djcpsh!dpo!uboub!JB!rvf!ejwvmhb@', 't5wjubs': 'Àrvê!ibdlfs!ftuâ!qmbofboep!js!b!Boepssb@', 'dbsnfobotjp': 'ÀDpo!rvjêo!botîp!bqsfoefs!Tjhnb@'}
enigmatic = {'qjsbub': 'ÀRvê!uêsnjop!tf!vujmj{b!dpnûonfouf!qbsb!eftdsjcjs!b!vob!qfstpob!rvf!dpqjb!z!ejtusjcvzf!jmfhbmnfouf!tpguxbsf-!nûtjdb!p!qfmîdvmbt!fo!mîofb@', 'wjsvt': 'ÀRvê!ujqp!ef!tpguxbsf!nbmjdjptp!tf!sfqmjdb!z!tf!qspqbhb!b!usbwêt!ef!bsdijwpt!z!qsphsbnbt@', 'cpuofu': 'ÀDônp!tf!mmbnb!bm!dpokvoup!ef!psefobepsft!jogfdubept!dpouspmbept!qps!vo!djcfsefmjdvfouf@', 'Uspzbop': 'Àdônp!tf!mmbnb!fm!tpguxbsf!nbmjdjptp!b!usbwêt!efm!dvbm!mpt!ibdlfst!upnbo!dpouspm!efm!tjtufnb!dpo!fm!pckfujwp!ef!spcbs!ebupt!qfstpobmft', 'hvtbop': 'Àrvê!wjsvt!qvfef!jogfdubsuf!fm!psefobeps!nfejbouf!usbotgfsfodjb!ef!bsdijwpt@', 'sbotpnxbsf': 'Àrvê!ujqp!ef!wjsvt!dpotjtuf!fo!rvf!vo!ibdlfs!uf!cmprvfb!fm!psefobeps!z!uf!qjef!vob!sfdpnqfotb@', 'jmpwfzpv': 'Àrvê!wjsvt!uspzbop!jogfdup!61!njmmpoft!ef!psefobepsft!fo!vob!tfnbob!fo!fm!bòp!3111@', 'qijtijoh': 'Àrvê!uêdojdb!tvqmboub!mb!jefoujebe!ef!dpnqbòîbt!v!pshbojtnpt!qûcmjdpt!z!tpmjdjubo!jogpsnbdjôo!qfstpobm!z!cbodbsjb!bm!vtvbsjp@', 'EEpT': 'ÀRvê!ujqp!ef!bubrvf!jogpsnâujdp!dpotjtuf!fo!jovoebs!vo!tfswjeps!p!sfe!dpo!vob!hsbo!dboujebe!ef!tpmjdjuveft!qbsb!efkbsmb!jobddftjcmf@', 'ibdljoh': 'ÀDvâm!ft!fm!uêsnjop!rvf!tf!vujmj{b!qbsb!eftdsjcjs!mb!qsâdujdb!ef!cvtdbs!z!fyqmpubs!wvmofsbcjmjebeft!fo!tjtufnbt!jogpsnâujdpt@','qzuipo': 'ÀDvâm!ft!vo!mfohvbkf!ef!qsphsbnbdjôo!dpopdjep!qps!tv!tjnqmjdjebe!z!mfhjcjmjebe@', 'gboubtnb': 'ÀRvê!gjhvsb!ftqfdusbm!b!nfovep!tf!btpdjb!dpo!Ibmmpxffo@', 'djcfstfhvsjebe': 'ÀRvê!dbnqp!tf!fogpdb!fo!qspufhfs!tjtufnbt!ef!jogpsnbdjôo!dpousb!bubrvft@', 'bsbòb': 'ÀRvê!dsjbuvsb!qfmveb!z!ef!pdip!qbubt!ft!dpnûo!fo!Ibmmpxffo@', 'mjovy': 'ÀDvâm!ft!vo!tjtufnb!pqfsbujwp!ef!dôejhp!bcjfsup!bnqmjbnfouf!vujmj{bep@', '{pncjf': 'ÀRvê!tfs!op!nvfsup!b!nfovep!bqbsfdf!fo!qfmîdvmbt!z!kvfhpt!ef!{pncjft@', 'kbwb': 'ÀRvê!mfohvbkf!ef!qsphsbnbdjôo!ft!gbnptp!qps!tfs!(xsjuf!podf-!svo!bozxifsf(@', 'dbmbcb{b': 'ÀRvê!wfhfubm!tf!ubmmb!dpnûonfouf!dpnp!mjoufsob!fo!Ibmmpxffo@', 'ibdlfs': 'ÀRvê!uêsnjop!tf!vujmj{b!qbsb!eftdsjcjs!b!vob!qfstpob!rvf!bddfef!b!tjtufnbt!jogpsnâujdpt!tjo!bvupsj{bdjôo@', 'wbnqjsp': 'ÀRvê!dsjbuvsb!ef!mb!opdif!tf!bmjnfoub!ef!mb!tbohsf!ef!mpt!wjwpt@', 'qiq': 'ÀRvê!mfohvbkf!ef!qsphsbnbdjôo!tf!vujmj{b!dpnûonfouf!qbsb!fm!eftbsspmmp!xfc@', 'nvsdjfmbhp': 'ÀRvê!nbnîgfsp!wvfmb!z!ft!b!nfovep!btpdjbep!dpo!mb!opdif@', 'tfhvsjebejogpsnbujdb': 'ÀRvê!tf!sfgjfsf!b!qspufhfs!tjtufnbt!z!ebupt!dpousb!bnfob{bt!djcfsoêujdbt@', 'tjtufnbpqfsbujwp': 'ÀRvê!tpguxbsf!dpouspmb!fm!ibsexbsf!ef!vob!dpnqvubepsb!z!benjojtusb!sfdvstpt@', 'npnjb': 'ÀRvê!tfs!tf!fowvfmwf!fo!wfoebt!z!ft!vo!ufnb!dpnûo!fo!qfmîdvmbt!ef!bwfouvsbt@', 'djcfsbubrvf': 'ÀRvê!uêsnjop!tf!vujmj{b!qbsb!eftdsjcjs!vo!bubrvf!nbmjdjptp!fo!mîofb@', 'csvkb': 'ÀRvê!gjhvsb!b!nfovep!tf!sfqsftfoub!wpmboep!fo!vob!ftdpcb!z!mbo{boep!ifdij{pt@', 'gjsfxbmm': 'ÀRvê!tf!vujmj{b!qbsb!gjmusbs!fm!usâgjdp!ef!sfe!op!eftfbep@', 'ftrvfmfup': 'ÀRvê!ftusvduvsb!joufsob!efm!dvfsqp!ivnbop!b!nfovep!tf!btpdjb!dpo!Ibmmpxffo@', 'djcfsefmjodvfouf': 'ÀRvê!uêsnjop!tf!vujmj{b!qbsb!eftdsjcjs!b!vob!qfstpob!rvf!dpnfuf!efmjupt!fo!mîofb@', 'ubsbouvmb': 'ÀRvê!dsjbuvsb!ef!pdip!qbubt!qfmvebt!b!nfovep!dbvtb!ufnps!fo!mb!hfouf@', 'dsjquphsbgjb': 'ÀRvê!uêdojdb!tf!vujmj{b!qbsb!qspufhfs!mb!jogpsnbdjôo!nfejbouf!mb!dpejgjdbdjôo@', 'esbdvmb': 'ÀRvê!qfstpobkf!mjufsbsjp!z!djofnbuphsâgjdp!ft!dpopdjep!qps!cfcfs!tbohsf@', 'nbmxbsf': 'ÀRvê!ujqp!ef!tpguxbsf!nbmjdjptp!qvfef!ebòbs!vob!dpnqvubepsb!p!spcbs!ebupt@', 'ftqboubqbkbspt': 'ÀRvê!gjhvsb!tf!dpmpdb!fo!mpt!dbnqpt!qbsb!btvtubs!b!mbt!bwft@'}
# diccionaris desencriptats:
diccionari= desencriptar_diccionari(enigmatic)
fantasmes = desencriptar_diccionari(fantasma)
fantlink = desencriptar_diccionari(fantaslink)

if __name__ == '__main__':
    # benvinguda al joc
    imprimir_como_maquina(f"{groc}    ___ _                           _     _   ____      ")
    imprimir_como_maquina(f"{groc}   / __(_) ___ _ ____   _____ _ __ (_) __| | / __ \ ___ ")   
    imprimir_como_maquina(f"{groc}  /__\// |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ / _` / __|")
    imprimir_como_maquina(f"{groc} / \/  \ |  __/ | | \ V /  __/ | | | | (_| | | (_| \__ \ ")
    imprimir_como_maquina(f"{groc} \_____/_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\ \__,_|___/ ")
    imprimir_como_maquina(f"{groc}                                 👻          \____/     ")
    imprimir_como_maquina(f"{vermell}  👻       _            _          _  _   _")
    imprimir_como_maquina(f"{vermell}      __ _| |  _ 👻 ___| |_ ___   | || | / | ")
    imprimir_como_maquina(f"{vermell}     / _` | | | '__/ _ \ __/ _ \  | || |_| |  ")
    imprimir_como_maquina(f"{vermell}    | (_| | | | | |  __/ || (_) | |__   _| | ")
    imprimir_como_maquina(f"{vermell}     \__,_|_| |_|  \___|\__\___/     |_| |_|")
    imprimir_como_maquina(f"{blau} Encuentra el 🍭 que está dentro de la mansión del TERROR")
    imprimir_como_maquina(f"{verd} Trata de acertar todas las preguntas para no cargarte de 🎃!!")

    imprimir_como_maquina(f"{blau} Has entrado por el nordoeste 🚪")
    # crear les habitacions aleatoriament
    habitacions = crear_mansio()   
    # comptador d'errors
    comptador = 0    

    continuar_joc = True
    start_time = time.time()
    # comença el joc
    while continuar_joc:
        posicio_jugador = moure_jugador(posicio_jugador)
        if posicio_jugador is None:
            continuar_joc = False
        else:
            continuar_joc = avaluar_casella(posicio_jugador, diccionari, fantasmes)
