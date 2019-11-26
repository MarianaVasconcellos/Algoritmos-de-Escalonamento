import math
import random

# variáveis:

tcheg = []
burst = []
nome = []
count = 0
texec = 0
tesp = 0
tesp_medio = 0
soma = 0
retorno = 0
retorno_medio = 0
soma2 = 0
count2 = 0
retorn1 = 0

# menu:
escolha = 0


def print_(param):
    try:
        file = open()
    except err:
        print(err)

def fifo(n, m):
    global retorno1, count2, soma, count2, soma, tesp
    if m == 2:
        for i in range(n):
            nome.append(i)
            burst.append(random.randint(1, 100))
            tcheg.append(random.randint(1, 15))

    else:
        for i in range(n):
            b = int(input('P' + str(i) + 'Burst: '))
            t = int(input('P' + str(i) + 'Tempo de Chegada: '))
            nome.append(i)
            burst.append(b)
            tcheg.append(t)

    print('Menu')
    print('Processo', 'Burst', 'Chegada')

    for i in range(n):
        print("  ", nome[i], "     ", burst[i], "   ", tcheg[i])

    entrada = tcheg
    tempos = burst
    proc = nome

    for j in range(n):
        for i in range(n - 1):
            if entrada[i] > entrada[i + 1]:
                aux = entrada[i + 1]
                entrada[i + 1] = entrada[i]
                entrada[i] = aux
                aux = tempos[i + 1]
                tempos[i + 1] = tempos[i]
                tempos[i] = aux
                aux = proc[i + 1]
                proc[i + 1] = proc[i]
                proc[i] = aux

    print('FCFS:')
    print('Processo', 'Burst', 'Chegada')

    for i in range(n):
        print("  ", proc[i], "     ", tempos[i], "   ", entrada[i])

    for x in range(n):
        if x == 0:
            tesp = 0
            retorno1 = tempos[x]

            print('P', proc[x])
            print("Tempo de espera", tesp)
            print('Tempo de Retorno:', retorno1)
        else:
            count = tempos[x - 1] - entrada[x]
            tesp += count
            soma += tesp
            soma2 = tesp + tempos[x]
            retorno = soma2
            count2 += retorno

            print('P', proc[x])
            print('Tempo de espera:', tesp)
            print('Tempo de Retorno:', retorno)

        tesp_medio = soma / n
        retorno_medio = (count2 + retorno1) / n

        print('\nTempo Médio de Espera: ', tesp_medio)
        print('Tempo Médio de Retorno: ', retorno_medio)


def sjf(n, m):
    global retorno1, count2, soma, count2, soma, tesp
    if m == 2:
        for i in range(n):
            nome.append(i)
            burst.append(random.randint(1, 100))
            tcheg.append(random.randint(1, 15))

    else:
        for i in range(n):
            b = int(input('P' + str(i) + 'Burst: '))
            t = int(input('P' + str(i) + 'Tempo de Chegada: '))
            nome.append(i)
            burst.append(b)
            tcheg.append(t)

    print('Menu')
    print('Processo', 'Burst', 'Chegada')

    for i in range(n):
        print("  ", nome[i], "     ", burst[i], "   ", tcheg[i])

    print('SJF:')

    entrada = tcheg
    tempos = burst
    proc = nome

    for j in range(n):
        for i in range(n - 1):
            if tempos[i] > tempos[i + 1]:
                aux = tempos[i + 1]
                tempos[i + 1] = tempos[i]
                tempos[i] = aux
                aux = entrada[i + 1]
                entrada[i + 1] = entrada[i]
                entrada[i] = aux
                aux = proc[i + 1]
                proc[i + 1] = proc[i]
                proc[i] = aux

    print('SJF:')
    print('Processo', 'Burst', 'Chegada')

    for i in range(n):
        print("  ", proc[i], "     ", tempos[i], "   ", entrada[i])

    for x in range(n):
        if x == 0:
            tesp = 0
            retorno1 = tempos[x]

            print('P', proc[x])
            print("Tempo de espera", tesp)
            print('Tempo de Retorno:', retorno1)
        else:
            count = tempos[x - 1] - entrada[x]
            tesp += count
            soma += tesp
            soma2 = tesp + tempos[x]
            retorno = soma2
            count2 += retorno

            print('P', proc[x])
            print('Tempo de espera:', tesp)
            print('Tempo de Retorno:', retorno)

    tesp_medio = soma / n
    retorno_medio = (count2 + retorno1) / n

    print('\nTempo Médio de Espera: ', tesp_medio)
    print('Tempo Médio de Retorno: ', retorno_medio)


