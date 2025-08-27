#esercizi in python
import os
def pulisci_terminale():
    os.system('cls' if os.name == 'nt' else 'clear')
pulisci_terminale()
print("questa è la calcolatrice di Loris")
num1 = float(input("inserisci il primo numero: "))
num2 = float(input("inserisci il secondo numero: "))
operatore = input("inserisci l'operatore (+, -, *, /): ")
if operatore == "+":
    risultato = num1 + num2
    print("Il risultato è:", risultato) 
elif operatore == "-":
    risultato = num1 - num2
    print("Il risultato è:", risultato)
elif operatore == "*":
    risultato = num1 * num2
    print("Il risultato è:", risultato)
elif operatore == "/":
    risultato = num1 / num2

  
