from random import randint
from Viegener import viegener

def vernam(language,message,flag):
        coder = ""
        RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        EU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if language == "RU":
            alphabet = RU
            for i in range(len(message)):
                coder += alphabet[randint(0,32)]
        if language == "EU":
            alphabet = EU
            for i in range(len(message)):
                coder += alphabet[randint(0,25)]
        return coder, viegener(language,coder,message,flag)