def round_robin(n, relogio, m):
    global i
    if m == 2:
        for i in range(n):
            nome.append(i)
            burst.append(random.randint(1, 100))
            tcheg.append(random.randint(1, 15))

    else:
        for i in range(n):
            b = int(input('P' + str(i) + 'Burst: '))
            t = int(input('P' + str(i) + 'Tempo de Chegada: '))
            nome.append(i)
            burst.append(b)
            tcheg.append(t)

        print('Menu')
        print('Processo', 'Burst', 'Chegada')

        for i in range(n):
            print("  ", nome[i], "     ", burst[i], "   ", tcheg[i])

        tempos = burst
        proc = []
        processados = []
        entrada = []
        fila = []
        soma = 0
        a = 0

        for i in range(n):
            if tempos[i] <= relogio:
                processados.append(tempos[i])

            else:
                trest = tempos[i] - relogio
                processados.append(relogio)
                fila.append(trest)

            entrada.append(tcheg[i])
            proc.append(nome[i])

        for y in fila:
            if y <= relogio:
                processados.append(y)

            else:
                trest = y - relogio
                fila.append(trest)
                processados.append(relogio)

            entrada.append(tcheg[i])
            proc.append(nome[i])

        print('Round Robin:')
        print('Processo', 'Burst', 'Chegada')

        for j in range(len(processados)):
            print("  ", proc[j], "     ", processados[j], "   ", entrada[j])

        for m in range(0, n):
            q = math.ceil(tempos[m] / relogio)
            count = relogio * q
            s = count - a
            a += tempos[m]

            if m == 0:
                tesp = count - entrada[m]
            else:
                if s <= 0:
                    tesp = count - entrada[m]
                else:
                    tesp = count - s - entrada[m]

            count2 = tesp + tempos[m]
            soma += tesp

            print('P', proc[m])
            print('Tempo de espera:', tesp)
            print('Tempo de Retorno:', count2)

        tesp_medio = soma / n
        retorno_medio = count2 / n
        print('\nTempo Médio de Espera: ', tesp_medio)
        print('Tempo Médio de Retorno: ', retorno_medio)

        for i in range(n):
            nome.append(i)
            burst.append(random.randint(1, 100))
            tcheg.append(random.randint(1, 15))

        for i in range(n):
            b = int(input('P' + str(i) + 'Burst: '))
            t = int(input('P' + str(i) + 'Tempo de Chegada: '))
            nome.append(i)
            burst.append(b)
            tcheg.append(t)

    print('Menu')
    print('Processo', 'Burst', 'Chegada')

    for i in range(n):
        print("  ", nome[i], "     ", burst[i], "   ", tcheg[i])

    tempos = burst
    proc = []
    processados = []
    entrada = []
    fila = []
    soma = 0
    a = 0

    for i in range(n):
        if tempos[i] <= relogio:
            processados.append(tempos[i])

        else:
            trest = tempos[i] - relogio
            processados.append(relogio)
            fila.append(trest)

        entrada.append(tcheg[i])
        proc.append(nome[i])

    for y in fila:
        if y <= relogio:
            processados.append(y)

        else:
            trest = y - relogio
            fila.append(trest)
            processados.append(relogio)

        entrada.append(tcheg[i])
        proc.append(nome[i])

    print('Round Robin:')
    print('Processo', 'Burst', 'Chegada')

    for j in range(len(processados)):
        print("  ", proc[j], "     ", processados[j], "   ", entrada[j])

    for m in range(0, n):
        q = math.ceil(tempos[m] / relogio)
        count = relogio * q
        s = count - a
        a += tempos[m]

        if m == 0:
            tesp = count - entrada[m]
        else:
            if s <= 0:
                tesp = count - entrada[m]
            else:
                tesp = count - s - entrada[m]

        count2 = tesp + tempos[m]
        soma += tesp

        print('P', proc[m])
        print('Tempo de espera:', tesp)
        print('Tempo de Retorno:', count2)

    tesp_medio = soma / n
    retorno_medio = count2 / n
    print('\nTempo Médio de Espera: ', tesp_medio)
    print('Tempo Médio de Retorno: ', retorno_medio)


