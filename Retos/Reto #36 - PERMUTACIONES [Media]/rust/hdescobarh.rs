// author: hdescobarh (Hans D. Escobar H.)

// Este modulo tiene mi solución
use crate::permutacion_naive::reordenar_texto;

fn main() {
    /*
    Implementación naive O(n!):
        -   case_sensitive
        -   acepta cualquier carácter Unicode (e.g., el texto '漢字한국어' es valido).

    Reordenar la secuencia es equivalente a,
    dada una secuencia de tamaño n, generar un arbol de n! hojas,
    con (n-k) ramificaciones desde cada nodo en el nivel k (0<=k<n), n,k\inℕ,
    siendo la raíz del arbol el nivel 0.
    */
    loop {
        let texto = match entrada_de_texto() {
            Some(string) => string,
            None => continue,
        };
        let para_imprimir: Vec<String> = reordenar_texto(texto);
        println!("{:?}", para_imprimir);
    }
}

mod permutacion_naive {

    /*
     * El algoritmo sigue una estructura de arbol en la que cada nodo, representado con el struct RamaArbol,
     * tiene una permutación de tamaño 0 <= t =< longitud_palabra (camino_secuencia) y una colección
     * de los longitud_palabra - t caracteres aún no incluidos (restantes).
     *
     * Ejemplo: el texto "abcd" la raíz comienza con un camino de 4 espacios vacíos y un restantes de 4;
     * En el siguiente nivel genera 4 nodos (uno por carácter restante), cada uno permutaciones de
     * tamaño 1 y un restantes de 3:
     *  - "a" y ['b', 'c', 'd']
     *  - "b" y ['a', 'c', 'd']
     *  - "c" y ['a', 'b', 'f']
     *  - "d" y ['a', 'b', 'c']
     */

    pub fn reordenar_texto(texto: String) -> Vec<String> {
        // Inicializa el nivel 0
        let tree_root = RamaArbol::desde_string(texto);
        // caché para la memoización. Se inicia con capacidad n! para reducir el allocation
        let mut cache: Vec<RamaArbol> =
            Vec::with_capacity(util_factorial(tree_root.restantes.len()));
        // El método para generar todas las hojas del arbol es recursivo
        RamaArbol::generar_hojas(&mut cache, vec![tree_root]);
        // Finalmente, extrae las secuencias de la caché para imprimirlas
        cache
            .into_iter()
            .map(|rama| rama.camino_secuencia)
            .collect()
    }

    #[derive(Clone)]
    struct RamaArbol {
        camino_secuencia: String,
        restantes: Vec<char>,
    }

    impl RamaArbol {
        pub fn desde_string(s: String) -> Self {
            RamaArbol {
                camino_secuencia: String::with_capacity(s.len()),
                restantes: s.chars().collect(),
            }
        }

        /**
         * Genera todas las posibles ramas a partir de una rama
         */
        fn ramificar(ramas: RamaArbol) -> Vec<RamaArbol> {
            if ramas.restantes.is_empty() {
                panic!("No puede generar mas ramas!");
            }
            let mut nuevas_ramas: Vec<RamaArbol> = Vec::with_capacity(ramas.restantes.len());
            for indice in 0..ramas.restantes.len() {
                /*Hace una deep copy de la Rama, remueve un caracter en el indice de los restantes
                y lo agrega al final de la secuencia */
                let mut rama: RamaArbol = ramas.clone();
                rama.camino_secuencia
                    .push(rama.restantes.swap_remove(indice));
                nuevas_ramas.push(rama);
            }
            nuevas_ramas
        }

        fn generar_hojas(resultado: &mut Vec<RamaArbol>, base: Vec<RamaArbol>) {
            for rama in base {
                if rama.restantes.is_empty() {
                    resultado.push(rama);
                } else {
                    let nueva_base = RamaArbol::ramificar(rama);
                    RamaArbol::generar_hojas(resultado, nueva_base);
                };
            }
        }
    }

