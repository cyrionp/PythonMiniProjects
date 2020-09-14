import random #This module is used to generate random number

def Line(): print("-"*31)

def GenerateMultiplication(digit):
    global question,result
    if digit==1:
        num1=random.randint(1,10)
        num2=random.randint(1,10)
        result=num1*num2
        question=f"{num1} x {num2}"
    elif digit==2:
        num1=random.randint(10,100)
        num2=random.randint(10,100)
        result=num1*num2
        question=f"{num1} x {num2}"
    elif digit==3:
        num1=random.randint(100,1000)
        num2=random.randint(100,1000)
        result=num1*num2
        question=f"{num1} x {num2}"
    elif digit==4:
        num1=random.randint(1000,10000)
        num2=random.randint(1000,10000)
        result=num1*num2
        question=f"{num1} x {num2}"

Line()
print(f"{' '*12}WELCOME")
Line()

while True: #This loop for if user wants to exit
    difficulty=int(input("Which level do you want?\n 1) Easy\n 2) Medium\n 3) Hard\n 4) Very Hard\n OTHERS) Exit\nYour choice: "))
    Line()
    if not difficulty in [1,2,3,4]: break
    GenerateMultiplication(difficulty)
    answer=int(input(f"{question}: "))
    print("Correct!") if answer==result else print(f"Wrong! The answer is {result}")
    Line()
