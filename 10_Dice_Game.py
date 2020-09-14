#Shuffle two dices until they both equal 6
#Calculate how many step is done

from random import randint

global dice1,dice2,step
step=0

while True:
    dice1=randint(1,7)
    dice2=randint(1,7)
    print(dice1,dice2)
    step+=1

    if dice1==6 and dice2==6: break

print(f"{step} step passed to reach 6-6") if step<2  else print(f"{step} steps passed to reach 6-6")
