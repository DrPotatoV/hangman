# Import modules to use
from words import palabras, vidasPics

from colorama import Fore, Back, Style #Importar colorama
import random

# 1. Bienvenida
print(Fore.GREEN + "Bienvenido al juego del Ahorcado")
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

def hangman(): #Mecanica del juego

  word = get_valid_word(palabras) # obtener palabra
  word_letters = set(word) # Separar palabra, ej: S, O , L
  alphabet = set(string.ascii_uppercase) #Convertir a mayus A, B, C, D, E,...
  letras_usadas = set()
  vidas = 7

while len(word_letters) > 0 and vidas > 0:
    print(f"Te quedan {vidas} vidas restantes y ya has usado estas letras: ",' '.join(letras_usadas))

    # what letter you guess, example WORD (- - R D)
    word_list = [letter if letter in letras_usadas else '-' for letter in word]

    print("Current word: ", ' '.join(word_list),"\n")

    user_letter = input('Guess a letter:').upper() # S

    if user_letter in alphabet - letras_usadas: # si "S" esta en "A,B,C,D" - ""
      letras_usadas.add(user_letter) # S
      # print(letras_usadas,'\n',word_letters)

      if user_letter in word_letters: # S es parte de tu palabra
        word_letters.remove(user_letter) # S, O , L le quito la S = O, L
      else:
        vidas = vidas - 1
        print("Esta letra no está en la palabra")

    elif user_letter in letras_usadas:
      print("Ya usaste esta palabra, intenta con otra.")
    else:
      print("Caracter invalido. Usa puras letras.")

  if vidas == 0
    print("Has perdido, la palabra era: ", word)
  else:
    print("Atinaste: ", word,"!!! =)")


hangman()



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