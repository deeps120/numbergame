import random 
number = random.randint(1,9)
guess = input("guess the number ")
if(guess == number):
    print("you are correct!")
elif(guess != number):
    print("wrong guess!")
    print("the answer was:", number)
