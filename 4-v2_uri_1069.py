n = int(input())

for i in range(n):
    diamantes = 0
    aberto = 0
    entrada = input()

    for c in entrada:
        if(c == '<'):
            aberto = aberto + 1
        elif(c == '>' and aberto > 0):
            diamantes = diamantes + 1
            aberto = aberto - 1
    print(f'{diamantes}')
        