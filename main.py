print("loading... ")
import time
import replit
time.sleep(0.3)
replit.clear()
print("loading... ⠁")
import os
game = True
time.sleep(0.1)
os.system("clear")
print("loading... ⠉")
computer = 0
tries = 0
time.sleep(0.1)
os.system("clear")
print("loading... ⠙")
max = 0
choice = 0
time.sleep(0.1)
print("loading... ⠹")
import random
import colorama
replit.clear()
print("loading... ⠽")

time.sleep(0.2)
replit.clear()
print("loading... ⠿")
time.sleep(0.3)
replit.clear()
print("-----------------")
time.sleep(0.05)
print(Fore.RED "Hi, Welcome back to up or down!")
time.sleep(0.05)
print()
time.sleep(0.05)
print(
    "HOW TO PLAY: computer will think of a \nrandom number, you need to guess it."
)
time.sleep(0.05)
print()
time.sleep(0.05)
print("github.com/TrashBin7")
time.sleep(0.05)
print("-----------------")
time.sleep(0.05)
print()
print()
time.sleep(0.05)
print("Pick game mode:")
time.sleep(0.05)
print()
time.sleep(0.05)
print("⣿ (1) 1-100")
time.sleep(0.05)
print("⣿ (2) 1-200 [RECOMMENDED]")
time.sleep(0.05)
print("⣿ (3) 1-500")
time.sleep(0.05)
print("⣿ (4) Custom")
time.sleep(0.05)
print()
time.sleep(0.05)
print("version 1.1")
time.sleep(0.05)

choice = input("")

if choice == "1":
    max = 100

elif choice == "2":
    max = 200

elif choice == "3":
    max = 500
  
elif choice == "4":
    print()
    print()
    max = input("1-")
  
else:
    print("you need to pick between 1-4!")
    time.sleep(0.3)
    print("picking 2...")
    max = 200
    time.sleep(2.5)

os.system('cls' if os.name == 'nt' else 'clear')

print(f"picking a random number between 1-{max}")
computer = random.randint(1, int(max))
time.sleep(0.50)
print("done!")
time.sleep(0.50)
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')
print("(!) Game Started.")
time.sleep(0.1)
print()
time.sleep(0.1)
print("(now type a number.)")
time.sleep(0.1)
while game == True:
 tries = tries + 1
 guess = input("YOU: ")
 guess = int(guess)
 if guess == computer:
   print()
   print("---------------")
   print(f"YOU WON! \nthis was your {tries}th guess.\n \nmade by github.com/TrashBin7")
   print("---------------")
   game = False
   
 elif guess <= computer:
   print("COMPUTER: higher.")

 elif guess >= computer:
   print("COMPUTER: lower.")

   
   