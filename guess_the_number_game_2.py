print("Imagine number between 0 and 1000!")
input("Press ENTER to continue")

def guess():
    """guess user imagined number in max. 10 steps
    :rtype: str
    """
    min = 0
    max = 1000
    while True:
        guess = int((max - min) / 2 + min)
        print(f"Your number is {guess}")
        user_input = input()
        correct_answers = ["You win", "To big", "To small"]
        if user_input in correct_answers:
            if user_input == "You win":
                print("Hurra! I guess")
                break
            if user_input == "To big":
                max = guess
            if user_input == "To small":
                min = guess
        else:
            print("Wrong answer")

guess()



