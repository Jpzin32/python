#ESCRITA
#jp = ('hello world')
#print (jp)
#print ('hello world')



#print('olá tudo bem?' , end=' ') #A mensagem vai aparecer sem quebra de linha (na mesma linha)
#print('como você está?') #A mensagem vai aparecer sem quebra de linha (na mesma linha)



#CONTAS
#jp2 = (7+4) #fazer contas não precisa usar o "('')"
#print(jp2) 
#print (7+4)



#ESCRITA COM NÚMERO
#jp3 = ('hello world' , 5)  #sem a virgula da erro Syntax
#print(jp3)
#print('hello world' , 5)
#print('olá' + 5) #(NÃO FUNCIONA)



#VARIAVEIS 
#nome = ('jonatha')
#idade = ('16')
#peso = ('60')
#print(nome, idade, peso)



#VARIAVEIS com INPUT(leia)
#nome = input('Qual seu nome?') #leia o nome
#idade = input('Qual a sua idade?')#leia a idade
#peso = input('Qual o seu peso?')#leia o peso
#print(nome, idade, peso) #imprimindo os resultados



#TIPOS DE VARIAVEIS
#int (número inteiro)
#float (número de ponto flutuante ou número real)  
#boll (boleano: True(Verdadeiro) False(Falso) A PRIMEIRA LETRA MAIÚSCULA)
#str (caracteres ('Olá'))



#n = bool(input('digite um numero'))
#print(n)
#aparace "true pois é verdade que tem um número dentro do "N" e caso n coloque nenhum número vai aparecer "false".



#DESAFIO GUSTAVO GUANABARA
#nome = input('Qual seu nome?') 
#print('bem vindo ao meu site' , nome)  



#DESAFIO 2 GUSTAVO GUANABARA
#dia = input ('qual o dia que você nasceu?')
#mes = input ('qual o mês que você nasceu?')
#ano = input ('qual o ano que você nasceu?')
#print ('o dia que você nasceu é:' , dia , 'o mês que você nasceu é:' , mes , ',o ano que você nasceu é:' , ano)



#DESAFIO 3 GUSTAVO GUANABARA
#numero = int (input ('digite o valor do primeiro número'))
#numero2 = int (input ('digite o valor do segundo número'))
#soma = (numero + numero2)
#print ('a resposta da sua soma é:' , s )   

#OU

#numero = input ('digite o valor do primeiro número')
#numero2 = input ('digite o valor do segundo número')
#print ('a soma...' , int(numero) + int(numero2))



#print('oi' * 5) #vai aparecer a msg 5 vezes



#nome = input('qual é seu nome?')
#print ('prazer em te conhecer {:>20}'.format(nome)) #A mensagem vai aparecer para o lado direito em 20 espaços utilizando o (":>20")
#print('prazer em te conhecer {:^20}'.format(nome)) #A mensagem vai centralizar em 20 espaços
#print('prazer em te conhecer {:=^20}'.format(nome)) #A mensagem vai aparecer centralizada em 20 espaços com "=" envolta dela



#DESAFIO GUSTAVO GUANABARA
#n = int(input('digite um número e veja seu antecessor e seu sucessor'))
#a = (n - 1)
#s = (n + 1)
#print('o antecessor de {} é {} e o sucessor é {}'.format(n, a, s))




#DESAFIO GUSTAVO GUANABARA
#n1 = int(input('digite o primeiro valor:'))
#d = (n1 * 2)
#t = (n1 * 3)
#r = (n1 **(1/2))
#print ('O dobro de {} é {} e o triplo de {} é {} e a raiz quadrada de {} é {}'.format(n1 , d , n1 , t , n1 , r))

#OU

#n1 = int(input('digite o valor:'))
#print ('O dobro de {} é {} \n e o triplo de {} é {} \n e a raiz quadrada de {} é {}'.format( n1 , (n1 * 2) , n1 , (n1 * 3) , n1 , (n1**(1/2)) ))



#DESAFIO GUSTAVO GUANABARA
#n1 = float(input('nota 1'))
#n2 = float(input('nota 2'))
#print ('o média dessas notas é: {}'.format((n1 + n2) / 2))



#DESAFIO GUSTAVO GUANABARA
#n1 = float(input('conversão de metros em km, cm e mm:'))
#print ('km = {}'.format(n1 / 1000))
#print ('cm = {}'.format(n1 * 100))
#print ('mm = {}'.format(n1 * 1000))



#DESAFIO GUSTAVO GUANABARA
#n1 = int(input('digite um número para ver sua tabuada'))
#print('a tabuada de {} x 1 é {}' .format( n1 ,(n1*1)))
#print('a tabuada de {} x 2 é {}' .format( n1 ,(n1*2)))
#print('a tabuada de {} x 3 é {}' .format( n1 ,(n1*3)))
#print('a tabuada de {} x 4 é {}' .format( n1 ,(n1*4)))
#print('a tabuada de {} x 5 é {}' .format( n1 ,(n1*5)))
#print('a tabuada de {} x 6 é {}' .format( n1 ,(n1*6)))
#print('a tabuada de {} x 7 é {}' .format( n1 ,(n1*7)))
#print('a tabuada de {} x 8 é {}' .format( n1 ,(n1*8)))
#print('a tabuada de {} x 9 é {}' .format( n1 ,(n1*9)))
#print('a tabuada de {} x 10 é {}' .format( n1 ,(n1*10)))



#DESAFIO GUSTAVO GUANABARA
#n1 =float(input('digite um número para convertelo em dolar e euro. R$'))
#print('o valor de {} em dolar é {:.2f}' .format(n1 , (n1 / 5.59)))
#print('o valor de {} em euro é {:.2f}' .format(n1 , (n1 / 5.99)))



#DESAFIO GUSTAVO GUANABARA
#leia =('digite a largura e altura para de respondermos o quanto de tinta você vai usar para pintar uma parede supondo que cada 1L de tinta pinta  2M²')
#n1 = float(input('digite a altura'))
#n2 = float(input('digite a largura'))
#print('a dimensão da sua parede é de {}x{} e a sua área é de {}M² e a quantidade de tinta utilizada vai ser {}L'.format(n1 , n2 , (n1 * n2) , (n1 * n2) /2))



#DESAFIO GUSTAVO GUANABARA
#n1 = float(input(('coloque o valor do seu produto e ganhe 5% de desconto R$')))
#print ('o desconto é de R${}'.format((n1 * 5) /100))
                                                  


#DESAFIO GUSTAVO GUANABARA
#n1 = float(input('digite o valor do salario R$'))
#s = float((n1 +(n1* 15 /100)))
#print('o valor do seu salario com o aumento de 15% é de R${:.2f}'.format(s))



#DESAFIO GUSTAVO GUANABARA
#C = int(input('adicione uma temperatura em C° para transformala em F°'))
#print('A temperatura em F° é {:.2f}'.format(C + 273))



#DESAFIO GUSTAVO GUANABARA
#d = int(input('quantos dias alugado?'))
#km =float(input('quantos KMS o carro tem rodado?:'))
#p = float((d * 60) + (km * 0.15))
#print ('o total a pagar é de {:.2f}'.format(p))