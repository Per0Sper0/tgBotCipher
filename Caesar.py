def caesar(message , x ,language):
    RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    EU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    if language == "RU":
        alphabetH = RU
        alphabetL = RU.lower()
    if language == "EU":
        alphabetH = EU
        alphabetL = EU.lower()
    for i in message:
        if i in alphabetH:
            y = (alphabetH.find(i) + x) % len(alphabetH)
            result += alphabetH[y]
        elif i in alphabetL:
            y = (alphabetL.find(i) + x) % len(alphabetH)
            result += alphabetL[y]
        else:
            result += i
    return result

