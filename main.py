#HELENA KUCHINSKI FERREIRA
#Você deverá criar uma lista com, no mínimo, 200.000 itens armazenados. Estes itens devem sernúmeros inteiros randomicamente gerados (use o twister de Mersenne para gerar os inteiros), em umrange de 1 a 1.000.000. Seu objetivo será medir o tempo para criar a lista, o tempo para reverter estalista, o tempo necessário para encontrar o item que está no meio da lista e o tempo necessário paraapagar todos os itens da lista, liberando a memória.

import time
import random

class NoLista:
  def __init__(self, dado):
    self.dado = dado
    self.proximo = None

  def __repr__(self):
    return '%s  %s' % (self.dado, self.proximo)

class ListaEncadeada:
  def __init__(self):
    self.head = None

  def __repr__(self):
    return "[" + str(self.head) + "]"

  def insere(lista, novoDado):
    novoNo = NoLista(novoDado)
    novoNo.proximo = lista.head
    lista.head = novoNo

  def reverse(self):
    anterior = None
    atual = self.head
    while(atual is not None):
      proximo = atual.proximo
      atual.proximo = anterior
      anterior = atual
      atual = proximo
    self.head = anterior

  def meio(self):
    pointUltimo= self.head
    pointPrimeiro = self.head
    while pointPrimeiro and pointPrimeiro.proximo:
      pointUltimo = pointUltimo.proximo
      pointPrimeiro = pointPrimeiro.proximo.proximo
    return pointUltimo.dado

  def remove(self):
    atual = self.head
    while atual:
      proximodAtual = atual.proximo
      del atual.dado
      atual = proximodAtual 
   

x = (random.randint(1,1000000) for i in range(200000))

lista = ListaEncadeada()

tPInicio1 = time.process_time() 

for i in x:
  lista.insere(i)
  
tPFinal1 = time.process_time() 

print(f'Preenchendo lista: {round((tPFinal1 - tPInicio1),3)} s')
'-----------------------------------------------------'
#Lista Reversa
tPInicio2 = time.process_time() 

lista.reverse()

tPFinal2 = time.process_time() 

print(f'Revertendo lista: {round((tPFinal2 - tPInicio2),3)} s')
'-----------------------------------------------------'
#Achando meio
tPInicio3 = time.process_time() 

lista.meio()

tPFinal3 = time.process_time() 

print(f'Encontrando elemento do meio: {round((tPFinal3 - tPInicio3),3)} s')
print(f'O elemento do meio da lista é: {lista.meio()}')
'-----------------------------------------------------'
#Apagando lista
tPInicio4 = time.process_time() 

lista.remove()
  
tPFinal4 = time.process_time()

print(f'Apagando todos os itens da lista: {round((tPFinal4 - tPInicio4),3)} s')