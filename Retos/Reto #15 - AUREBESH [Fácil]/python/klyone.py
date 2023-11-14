#!/usr/bin/env python3

import re

translation_dict = {
    "a" : "<aurek>",
    "b" : "<besh>",
    "c" : "<cresh>",
    "d" : "<dorn>",
    "e" : "<esk>",
    "f" : "<forn>",
    "g" : "<grek>",
    "h" : "<herf>",
    "i" : "<isk>",
    "j" : "<jenth>",
    "k" : "<krill>",
    "l" : "<leth>",
    "m" : "<mern>",
    "n" : "<nern>",
    "o" : "<osk>",
    "p" : "<peth>",
    "q" : "<qek>",
    "r" : "<resh>",
    "s" : "<senth>",
    "t" : "<trill>",
    "u" : "<usk>",
    "v" : "<vev>",
    "w" : "<wesk>",
    "x" : "<xesh>",
    "y" : "<yirt>",
    "z" : "<zerek>",
    "<aurek>" : "a",
    "<besh>" : "b",
    "<cresh>" : "c",
    "<dorn>" : "d",
    "<esk>" : "e",
    "<forn>" : "f",
    "<grek>" : "g",
    "<herf>" : "h",
    "<isk>" : "i",
    "<jenth>" : "j",
    "<krill>" : "k",
    "<leth>" : "l",
    "<mern>" : "m",
    "<nern>" : "n",
    "<osk>" : "o",
    "<peth>" : "p",
    "<qek>" : "q",
    "<resh>" : "r",
    "<senth>" : "s",
    "<trill>" : "t",
    "<usk>" : "u",
    "<vev>" : "v",
    "<wesk>" : "w",
    "<xesh>" : "x",
    "<yirt>" : "y",
    "<zerek>" : "z",
}

def generate_translation(word):
    if not word in translation_dict:
        if not word.lower() in translation_dict:
            return word
        else:
            return translation_dict[word.lower()].upper()
    else:
        return translation_dict[word]

def translate_from(language, text):
    if language != "natural" and language != "aurebesh":
        raise Exception()

    if language == "natural":
        regex = re.compile(".|\n")
    else:
        regex = re.compile("<\w+>|\s|\n")

    res = "".join(list(map(generate_translation, re.findall(regex, text))))

    return res

def print_result(text, translation):
   print(text + " => " + translation)

if __name__ == "__main__":
    txt = "hola amigos    mios"
    res = translate_from("natural", txt)
    print_result(txt, res)

    txt = "<herf><osk><leth><aurek> <aurek><mern><isk><grek><osk><senth>    <mern><isk><osk><senth>"
    res = translate_from("aurebesh", txt)
    print_result(txt, res)

    txt = "Este MENsaje tiene MayusCulas"
    res = translate_from("natural", txt)
    print_result(txt, res)

    txt = "<ESK><senth><trill><esk> <MERN><ESK><NERN><senth><aurek><jenth><esk> <trill><isk><esk><nern><esk> <MERN><aurek><yirt><usk><senth><CRESH><usk><leth><aurek><senth>"
    res = translate_from("aurebesh", txt)
    print_result(txt, res)
