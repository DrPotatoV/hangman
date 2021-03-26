# Import modules to use
'''from words import palabras, vidasPics

from colorama import Fore, Back, Style #Importar colorama
import random

# 1. Bienvenida
print(Fore.GREEN + "Bienvenido al juego del Ahorcado")
print(Fore.RED + "Comenzaras con 6 vidas, mucha suerte!")
print(Style.RESET_ALL)
vidas = 0
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

# Main function, init game
def hangman():

  word = get_valid_word(palabras) # SOL
  word_letters = set(word) # S, O , L
  alphabet = set(string.ascii_uppercase) # A, B, C, D, E,...
  used_letters = set()
  lives = 6

  print("La palabra es: ",word)

  while len(word_letters) > 0 and lives > 0:
    print(f"You have {lives} lives left and you have used these letters: ",' '.join(used_letters))

    # what letter you guess, example WORD (- - R D)
    word_list = [letter if letter in used_letters else '-' for letter in word]

    print("Current word: ", ' '.join(word_list),"\n")

    user_letter = input('Guess a letter:').upper() # S

    if user_letter in alphabet - used_letters: # si "S" esta en "A,B,C,D" - ""
      used_letters.add(user_letter) # S
      # print(used_letters,'\n',word_letters)

      if user_letter in word_letters: # S es parte de tu palabra
        word_letters.remove(user_letter) # S, O , L le quito la S = O, L
      else:
        lives = lives - 1
        print('Letter is not in word')

    elif user_letter in used_letters:
      print("You have already used that character. Please try again.")
    else:
      print("Invalid character. Please try again.")

  if lives == 0:
    print("You died, The word was: ", word)
  else:
    print("You guessed the word: ", word,"!!! =)")
hangman()'''
#-----------------------------------------------------------------------------------------------------------
from words import palabras,vidasPics
from colorama import Fore, Back, Style #Importar colorama
import string
import random
guiones = ""

# 1. Bienvenida
print(Fore.GREEN + "Bienvenido al juego del Ahorcado")
print(Fore.RED + "Comenzaras con 6 vidas, mucha suerte!")
print(Style.RESET_ALL)

# 2. Funcion para obtener palabra
def get_valid_word(palabras):
  word = random.choice(palabras)

  # Escogiendo una buena palabra
  while '-' in word or ' ' in word: # While - or ' '
    word = random.choice(palabras)

  return word.upper()

'''# Imprimir palabra y largo de palabra
my_word = get_valid_word(palabras)
print(my_word + '\n',len(my_word))

#Desplegar guines segun palabra---------------------------------------------------------------------
largpalab = len(my_word) #Guarda el numero de caracteres de la palabra
print(largpalab)
for i in range(largpalab):
    guiones = guiones + "_ "
print(Fore.GREEN + guiones)
print(Style.RESET_ALL)'''

# Main function, init game
def hangman():

  word = get_valid_word(palabras) # SOL
  word_letters = set(word) # S, O , L
  alphabet = set(string.ascii_uppercase) # A, B, C, D, E,...
  used_letters = set()
  lives = 6
  print(vidasPics[lives])

  print("La palabra es: ",word)

  while len(word_letters) > 0 and lives > 0:
    print(f"Te quedan {lives} Vidas y has usado estas letras: ",' '.join(used_letters))
    print(vidasPics[lives])

    # what letter you guess, example WORD (- - R D)
    word_list = [letter if letter in used_letters else '-' for letter in word]

    print("Current word: ", ' '.join(word_list),"\n")

    user_letter = input('Guess a letter:').upper() # S

    if user_letter in alphabet - used_letters: # si "S" esta en "A,B,C,D" - ""
      used_letters.add(user_letter) # S
      # print(used_letters,'\n',word_letters)

      if user_letter in word_letters: # S es parte de tu palabra
        word_letters.remove(user_letter) # S, O , L le quito la S = O, L
      else:
        lives = lives - 1
        print('Letter is not in word')

    elif user_letter in used_letters:
      print("You have already used that character. Please try again.")
    else:
      print("Invalid character. Please try again.")

  if lives == 0:
    print("You died, The word was: ", word)
  else:
    print("You guessed the word: ", word,"!!! =)")


hangman()
#-----------------------------------------------------------------------------------------------------------
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