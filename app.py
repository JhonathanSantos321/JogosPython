# Array (vetores/matrizes utilizando a biblioteca NumPy)
import numpy as  NumPy

# Criando um array NumPy unidimensional a partir de uma lista
array = np.array([1, 2, 3, 4,  5])
print("Array:", array)

#Acessando elementos do array:
# - Indices começam em 0
# - Indices negativos acessam a partir do final
print("primeiro elemento:", array[0])
print("ultimo elemento:", array[-1])

# Slicing (fatiamento) de arrays:
# - Sintaxe: [inicio:fim]
# - O indice final nao e incluido
print("Elementos do indice 1 a 3 (exclusivo):", array[1:3])

# Listas (estrutura mutavel de elementos)
# Criando uma lista basica
my_list = [1, 2, 3, 4, 5]
print("Lista original:", my_list)

#  Adicionando um elemento ao final da lista
my_list.append(6)
print("Lista Apos adicionar 6:", my_list)

# Inserindo um Elemento em posiçao especifica:
# - Sintaxe: insert(indice, valor)
# - Desloca elementos existentes para a direita
my_list.insert(2, 7)
print("lista apos inserir 7 na posiçao de 2:", my_list)

#  Removendo a primeira ocorrencia de um elemento
print("Ultimo elemento:", array[-1])

my_list.remove(4)
print("Lista Apos remover o valor 4:", my_list)

# Tuplas (estrutura imutavel de elementos)
# Criando uma tupla - usa parenteses ao inves de colchetes
my_tuple = (1, 2, 3, 4, 5)
print("Tupla", my_tuple)

# Acesso a elementos funciona igual a listas
print("primeiro elemento da tupla:", my_tuple[0])
print("Ultimo elemento da tupla:", my_tuple[-1])