import random 
print("welcome in guess the number world")
print("1. Super Easy ")
print("2. Easy ")
print("3. Normal ")
print("4. Hard ")
print("5. Hardest")
   
choice = input("Enter your choice: ").lower()
if choice == 1:
     limit = 10
elif choice == 2:
     limit = 100
elif choice == 3:
     limit = 1000
elif choice == 4:
     limit = 10000
elif choice == 5:
     limit = 100000
else:
     print("invalid choice")
     exit()

user = 0
comp = random.randint(1,limit)
attempt = 0

while user != comp:
     user = int(input(f"Enter a number beetween 1 to {limit}. "))
     attempt = attempt + 1
     if user > comp:
          print("please lower number")
     elif user < comp:
          print("please higher number")
     else:
          print(f"congratulation! you guessed the correct number in {attempt} attempt ")
          break



           
           



