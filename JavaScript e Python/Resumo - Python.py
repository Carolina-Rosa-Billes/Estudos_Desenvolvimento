# Operadores Matemáticos:
# + = adição.
# - = subtração
# * = multiplicação.
# / = divisão com casas decimais.
# // = divisão só com a parte inteira.
# % = resto da divisão.
# ** = potenciação.

# Operadore Relacionais:
# = = atribuição.
# == = igualdade.
# > = maior.
# < = menor.
# >= = maior ou igual.
# <= = menor ou igual.
# != = diferente.

# Operadores Booleanos:
# Not = não.
# And = e.
# Or = ou.

# Álgebra Booleana:
# 1º (); []; {}.
# 2º 2; √.
# 3º *; /; %.
# 4º +; -.
# 5º Operadores Relacionais.
# 6º Not.
# 7º And.
# 8º Or.
# 9º =.

# Operadores de Atribuição:
# a += 1 === a = a + 1.
# a -= 1 === a = a - 1.
# a *= 1 === a = a * 1.
# a /= 1 === a = a / 1.
# a **= 1 === a = a ** 1.
# a //= 1 === a = a // 1.

# Estruturas de Dados
# () = Tuplas.
# [] = Listas.
# {} = Dicionários.

# Print (imprimir)
print ('Olá, mundo!')
print (2 + 3)
print ('2 + 3')

# Concatenação
print ('2' + '3')
print ('Olá, ' + 'mundo!')
print ('Olá,','mundo!')
print ('O resultado de 2 + 3 é', 2 + 3)

# Atribuição
nota = 8.5
disciplina = 'Lógica de Programação e Algoritmos'
print (nota)
print (disciplina)
print ('Disciplina:',disciplina,'Nota:',nota)

# Variável Numérica
print (int(3))
print (float(3.3))

# Variável Booleana
a = 1
b = 5
print (a == b)
print (a != b)

# Variável String
frase = 'Olá, mundo!'
print (frase)
print (frase [2])

# Concatenação de String
s1 = 'Lógica de Programação'
s2 = s1 + ' e Algoritmos'
print (s2)
s3 = 'A' + '-' *10 + 'B'
print (s3)

# Composição de String
nota = 8.5
s1 = 'Você tirou %f na disciplina de Lógica de Programação e Algoritmos' % nota
print (s1)
s2 = 'Você tirou %.2f na disciplina de Lógica de Programação e Algoritmos' % nota
print (s2)
disciplina = 'Lógica de Programação e Algoritmos'
s3 = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina)
print (s3)
# %d ou %i = números inteiros.
# %f = foats, números com vírgula.
# %s = strings, caracteres.
disciplina = 'Lógica de Programação e Algoritmos'
s4 = 'Você tirou {} na disciplina de {}' .format(nota, disciplina)
print (s4)

# Fatiamento de String
s1 = 'Lógica de Programação e Algoritmos'
print (s1[0:6])
print (s1[24:34])
print (s1[:6])
# Sempre considerar um número a mais na conta. Se quiser até o 5, pedir até o 6.

# Len (tamanho)
s1 = 'Lógica de Programação e Algoritmos'
print (len(s1))

# Input (entrada)
nome1 = input ('Qual é o seu nome? ')
print (nome1)
nome2 = input ('Qual é o seu nome? ')
print ('Olá, %s Seja bem vinda!' % nome2)
print ('Olá, {} Seja bem vinda!' .format (nome2))

# Input com Resultados Numéricos
idade = int (input('Qual a sua idade? '))
print ('A sua idade é %d anos.' % idade)
nota = float (input('Qual a sua nota? '))
print ('A sua nota é %.2f.' % nota)

# Abs (valor absoluto)
abs (54 - 57)

# Min (valor minímo)
min (34, 29, 31)

# If (se) = Condicional Simples
a = int (input('Qual a sua idade? '))
b = int (input('Qual o seu peso? '))
if (a > b):
  print ('Sua idade é maior que seu peso.')

# Else (senão) = Condicional Composta
a = int (input('Qual a sua idade? '))
if (a % 2 == 0):
  print ('O número é par!')
else:
  print ('O número é ímpar!')

# Not (não)
a = True
b = False
print (not a)
print (not b)
c = 10
d = 1
print (not c > d)

# And (e)
a = True
b = False
print (a and b)
c = 10
d = 1
e = 5.5
print (c > d and e == d)

# Or (ou)
a = True
b = False
print (a or b)
c = 10
d = 1
e = 5.5
print (c > d or e == d)

