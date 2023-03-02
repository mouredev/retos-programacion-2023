#!/usr/bin/env python3

class PhraseParser:
    def __clear_state(self):
        self.valid = False
        self.heterogram = False
        self.isogram = False
        self.panagram = False
        self.phrase = None
        self.state = {}

        for alpha in self.alphabet:
            self.state[alpha.lower()] = 0

    def __init__(self, alphabet=None, ignore_spaces=True):
        if alphabet == None:
            self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        else:
            self.alphabet = alphabet.lower()

        self.__clear_state()
        self.ignore_spaces = ignore_spaces

    def __check_heterogram(self):
        self.heterogram = True
        for s in self.state:
            if self.state[s] > 1:
                self.heterogram = False
                break

    def __check_isogram(self):
        self.isogram = True
        requested_amount = -1

        for s in self.state:
            if requested_amount == -1 and self.state[s] > 0:
                requested_amount = self.state[s]
            else:
                if self.state[s] > 0 and self.state[s] != requested_amount:
                    self.isogram = False
                    break

    def __check_panagram(self):
        self.panagram = True

        for s in self.state:
            if self.state[s] == 0:
                self.panagram = False
                break

    def parse(self, phrase):
        self.__clear_state()
        self.phrase = phrase
        self.valid = True

        for s in phrase:
            if self.ignore_spaces and s.isspace():
                continue
            if not s.lower() in self.alphabet:
                self.valid = False
                break
            self.state[s.lower()] = self.state[s.lower()] + 1

        self.__check_heterogram()
        self.__check_isogram()
        self.__check_panagram()

    def is_valid(self):
        return self.valid

    def is_heterogram(self):
        return self.heterogram

    def is_isogram(self):
        return self.isogram

    def is_panagram(self):
        return self.panagram

def check_phrase(parser, phrase):
    parser.parse(phrase)
    print("---------------------------------")
    print("Phrase: " + phrase)
    print("Valid: " + str(parser.is_valid()))
    print("Heterogram: " + str(parser.is_heterogram()))
    print("Isogram: " + str(parser.is_isogram()))
    print("Panagram: " + str(parser.is_panagram()))
    print("---------------------------------")

if __name__ == "__main__":
    parser = PhraseParser()
    check_phrase(parser, "aba 123")
    check_phrase(parser, "abc")
    check_phrase(parser, "abba baba")
    check_phrase(parser, "abcdefghi jklmnopqrst uvw xyzz")
    check_phrase(parser, "abcdefghi jklmnopqrst uvw xyz")
