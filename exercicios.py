def Ex1():
    n = 1
    while n > 0:
        n = int(input("Informe um numero para saber o quadrado: "))
        if n > 0:
            print(n ** 2)
        elif n == 0:
            print("Fim do programa!")
        else:
            print("Numero invalido, fim do programa")
#------------------------------------------------------------------------------#
def Ex2():
    n = int(input("Informe o termo 'n':"))
    while n <= 0:
        n = int(input("Informe o termo 'n':"))
    cont = 1
    soma = 0
    while cont <= n:
        soma = soma + cont
        cont += 1
    print(soma)
#------------------------------------------------------------------------------#
def Ex3():
    n = int(input("Informe o termo 'n':"))
    while n <= 0:
        n = int(input("Informe o termo 'n':"))
    cont = 0
    impar = 1
    while cont < n:
        if impar % 2 == 0:
            impar += 1
        else:
            print(impar)
            impar += 1
            cont += 1
#------------------------------------------------------------------------------#
def Ex4():
    x = int(input("Informe o termo 'x':"))
    n = int(input("Informe o termo 'n':"))
    while n <= 0:
        n = int(input("Informe o termo 'n':"))
    print(x ** n)
#------------------------------------------------------------------------------#
def Ex5():
    dias = 31
    vendas = 0
    cont = 1
    maior = 0
    totalVendas = 0
    while cont <= dias:
        vendas = int(input("\nInforme a venda: "))
        totalVendas += vendas
        if vendas > maior:
            maior = cont
        cont += 1
    print("\nDia da maior venda:")
    print(maior)
    print("\nTotal vendido:")
    print(totalVendas)
#------------------------------------------------------------------------------#
def Ex6():
    n = int(input("Numero de alunos:"))
    notaMax = 100
    notaMin = 0
    cont = 1
    maior = 0
    menor = 0
    while cont <= n:
        nota = int(input("Informe a nota:"))
        while nota > 100 or nota < 0:
            nota = int(input("Informe uma nota valida:"))
        if cont == 1:
            maior = nota
            menor = nota
        elif nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota
        else:
            pass
        cont += 1
    print("\nMaior nota:")
    print(maior)
    print("\nMenor nota:")
    print(menor)
#------------------------------------------------------------------------------#
def Ex7():
    n = int(input("Informe o termo 'n':"))
    soma = 0
    cont = 1
    while cont <= n:
        num = int(input("Informe o numero: "))
        if num % 2 == 0:
            soma += num
        cont += 1
    print("\nSoma dos numeros pares:")
    print(soma)
#------------------------------------------------------------------------------#
def Ex8():
    n = int(input("Informe o termo 'n':"))
    while n <= 0:
        n = int(input("Informe o termo 'n':"))
    cont = 1
    result = 1
    while cont <= n:
        result *= cont
        cont += 1
    print(result)
#------------------------------------------------------------------------------#
def Ex9():
    n = int(input("Informe o termo 'n':"))
    i = int(input("\nInforme o termo 'i':"))
    j = int(input("\nInforme o termo 'j':"))
    mult = 0
    cont = 0
    while cont < n:
        if mult % i == 0 or mult % j == 0:
            print(mult)
            cont += 1
        mult += 1
#------------------------------------------------------------------------------#
def Ex10():
    n = int(input("Informe o termo 'n':"))
    while n <= 0:
        n = int(input("Informe o termo 'n':"))
    cont = 1
    result = 1
    while cont <= n/2:
        result = cont * (cont + 1) * (cont + 2)
        if result == n:
            break
        cont += 1
    if result == n:
        print("\nO numero e triangular")
    else:
        print("\nO numero nao e triangular")
#------------------------------------------------------------------------------#
def Ex11():
    n = int(input("Informe o termo 'n':"))
    cont = 2
    primo = True
    while cont < n/2:
        if n % cont == 0:
            primo = False
            break
        cont += 1
    if primo == True:
        print("\nO numero %d e primo" %(n))
    else:
        print("\nO numero %d nao e primo" %(n))
#------------------------------------------------------------------------------#
def Ex12():
    '''
    Programa que lê um dois inteiro positivos n e m e imprime o 
    máximo divisor comum (mdc) de n e m.

    Exemplos de execução

    Digite o valor de n (n > 0): 15
    Digite o valor de m (m > 0): 24
    MDC(15,24)=3

    Digite o valor de n (n > 0): 315
    Digite o valor de m (m > 0): 125
    MDC(315,125)=5

    Digite o valor de n (n > 0): 7
    Digite o valor de m (m > 0): 5
    MDC(7,5)=1
    '''

    print("Determina o mdc de dois números n > 0 e m > 0\n")

    # leia o valor de n
    n = int(input("Digite o valor de n (n > 0): "))

    # leia o valor de m
    m = int(input("Digite o valor de m (m > 0): "))

    # em cada iteração mdc é o candidato a mdc(n,m)
    mdc = n
    while n % mdc != 0 or m % mdc != 0: 
        mdc = mdc - 1

    print("MDC(%d,%d)=%d" %(n,m,mdc))

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#------------------------------------------------------------------------------#
def Ex13():
    '''
    Programa que lê um inteiro positivos n e verifica e imprime uma
    mensagem indicando se n é perfeito.
    '''

    print("Determina se um número n é perfeito\n")

    # leia o valor de n
    n = int(input("Digite o valor de n: "))

    soma = 0
  
    for divisor in range(1,n):
        if n % divisor == 0:
            soma += divisor # soma = soma + divisor

    if n == soma:
        print("O numero %d é perfeito" %(n))
    else: 
        print("O numero %d nao é perfeito\n" %(n))
  
#------------------------------------------------------------------------------#
def Ex14():
    '''
    Programa que lê um inteiro positivos n e imprime o n-ésimo
    número de Fibonacci F_n.

    F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, F_5  = 5, ...
    '''

    print("Calcula o n-=esimo número de Fibonacci\n")

    # leia o valor de n
    n = int(input("Digite o valor de n (n > 0): "))

    f_ant   = 0
    f_atual = 1
    i       = 1  
  
    while i < n: # antes da comparação vale que f_atual == F(i)
        f_prox  = f_ant + f_atual
        f_ant   = f_atual
        f_atual = f_prox
        i       = i + 1

    print("F(%d) = %d" %(n,f_atual))
#------------------------------------------------------------------------------#
