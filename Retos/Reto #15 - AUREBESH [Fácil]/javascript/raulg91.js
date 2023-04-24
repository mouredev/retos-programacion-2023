let dic = {

    'a': 'aurek',
    'b': 'besh',
    'c': 'cresh',
    'd': 'dorn',
    'e': 'esk',
    'f': 'forn',
    'g': 'grek',
    'h': 'hierf',
    'i': 'isk',
    'j': 'jenth',
    'k': 'krill',
    'l': 'leth',
    'm': 'mern',
    'n': 'nern',
    'o': 'osk',
    'p': 'peth',
    'q': 'qek',
    'r': 'resh',
    's': 'senth',
    't': 'trill',
    'u': 'usk',
    'v': 'vek',
    'w': 'wesk',
    'x': 'xesh',
    'y': 'yirt',
    'z': 'zerek'
};

function swap_dic(dictionay) {

    let aux_dic = {};

    for (let i in dic) {
        aux_dic[dic[i]] = i;
    }

    return aux_dic;
}

function aurebesh(text) {


    let language = 'ES';
    let text_translation = "";
    let pos = 0;

    //Create aurebesh to Spanish dictiory    
    let dic2 = swap_dic(dic);

    //Detect language

    for (let j in dic2) {

        if (text.includes(j)) {

            //Means an Aurebesh character has been found
            language = 'AU';
        }
    }


    if (language == 'AU') {
        // Aurebesh to Spanish
        while(pos< text.length){
            for (let i in dic2) {
                if(text.indexOf(i)==pos){
                    text_translation += dic2[i];
                    pos = pos + i.length;
                }
            }

        }
      
    }
    else {
        //Spanish to Aurebesh
        for (let i of text) {

            text_translation += dic[i];
        }
    }
    return text_translation
}

//let text_original = "brais";
let text_original = "beshreshaurekisksenth";

console.log(aurebesh(text_original))