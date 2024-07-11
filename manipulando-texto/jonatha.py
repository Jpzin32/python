frase = 'Jp te comeu'

#print (frase)

#print(frase[4])#vai mostrar somente a caracter 4

#print(frase[0:15])#vai selecionar as caracteres do 0 até 15

#print("""colocando
#     3 ("")
#     o 
#     print
#     vai pegar mais de uma
#     linha.
#""")

#print(len(frase))#vai contar as caracteres da frase incluindo os espaços.

#print(len(frase.strip()))#vai contar as caracteres da frase tirando os espaços.

#print(frase.replace('comeu', 'ama')) vai trocar a palavra selecionada.

#print('jp' in frase)#vai mostrar se a palavra selecionada está ou não na variavel.

#print(frase.find('te'))#vai mostrar a posição da palavra na variavel

#print(frase.lower().find('jp'))#preocurar a palavra na variavel em minuscula e mostrar posição dela

#print(frase.split())#vai colocar a frase em uma lista e separar cada palavra


#(LOWER MINUSCULO) (UPPER MAISCULO)


n1 = float(input(('digite um número: ')))
print('esse é o valor do produto com 10% de desconto R$:{:.2f}' .format(n1 * 90/100))