def multinivel(n, relogio, m):
    if m == 2:
        for i in range(n):
            nome.append(i)
            burst.append(random.randint(1, 100))
            tcheg.append(random.randint(1, 15))
    else:
        for i in range(n):
            b = int(input('P' + str(i) + 'Burst: '))
            t = int(input('P' + str(i) + 'Tempo de Chegada: '))
            nome.append(i)
            burst.append(b)
            tcheg.append(t)

    print('Menu')
    print('Processo', 'Burst', 'Chegada')

    for i in range(n):
        print("  ", nome[i], "     ", burst[i], "   ", tcheg[i])

    entrada = []
    entrada2 = []
    tempos = burst
    proc = []
    proc2 = []
    processados = []
    fila = []

    for i in range(n):
        if tempos[i] <= relogio:
            processados.append(tempos[i])
            entrada.append(tcheg[i])
            proc.append(nome[i])

        else:
            trest = tempos[i] - relogio
            processados.append(relogio)
            fila.append(trest)
            entrada.append(tcheg[i])
            proc.append(nome[i])
            entrada2.append(tcheg[i])
            proc2.append(nome[i])

    print('Multinível:')
    print('Fila 1: ')
    print('Processo', 'Burst', 'Chegada')

    for j in range(len(processados)):
        print("  ", proc[j], "     ", processados[j], "   ", entrada[j])

    for y in range(len(fila) - 1):
        if fila[y] > fila[y + 1]:
            aux = fila[y + 1]
            fila[y + 1] = fila[y]
            fila[y] = aux
            aux = entrada2[y + 1]
            entrada2[y + 1] = entrada2[y]
            entrada2[y] = aux
            aux = proc2[y + 1]
            proc2[y + 1] = proc2[y]
            proc2[y] = aux

    print('Fila 2:')
    print('Processo', 'Burst', 'Chegada')

    for j in range(len(fila)):
        print("  ", proc2[j], "     ", fila[j], "   ", entrada2[j])


while escolha != 5:
    print('Menu: \n')
    print('1 - FIFO \n2 - SJF\n3 - ROUND ROBIN\n4 - MULTINÍVEL\n5 - SAIR DO PROGRAMA')

    escolha = int(input('Opção: '))

    if escolha == 1:
        n = int(input("Quantidade de processos: "))
        m = int(input("Burst manual ou aleatório?\n 1 - Manual\n 2 - Aleatório\n"))

        fifo(n, m)

    elif escolha == 2:
        n = int(input("Quantidade de processos: "))
        m = int(input("Burst manual ou aleatório?\n 1 - Manual\n 2 - Aleatório\n"))

        sjf(n, m)

    elif escolha == 3:
        n = int(input("Quantidade de processos: "))
        relogio = int(input('Quantum de tempo: '))
        m = int(input("Burst manual ou aleatório?\n 1 - Manual\n 2 - Aleatório\n"))

        round_robin(n, relogio, m)

    elif escolha == 4:
        n = int(input("Quantidade de processos: "))
        relogio = int(input('Quantum de tempo: '))
        m = int(input("Burst manual ou aleatório?\n 1 - Manual\n 2 - Aleatório\n"))

        multinivel(n, relogio, m)

    elif escolha == 5:
        print("FIM")
    else:
        print('Opção inválida. Escolha uma opção')
