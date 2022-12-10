import random
import math

limite_inferior = int(input("Digite o primeiro número do intervalo: "))
limite_superior = int(input("Digite o segundo número do intervalo: "))

x = random.randint(limite_inferior, limite_superior)
print("\n\tVocê tem apenas", round(math.log(limite_superior - limite_inferior + 1, 2))," chances para adivinhar o inteiro!\n")

 
count = 0
 
while count < math.log(limite_superior - limite_inferior + 1, 2):
    count += 1
     
    guess = int(input("Adivinhe o número:- ")) 
     
    
    if x == guess:  
       print("Parabéns, você conseguiu acertar em ", count, " tentativas.")
       
       break
    elif x > guess:
       print("Ahh!!! Você disse um valor pequeno de mais!")
    elif x < guess:
       print("Ah!!! Você disse um valor alto de mais!")
 
if count >= math.log(limite_superior - limite_inferior + 1, 2):
   print("\nO número é: %d"%x)
   print("\tMais sorte na próxima vez!")