    fn util_factorial(numero: usize) -> usize {
        let mut resultado = 1;
        for valores in 1..(numero + 1) {
            resultado *= valores;
        }
        resultado
    }
}

use std::io;

/**
 * Se encarga de imprimir mensajes en consola y del parsing del input del usuario
 */
pub fn entrada_de_texto() -> Option<String> {
    println!("Ingrese el texto a permutar (o '0' para salir):\n");

    let mut input: String = String::new();
    // Validar la entrada
    io::stdin()
        .read_line(&mut input)
        .expect("Error al leer la entrada.\n");

    // Detectar si hay código de salida
    if let Ok(numero) = input.trim().parse::<usize>() {
        if numero == 0 {
            println!("Saliendo...\n");
            std::process::exit(0);
        }
    };

    if input.chars().count() > 11 {
        println!("La longitud es muy grande para el algoritmo implementado.\n");
        None
    } else {
        Some(input.trim().to_string())
    }
}

// Unit Tests
#[cfg(test)]
mod test {
    use super::*;
    use std::collections::HashSet;

    #[test]
    fn manejo_texto_vacio_correcto() {
        let resultado: HashSet<String> = reordenar_texto(String::from("")).into_iter().collect();
        let esperado = HashSet::from(["".to_string()]);
        assert!(esperado == resultado);
    }

    #[test]
    fn reordena_texto_minimo() {
        let resultado: HashSet<String> = reordenar_texto(String::from("ab")).into_iter().collect();
        let esperado: HashSet<String> = ["ab", "ba"].into_iter().map(|s| s.to_string()).collect();
        assert!(esperado == resultado);
    }

    #[test]
    fn reordena_texto_con_mayusculas() {
        let resultado: HashSet<String> =
            reordenar_texto(String::from("hLOa")).into_iter().collect();
        let esperado: HashSet<String> = [
            "hOLa", "OhLa", "LhOa", "hLOa", "OLha", "LOha", "LOah", "OLah", "aLOh", "LaOh", "OaLh",
            "aOLh", "ahLO", "haLO", "LahO", "aLhO", "hLaO", "LhaO", "OhaL", "hOaL", "aOhL", "OahL",
            "haOL", "ahOL",
        ]
        .into_iter()
        .map(|s| s.to_string())
        .collect();
        assert!(esperado == resultado);
    }

