n = int(input())

for i in range(n):
    diamantes = 0
    p_aberto = []
    entrada = input()

    for c in entrada:
        if(c == '<'):
            p_aberto.append(c)
        elif(c == '>' and len(p_aberto) > 0):
            diamantes = diamantes + 1
            p_aberto.pop()
    print(f'{diamantes}')