from Caesar import caesar
def hackcaesar(message, language):
    dictRU = {'А': 8.04,'Б': 1.55,'В': 4.75,'Г': 1.88,'Д': 2.95,'Е': 8.21,'Ё': 0.22,'Ж': 0.80,'З': 1.61,'И': 7.98,'Й': 1.36, 'К': 3.49,
                'Л': 4.32,'М': 3.11,'Н': 6.72,'О': 10.61,'П': 2.82, 'Р': 5.38,'С': 5.71,'Т': 5.83,'У': 2.28,'Ф': 0.41,
                'Х': 1.02,'Ц': 0.58, 'Ч': 1.23, 'Ш': 0.55,'Щ': 0.34,  'Ъ': 0.03,'Ы': 1.91,'Ь': 1.39,'Э': 0.31,'Ю': 0.63,'Я': 2.00}
    dictEU = {'A': 8.55,'B': 1.60,'C': 3.16,'D': 3.87,'E': 12.10,'F': 2.18,'G': 2.09,
              'H': 4.96,'I': 7.33,'J': 0.22,'K': 0.81,'L': 4.21,'M': 2.53,'N': 7.17,
              'O': 7.47,'P': 2.07,'Q': 0.10,'R': 6.33,'S': 6.73,'T': 8.94,
               'U': 2.68,   'V': 1.06,'W': 1.83,'X': 0.19,'Y': 1.72,'Z': 0.11,}
    RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    EU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    messagebeg = message
    message = message.upper()
    if language == "RU":
        alphabet = RU
        analys = list(dictRU.values())
    if language == "EU":
        alphabet = EU
        analys = list(dictEU.values())
    counter = 0
    dictAL = dict()
    for i in alphabet:
         dictAL[i] = 0
    for i in message:
        if i in alphabet:
            dictAL[i] += 1
            counter += 1
    for i in alphabet:
        dictAL[i] = round(dictAL[i] / counter * 100,2)
    text = list(dictAL.values())
    min = 10000
    x = 0
    for i in range(len(alphabet)):
        sum = 0
        for j in range(len(alphabet)):
            sum += (analys[j] - text[(i + j) % len(alphabet)]) ** 2
        if sum < min:
            min = sum
            x = i
    return caesar(messagebeg, -x, language)