# Condicionais Aninhadas
print ('Escolha o que deseja comprar:')
print ('1 - Maçã')
print ('2 - Laranja')
print ('3 - Banana')
produto = int (input('Qual o número do produto que deseja comprar? '))
quantidade = int (input('Quantas unidades deseja comprar? '))
if (produto == 1):
  pagar = quantidade * 2.3
  print ('Você comprou %i maçãs. O total a pagar é %.2f.' % (quantidade, pagar))
else:
  if (produto == 2):
    pagar = quantidade * 3.6
    print ('Você comprou %i laranjas. O total a pagar é %.2f.' % (quantidade, pagar))
  else:
    if (produto == 3):
      pagar = quantidade * 1.85
      print ('Você comprou %i bananas. O total a pagar é %.2f.' % (quantidade, pagar))
    else:
      print ('Este número não corresponde a nenhum item. Por favor, tente novamente.')

# Elif (se-senão) = Condicional de Múltipla Escolha
print ('Escolha o que deseja comprar:')
print ('1 - Maçã')
print ('2 - Laranja')
print ('3 - Banana')
produto = int (input('Qual o número do produto que deseja comprar? '))
quantidade = int (input('Quantas unidades deseja comprar? '))
if (produto == 1):
  pagar = quantidade * 2.3
  print ('Você comprou %i maçãs. O total a pagar é %.2f.' % (quantidade, pagar))
elif (produto == 2):
    pagar = quantidade * 3.6
    print ('Você comprou %i laranjas. O total a pagar é %.2f.' % (quantidade, pagar))
elif (produto == 3):
      pagar = quantidade * 1.85
      print ('Você comprou %i bananas. O total a pagar é %.2f.' % (quantidade, pagar))
else:
  print ('Este número não corresponde a nenhum item. Por favor, tente novamente.')
# Simplificação da condicional aninhada, coloca else e if em um só: elif.

# While (enquanto) = Estrutura de repetição
a = 1
while (a <= 5):
  print (a)
  a = a + 1
inicial = int (input ('Qual o valor inicial? '))
final = int (input ('Qual o valor final? '))
while (inicial <= final):
  if (inicial % 2 == 0):
    print (inicial)
  inicial = inicial + 1
somar = 0
contar = 1
while (contar <= 5):
  a = float (input ('Digite a %iª nota: ' % contar))
  somar = somar + a
  contar = contar + 1
media = somar / 5
print ('Média final: {}.'.format(media))
# Variável Contadora = vai colocando valores constantes.
# Variável Acumuladora = vai somando valores diferentes.

# Validação de Dados de Entrada
a = int(input ('Digite um número maior que 0: '))
while (a <= 0):
  a = int(input ('Digite um número maior que 0: '))
print ('Você digitou %i. Parabéns!' % a)

# Break (sair) = Encerrar o Programa
print ('Digite uma mensagem. Ela será repetida! Caso deseje sair, escreva "Tchau!".')
while True:
  texto = input ('')
  print (texto)
  if (texto == 'Tchau!'):
    break
print ('Até a próxima!')

# Continue (voltar) = Voltar ao Início
while True:
  nome = input ('Qual o seu nome? ')
  if (nome != 'Carolina'):
    continue
  senha = input ('Qua a sua senha:')
  if (senha == '123'):
    break
print ('Acesso concedido!')

# For (para) = Estrutura de Repetição com Números Conhecidos
for a in range (6):
  print (a)
for a in range (2,6):
  print (a)
for a in range (0,6,2):
  print (a)
# In = no
# Range = intervalo

# Estruturas de Repetição Aninhadas
tabuada = 1
while (tabuada <= 10):
  print ('Tabuada do %i:' % tabuada)
  a = 1
  while (a <= 10):
    print ('%i x %i = %i' % (tabuada, a, tabuada * a))
    a += 1
  tabuada += 1
for tabuada in range (1, 11, 1):
  print ('Tabuada do %i:' % tabuada)
  for a in range (1, 11, 1):
    print ('%i x %i = %i' % (tabuada, a, tabuada * a))
tabuada = 1
while (tabuada <= 10):
  print ('Tabuada do %i:' % tabuada)
  for a in range (1, 11, 1):
    print ('%i x %i = %i' % (tabuada, a, tabuada * a))
  tabuada += 1

# Def (função definida)
def nome_da_funcao():
  print('O que quisermos repetir várias vezes.')
nome_da_funcao()
#Primeiro definimos o que vai acontecer na função, depois colocamos ela para rodar.

# Parâmetros
def nome_da_funcao(s1, int1, s2):
  print(s1)
  print(int1)
  print(s2)
