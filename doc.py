'''

# Sites para praticar python:
- urionlinejudge.com.br
- hackerrank.com
- codechef.com
- codingame.com


########### APRENDENDO PYTHON: ###########

- VARIÁVEIS:
São valores armazenados que podem ser substituídos ao serem mencionados novamente (
    Ex:
    carro = 'Sienna'
    carro = 'Focus' (novo valor atribuído à variável 'carro')
    )

- NÚMEROS EM PYTHON:
int: números inteiros (ex: -3,-2,-1, 1, 2, 3)
float: números decimais (ex: 1.3, -3.5, 14123.1)
complex: números com incógnitas(ex: 2 + 3j, 3p * 2f)

- TEXTOS EM PYTHON:
str: textos entre aspas simples ou duplas (ex: 'Gabriel', "Rafael")
#: Usadas para comentar o código (O que estiver após a # não será compilado. ONELINE)
'''''': Usadas para comentar um bloco de código

- TIPOS DE DADOS:
type(dado): Usamos sempre que quiser saber que tipo de dado é a variável (
    Ex: 
    print(type(idade))
)

- ALTERANDO O TIPO DE VARIÁVEL (CASTING):
idade_inteiro = 22
idade_string = str(idade_inteiro)
idade_float = float(idade_inteiro)

- ESCOPO DE VARIÁVEIS:
GLOBAIS: Podem ser usadas por funções e manter o mesmo valor
(
    ex:
    x = 5
    def funcao():
        print(x)
)
LOCAIS: Sao variáveis criadas dentro das funçoes e nao podem ser usadas como globais
(
    ex:
    x = 5
    for i in range x:
        print(i)
)

- OPERADORES ARITMETICOS:
+ : soma
- : subtração
* : multiplicação
/ : divisão
** : exponenciação
// : divisão inteira
% : resto

- Boolean:
True: quando a condição é verdadeira
False: quando a condição é falsa

- Operadores de comparação: Retornam valores booleanos

== : Operador de igualdade
!= : Operador da diferença/não igualdade
> : Maior que
< : Menor que
>= : Maior ou igual a
<= : Menor ou igual a

- Condições: Caso uma condição seja satisfeira o bloco de código irá rodar

if: primeira condição 
(
    ex:
    x = 3
    if x == 3:
        print('Correto')
)
elif: Segunda/Terceira/Quarta... condição (Pode ser ou não acompanhada do IF)
(
    ex: 
    x = 3
    if x == 3:
        print('Correto')
    elif x == 5:
        print('Não errou e nem acertou')
)
else: Ultima condição (é sempre acompanhada do IF)
(
    ex: 
    x = 3
    if x == 3:
        print('Correto')
    elif x == 5:
        print('Segunda chance')
    elif x == 8:
        print('Terceira chance')
    else: 
        print('Errou')
)

- ESTRUTURAS DE REPETIÇÃO:
WHILE + condição: O laço se repitirá enquanto a condição nao for satisfeita: 
(
    ex:
    a = 0
    while a <= 5:
        print(a)
        if a == 3:
            break
        a = a + 1
)

FOR + range ou in:
    ex:
    s = 'pernambuco'
    for x in s:
        print(x)
    for x in range(5):
        print(x)
    for x in range(5, 10):
        print(x)
    for x in range(5, 100, 5):
    print(x)

# Trocando variaveis:

x = int(input('X = '))
y = int(input('Y = '))

temp = y
y = x
x = temp

print(f'X = {x}\nY = {y}')

# Numero positivo
n = int(input('Numero: '))

if n > 0:
    print(f'{n} é positivo')
elif n == 0:
    print(f'{n} é igual a 0')
else:
    print(f'{n} é negativo')

#Como saber se um numero é par

numero = int(input())

if(numero % 2) == 0:
    print(f'{numero} é par')
else:
    print(f'{numero} é ímpar')


#FATORIAL DE UM NÚMERO

numero = int(input('Digite o número a ser fatorado: '))

fatorial = 1

if numero < 0:
    print('Não existe fatorial de número negativo')
elif numero == 0:
    print('O fatorial de 0 é 1')
else:
    for x in range(1, numero + 1):
        fatorial = fatorial * x
    print(fatorial)



#Número primo
numero = int(input("Verifique um numero p saber se ele é primo: "))

if numero > 1:
    for x in range(2, numero):
        if numero % 2 == 0:
            print('Esse numero não é primo')
            break
    else:
        print('Esse número é primo')

else:
    print('Esse numero é menor que zero ou igual a 1')


# Pass(estruturas condicionais) e Continue(estruturas de repetição):
for x in range(1, 10):
    if x == 5:
        continue # Ao chegar no 5 interpretador irá sair do laço e continuar o código
                # Difente do break, que fará o código inteiro parar ao acatar a condição
if x == 5:
    pass


# Operadores de Atribuição:

x = 5
print(x)
x += 5
print(x)
x -= 5
print(x)
x *= 5
print(x)
x /= 5
print(x)
x **= 5
print(x)
x %= 4


####### Coleções: #######

nome = 'Chicago'

#print(nome[2]) Printa a letra da variavel nome com o index 2

for x in range(1,11,1): # contando de 1 a 10
    print(x)
for x in range(10,0,-1): # contando de 10 a 1
    print(x)

nome2 = 'Queens'

print(nome, end=' ') #Juntando duas saidas
print(nome2)

for x in nome:
    print(x, end= ' ')

print('\n')

x, y = 3, 5 
print(x, y)
x, y = y, x # Trocando variaveis

print(x, y)


# Listas:

lista = ['Gabriel', True, 3, 3.4]
print(lista) # Saida de dados da lista
print(type(lista)) # Tipo de lista
print(lista[0]) # Printando o dado no index 0
print(lista[-3]) #Index 1 do final da lista (invertida)


# Slicing (Em lista):

lista = ['Gabriel', True, 3, 3.4, 'Ferreira', 'Pato']

#print(lista[::])  Printa todos os elementos
#print(lista[2:])  Printa os elementos do index 2 ate o ultimo
#print(lista[:3])  Printa todos os elementos ate o index 3-1
#print(lista[1:4])  Printa o intervalo de elem. do index 1 ao 3-1
#print(lista[1:6:2]) Printa os el. de 1 a 5-1 de 2 em 2
#print(lista[0][2:5])  Pega o 1º ele da lista e printa o index 2 ao 5-1 ('bri')

# Funções (Coleções):

lista1 = [1, 5, 3]
lista2 = ['jane', 'gabriel', 'denis']
lista3 = ['rafa', 'teto', 'rafa']
lista2 = lista3 + lista2
# print(lista1)

#print(len(lista1))  Tamanho da lista 

# Funções para dados numericos:

print(sum(lista1)) # Soma todos os val da lista
print(max(lista1)) # Maior numero da lista
print(min(lista1)) # Menor val da lista


#Funões (List)
nome = 'Curso de Python'
valor = range(10)
print(nome)
print(valor)

lista_range = list(range(10))
lista_str = list("curso de python")
print(lista_range)
print(lista_str)
elemento = 7
if elemento in lista_str:
    print('Este elemento esta dentro da lista')



#Modificando items da lista:
print('-'*20)
lista = ["Gabriel", "Felipe", "David", "Rodrigo", "Isla", "Andreas", "Arão", "Arrascaeta", "Everton", "Bruno", "Gabigol"]
print(lista) #Printando a lista atual

#lista[1] = "Dantas" #trocando o item no index 1
#print(lista)

#lista[1:4] = ["vitor", "ruan", "diego"] Nindex = Nvalores Alterando os valores do 1 ao 3 com 3 elementos
#lista[1:2] = ["vitor", "ruan", "diego"] Nindex < Nvalores (1 - 3): os 3 valores irao entrar e os index seguintes irao se deslocar
#lista[1:5] = ["vitor", "Santana"] Nidex > Nvalores (4 - 2):  os 2 valores irao entrar e os index seguintes serao apagados
print(lista)


lista = ['a', 'b', 'c']
lista2 = [1, 2, 3]

lista = lista + lista2
print(lista)

#lista.extend(lista2)  Adiciona a lista2 atraves do .extend()

for x in lista2:
    lista.append(x) #Adiciona os elementos atraves do for

print(lista)


#Copia de uma lista, maneira 1:
lista = ['a', 'b', 'c']
print(lista)
lista2 = lista
print(lista2)

lista2.append('d') #Dessa forma, o que for adicionada em uma lista será adicionada em outra
lista.append('e') #Dessa forma, o que for adicionado nessa lista sera adicionado na outra

print(lista)
print(lista2)


# Copia de uma lista, maneira 2:
lista = ['a', 'b', 'c']
print(lista)
lista2 = lista.copy() #Com a função copy() as listas serao independentes
print(lista2)

lista2.append('d') # Ao usar append, a lista n será ligada a outra
lista.append('e')

print(lista)
print(lista2)


#Tuplas: São IMUTAVEIS, Armazenam diversos itens e sao ordenaveis(index) normalmente

tupla = ('item1', 'item2', 'item3', 'item1') # Sao feitas entre parenteses
print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla[2])
print(tupla.count('item1')) #Mostra quantos item1 tem na tupla
print(dir(tupla)) # Mostra as funcoes da tupla
#tupla.append('item4') Não possui append, nem varias outras por nao ser mutavel
print(tupla)'''


for x in range(10):
    x =input()