    #[test]
    fn reordena_palabra_longitud_seis() {
        let resultado: HashSet<String> = reordenar_texto(String::from("celula"))
            .into_iter()
            .collect();
        let esperado: HashSet<String> = [
            "celula", "eclula", "lceula", "cleula", "elcula", "lecula", "leucla", "elucla",
            "ulecla", "luecla", "eulcla", "uelcla", "uclela", "culela", "lucela", "ulcela",
            "cluela", "lcuela", "eculla", "ceulla", "ueclla", "euclla", "cuella", "ucella",
            "lcelua", "clelua", "elclua", "leclua", "cellua", "ecllua", "llecua", "ellcua",
            "lelcua", "clleua", "lcleua", "llceua", "lulcea", "ullcea", "llucea", "luclea",
            "ulclea", "clulea", "lculea", "ucllea", "cullea", "clluea", "lcluea", "llcuea",
            "elulca", "leulca", "uellca", "eullca", "luelca", "ulelca", "ulleca", "luleca",
            "llueca", "leluca", "elluca", "lleuca", "leluac", "elluac", "lleuac", "leulac",
            "elulac", "ulelac", "luelac", "eullac", "uellac", "ulleac", "luleac", "llueac",
            "aleluc", "laeluc", "ealluc", "aelluc", "lealuc", "elaluc", "ellauc", "lelauc",
            "lleauc", "laleuc", "alleuc", "llaeuc", "ualelc", "aulelc", "luaelc", "ulaelc",
            "aluelc", "lauelc", "laeulc", "aleulc", "elaulc", "leaulc", "aelulc", "ealulc",
            "eulalc", "uelalc", "leualc", "elualc", "ulealc", "luealc", "auellc", "uaellc",
            "eaullc", "aeullc", "ueallc", "euallc", "lualec", "ulalec", "alulec", "laulec",
            "uallec", "aullec", "llauec", "alluec", "laluec", "ullaec", "lulaec", "lluaec",
            "aelclu", "ealclu", "laeclu", "aleclu", "elaclu", "leaclu", "lecalu", "elcalu",
            "clealu", "lcealu", "eclalu", "celalu", "calelu", "aclelu", "lcaelu", "claelu",
            "alcelu", "lacelu", "eacllu", "aecllu", "ceallu", "ecallu", "acellu", "caellu",
            "laelcu", "alelcu", "elalcu", "lealcu", "aellcu", "eallcu", "lleacu", "ellacu",
            "lelacu", "allecu", "lalecu", "llaecu", "lclaeu", "cllaeu", "llcaeu", "lcaleu",
            "claleu", "alcleu", "lacleu", "calleu", "aclleu", "allceu", "lalceu", "llaceu",
            "elclau", "leclau", "cellau", "ecllau", "lcelau", "clelau", "clleau", "lcleau",
            "llceau", "lelcau", "ellcau", "llecau", "leucal", "elucal", "ulecal", "luecal",
            "eulcal", "uelcal", "ueclal", "euclal", "cuelal", "ucelal", "eculal", "ceulal",
            "clueal", "lcueal", "ucleal", "culeal", "luceal", "ulceal", "elcual", "lecual",
            "celual", "eclual", "lceual", "cleual", "aleucl", "laeucl", "ealucl", "aelucl",
            "leaucl", "elaucl", "eluacl", "leuacl", "uelacl", "eulacl", "lueacl", "uleacl",
            "uaelcl", "auelcl", "eualcl", "uealcl", "aeulcl", "eaulcl", "lauecl", "aluecl",
            "ulaecl", "luaecl", "aulecl", "ualecl", "caleul", "acleul", "lcaeul", "claeul",
            "alceul", "laceul", "laecul", "alecul", "elacul", "leacul", "aelcul", "ealcul",
            "eclaul", "celaul", "lecaul", "elcaul", "cleaul", "lceaul", "acelul", "caelul",
            "eaclul", "aeclul", "cealul", "ecalul", "ucalel", "cualel", "auclel", "uaclel",
            "caulel", "aculel", "acluel", "caluel", "lacuel", "alcuel", "clauel", "lcauel",
            "luacel", "ulacel", "alucel", "laucel", "ualcel", "aulcel", "culael", "uclael",
            "lcuael", "cluael", "ulcael", "lucael", "eucall", "uecall", "ceuall", "ecuall",
            "uceall", "cueall", "cuaell", "ucaell", "acuell", "cauell", "uacell", "aucell",
            "aecull", "eacull", "caeull", "aceull", "ecaull", "ceaull", "ueacll", "euacll",
            "auecll", "uaecll", "eaucll", "aeucll", "alucle", "laucle", "ualcle", "aulcle",
            "luacle", "ulacle", "ulcale", "lucale", "culale", "uclale", "lcuale", "cluale",
            "caulle", "aculle", "ucalle", "cualle", "auclle", "uaclle", "lacule", "alcule",
            "claule", "lcaule", "aclule", "calule", "laluce", "alluce", "llauce", "laulce",
            "alulce", "ulalce", "lualce", "aullce", "uallce", "ullace", "lulace", "lluace",
            "clalue", "lcalue", "acllue", "callue", "laclue", "alclue", "allcue", "lalcue",
            "llacue", "lclaue", "cllaue", "llcaue", "luclae", "ulclae", "clulae", "lculae",
            "ucllae", "cullae", "llcuae", "clluae", "lcluae", "ullcae", "lulcae", "llucae",
        ]
        .into_iter()
        .map(|s| s.to_string())
        .collect();
        assert!(esperado == resultado);
    }
}
