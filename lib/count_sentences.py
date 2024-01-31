#!/usr/bin/env python3

class MyString:

    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if type(new_value) != str:
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else:
            return False
    
    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False
    
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False
    
    def count_sentences(self):
        copy = self.value.replace("!" , "\n").replace("?" , "\n").replace("." , "\n").splitlines()
        length_of_sentences = [item for item in copy if len(item) >= 1]
        return len(length_of_sentences)

string_1 = MyString("This is a sentence with a period. It has three sentences!! wow???")
string_2 = MyString("This is a sentence without a period")
string_3 = MyString("This is a sentence with a question mark?")

string_1.count_sentences()
dir(str)