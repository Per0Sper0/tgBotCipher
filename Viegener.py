def viegener(language, coder, message,flag):
    RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    EU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    key = ""
    coder = coder.upper()
    if language == "RU":
        alphabetH = RU
        alphabetL = RU.lower()
        for i in coder:
            if i >= "А" and i <= "Я":
               key += i
    if language == "EU":
        alphabetH = EU
        alphabetL = EU.lower()
        for i in coder:
            if i >= "A" and i <= "Z":
               key += i
    while len(key) <= len(message):
        key += key
    for i in range(len(message)):
        if message[i] in alphabetH:
            y = (alphabetH.find(message[i]) + flag * alphabetH.find(key[i])) % len(alphabetH)
            result += alphabetH[y]
        elif message[i] in alphabetL:
            y = (alphabetL.find(message[i]) + flag * alphabetH.find(key[i])) % len(alphabetL)
            result += alphabetL[y]
        else:
            result += message[i]
    return(result)




