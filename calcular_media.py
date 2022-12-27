
def média_notas():

    print("digite seu nome:")
    nome = input()
    Matemática = float(input(" Digite sua nota "))
    Português = float(input(" Digite sua nota "))
    Física = float(input(" Digite sua nota "))
    História = float(input(" Digite sua nota "))

    Média = (Matemática + Português + Física + História) / 4
    alunos = {}
    if Média  >= 7:
        print(' Parabéns {} '.format(nome)+(f' sua média é {Média} '))
    else:
        print('Continue estudando {}'.format(nome))
    return alunos

média_notas()

alunos = alunos