nome_da_funcao('Olá, ', 0, 'mundo!')
nome_da_funcao(s2 = 'Olá, ', int1 = 0, s1 = 'mundo!')
def nome_da_funcao(a = 0, b = 0, c = 0):
  print(a + b + c)
nome_da_funcao(10, 15, 20)
nome_da_funcao(10, 15)
nome_da_funcao(10)
nome_da_funcao()

# Variáveis Locais e Globais
def comida():
  ovos = 'Variável Local da Comida'
  print(ovos)
def bacon():
  ovos = 'Variável Local do Bacon'
  print(ovos)
  comida()
  print(ovos)
ovos = 'Variável Global do Proprama Principal'
bacon()
print(ovos)

# Return (retorno)
def soma(a = 0, b = 0, c = 0):
  resposta = (a + b + c)
  return resposta
print(soma(1, 2, 3))

# Try (tentativa), Except (exceção) e Finally (finalmente) = Validação de Erros
while True:
  try:
    x = int(input('Por favor, digite um número: '))
    break
  except ValueError:
    print('Ops! Não é um número. Por favor, tente novamente.')
def divisao():
  try:
    numerador = int(input('Digite o numerador: '))
    denominador = int(input('Digite o denominador: '))
    resposta = numerador / denominador
  except ZeroDivisionError:
    print('Ops! É 0. Por favor, tente novamente.')
  except:
    print('Ops! Não deu certo. Por favor, tente novamente.')
  else:
    return resposta
  finally:
    print('Agradecemos a preferência!')
print(divisao())

# Lambda (função pequeninha)
potenciacao = lambda x: x * x
print(potenciacao(3))
soma = lambda x, y: x + y
print(soma(5, 10))

# Help (socorro)
help(print)

# Docstring (explicação da função)
def soma(a = 0, b = 0, c = 0):
  """
  Dá a doma de até três valores.
  a = primeiro valor (opcional).
  b = segundo valor (opcional).
  c = terceiro valor (opcional).
  """
  return (a + b + c)
print(soma(1, 2, 3))
help(soma)

# Tuplas ().
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila[0])
print(mochila[2])
print(mochila[0:2])
print(mochila[2:])
print(mochila[-1])
for item in mochila:
  print('Na minha mochila tem {}.'.format(item))
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade
print(mochila_grande)

# Desempacotamento de Parâmetros.
def soma(*num):
  soma = 0
  print('Fatores: {}.'.format(num))
  for a in num:
    soma += a
  return soma
print('Resultado: {}.'.format(soma(1, 2)))
print('Resultado: {}.'.format(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# Listas [].
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila)
mochila[2] = 'Laranja'
print(mochila)
mochila.append('Ovos')
print(mochila)
mochila.insert(1,'Canivete')
print(mochila)
del mochila[1]
print(mochila)
mochila.remove('Ovos')
print(mochila)

# Cópia de Listas.
a = [5, 7, 9, 11]
b = a
print(a)
print(b)
b[0] = 2
print(a)
print(b)
a = [5, 7, 9, 11]
b = a[:]
print(a)
print(b)
b[0] = 2
print(a)
print(b)

# Dupla Indexação.
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0][0])
print(mochila[2][3])
verdureira = [['Cebola', 0.39], ['Tomate', 0.49], ['Maçã', 0.89]]
print(verdureira[0])
print(verdureira[0][0])
print(verdureira[0][1])

# Dicionários {}.
games = {'Nome':'Super Mário',
         'Desenvolvedora':'Nintendo',
         'Ano':1990}
print(games)
print(games['Nome'])
print(games['Desenvolvedora'])
print(games['Ano'])
for a in games.values():
  print(a)
for a in games.keys():
  print(a)
for a,b in games.items():
  print('{} = {}'.format(a,b))

  # Alterando Strings.
s1 = list('Algoritmos')
print(s1)
print(''.join(s1))
s1[0] = 'a'
print(''.join(s1))

# Manipulando Strings.
s1 = 'Lógica de Programação e Algoritmos'
print(s1.startswith('Lógica'))
print(s1.endswith('Algoritmos'))
print(s1.lower())
print(s1.upper())
print(s1.count('a'))
print(s1.split(' '))
print(s1.replace('Algoritmos','Computação'))
print(s1.replace(' ','-', 2))

# Validação de Strings.
s1 = 'Lógica de Programação e Algoritmos'
s2 = '33'
print(s1.isalnum())
print(s2.isalnum())
print(s1.isalpha())
print(s1.isalpha())