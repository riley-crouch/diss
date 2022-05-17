import random
import csv

doRun = True

name = [
    ["João", "M"],
    ["Henrique", "M"],
    ["Vitor", "M"],
    ["Pedro", "M"],
    ["Antônio", "M"],
    ["Felipe", "M"],
    ["Thiago", "M"],
    ["Maria", "F"],
    ["Vêronica", "F"],
    ["Helena", "F"],
    ["Aline", "F"],
    ["Camila", "F"],
    ["Laís", "F"],
    ["Mariana", "F"],
    ["Rafa", "Q"],
    ["Alex", "Q"],
    ["Duda", "Q"],
    ["Andrea", "Q"],
    ["Dani", "Q"],
]

verb = [
    ["impressionou", "1"],
    ["supreendeu", "1"],
    ["se aproximou a", "1"],
    ["perseguiu", "1"],
    ["telefonou a", "1"],
    ["ama", "2"],
    ["matou", "2"],
    ["tem medo de", "2"],
    ["culpou", "2"],
    ["puniu", "2"],
    ["repreendeu", "2"],
    ["felicitou", "2"],
    ["admira", "2"],
]

data = []


def firstWord(s):
    return s.split()[0]


def test() -> list:
    nN = len(name) - 1
    nV = len(verb) - 1
    N1 = name[random.randint(0, nN)]
    N2 = name[random.randint(0, nN)]
    V = verb[random.randint(0, nV)]

    response = input(
        "Completa a frase.\n" +
        N1[0] + " " + V[0] + " " + N2[0] + " porque "
    )
    return [N1[1], N2[1], V[1], firstWord(response), response]


while doRun:
    l = len(data)
    data.append(test())
    if data[l][3] == "yeehaw":
        data.remove(data[l])
        doRun = False

file = open('data.txt', 'a')
for i in data:
    text = "\n" + i[0] + "," + i[1] + "," + i[2] + "," + i[3]+","+i[4]
    file.write(text)

file.close()
