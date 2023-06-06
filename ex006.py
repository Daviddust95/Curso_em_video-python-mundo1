'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

n1 = int (input ('informe um número:'))
dobro = n1 * 2
triplo = n1 * 3
Rq = n1 ** (1/2)
print("O dobro de {} é :{}".format(n1,dobro))
print("O triplo de {} é:{}".format(n1,triplo))
print("A raiz quadrada de {} é: {:.2f}".format(n1,Rq))
