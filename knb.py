import random

print("1- камень, 2- ножницы, 3- бумага")

player = int(input("Введите число от 1 до 3"))
if player == 1:
        print("игрок показал камень")
elif player == 2:
        print("игрок показал ножницы")
elif player == 3:
        print("игрок показал бумагу")

computer = random.randint(1, 3)
if computer == 1:
        print("компьютер  показал камень")
elif player == 2:
        print("компьютер показал ножницы")
elif player == 3:
        print("компьтер показал бумага")

if player == computer:
     print("ничья")
else:
    if player == 1 and computer == 2:
        print("игрок победил!")
    elif player == 2 and computer == 3:
        print("игрок победил!")
    elif player == 3 and computer == 1:
        print("игрок победил!")
    else:
        print("компьютер победил!")