# 
"""
Orbis Geoscripting
"""
import random

nombre=input("Hola ¿cómo estás?, vamos a jugar al Ahorcado \npero primero, me gustaría saber tu nombre ¿Cómo te llamas?: ")
print("\nBienvenido, "+nombre,"\nEs hora de jugar")
print(" ")
print("\n¡Comienza a adivinar!")

with open(r'\palabras-master\listado-general.txt', 'r', encoding="utf8") as f:
    palabra = [line.strip() for line in f]

palabras = random.choice(palabra)
tupalabra=" "
vidas= 5

while vidas > 0:
    fallas=0
    
    
    for letra in palabras:
        if letra in tupalabra:
            print(letra,end=" ")
        else:
            print("_",end=" ")
            fallas+=1
            
    if fallas==0:
        print("")
        print("¡¡¡Felicidades!!! \nGanaste :DDDD")
        break
    
    tuletra=input("Introduce tu letra: ")

    tuletra = tuletra.lower()
    tupalabra+=tuletra
    

    if tuletra not in palabras:
        vidas-=1
        print("¡Equivocacion\n!")
        print("Te quedan ",+vidas," vidas")
    if vidas== 0:
        print(f"¡Perdiste!, la palabra era: {palabras}")
else:
    print("\ngracias por participar")
