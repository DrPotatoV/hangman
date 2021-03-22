# Import modules to use
from words import palabras

from colorama import Fore, Back, Style #Importar colorama
import random

# 1. Bienvenida
print(Fore.GREEN + "Welcome to the game hangman in Python")
print(Fore.RED + "Comenzaras con 6 vidas, mucha suerte!")
print(Style.RESET_ALL)
vidas = 6
guiones = ""


# 2. Funcion para obtener palabra
def get_valid_word(palabras):
  word = random.choice(palabras)

  # Escogiendo una buena palabra
  while '-' in word or ' ' in word: # While - or ' '
    word = random.choice(palabras)

  return word

# Imprimir palabra y largo de palabra
my_word = get_valid_word(palabras)
print(my_word + '\n',len(my_word))

#Desplegar guines segun palabra
largpalab = len(my_word) #Guarda el numero de caracteres de la palabra
print(largpalab)
for i in range(largpalab):
    guiones = guiones + "_ "
print(Fore.GREEN + guiones)
print(Style.RESET_ALL)




#Juega------------------------------------------------------------------------------------------------------
#vidasrest = vidas
#do{
#nombre = input("Introduzca una letra")
#Atinó la letra

#No atinó la letra
#vidasrest = vidasrest - 1
#}
#while(vidas >= 1) #Detener al finalizar las vidas
#print("Mejor suerte la proxima")



# Una función que despliegue los guiones
# dependiendo el tamaño de la palabra
# Ejemplo:
# A N O N Y M O U S
# _ _ _ _ _ _ _ _ _