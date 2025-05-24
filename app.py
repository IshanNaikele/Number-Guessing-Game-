import random


print("**************************************************************************")
print("Welcome to Number Guessing Game ")
print("**************************************************************************")

progNumber=random.randint(1,100)

exit=True
attempts=0
while True:
    attempts=0
    progNumber=random.randint(1,100)
    while True :
        try :
           num=int(input("Enter a Number :"))
           if num<1 or num>100 :
               print("Enter number between 0 to 101")
               continue
        except :
           print("Enter Numeric Value .")
           continue
        attempts+=1;
        if num>progNumber:
           print("Your Number is too High .Try a little lower")
        elif num<progNumber :
           print("Your Number is too low .Try a little higher")
        else:
           print(f"Congrats!!!You Guessed the right number in {attempts} attempt.")
           break
           
    # Ask if they want to play again
    choice = input("Do you want to play again? (Y/N): ").strip().upper()
    if choice != 'Y':
        print("Thanks for playing! Goodbye!")
        break  # Exit outer loop

    