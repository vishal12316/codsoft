import random

print("Select '0' For Rock!"'\n'
      "Select '1' For Paper!"'\n'
      "Select '2' For Scissors!")

i = int(input("Enter your Choice:"))
if i < 0 or i > 2 :
    print("Invalid choice , choose numbers only 0 , 1 and 2 ")
else:
    c = random.randint(0, 2)
    print(f"You chose {['Rock', 'Paper', 'Scissors'][i]}")
    print(f"Computer chose {['Rock', 'Paper', 'Scissors'][c]}")

    if i == c:
        print(f"You Both Choose {['Rock', 'Paper', 'Scissors'][i]}, it's a Tie!")
    elif i == 0 and c == 2:
        print("Rock smashes scissors! You win!!")
    elif i == 1 and c == 0:
        print("Paper covers rock! You win!!")
    elif i == 2 and c == 1:
        print("Scissors cuts paper! You win!!")
    elif i== 0 and c == 1:
        print("Paper covers rock! Computer wins!!")
    elif i == 1 and c == 2:
        print("Scissors cuts paper! Computer wins!!")
    elif i == 2 and c == 0:
        print("Rock smashes scissors! Computer wins!!")
    else:
        print("Invalid choice. Please try again!!")