
import random

print("Number guessing game") 

def game():
number = random.randint (1,9)
chances = 0
  
print("tebak angka antara 1 sampe 9:")  


while chances < 5: 
 
    guess = int(input()) 
      

    if guess == number: 
          
        print("jago!!") 
        break
          
    elif guess < number: 
        print("kekecilan nebaknya", guess) 
  
          
    else: 
        print("kegedean nebaknya", guess) 
          
    chances += 1
          
          
if not chances < 5: 
    print("salah gan, yg bener", number) 
except: 
