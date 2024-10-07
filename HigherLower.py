from logo import higher_lower, vs
import random
from game_data import data

item_2 = random.choice(data)

"""function to write a sentence from an item."""
def pick_a_person(person):
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}"

"""global variable score which describes the present score of the game"""
score = 0

continue_game = True

"""print higher lower logo from logo.py file"""
print(higher_lower)


while continue_game:
    """Randomly picking up an item from an dictionary"""
    item_1 = item_2
    # print(item_1)

    item_2 = random.choice(data)

    """checking if two items are same or not"""
    if item_1 == item_2:
        item_2 = random.choice(data)
    # print(item_2)


    print(f"Compare A : {pick_a_person(item_1)}")

    """print vs logo"""
    print(vs)

    print(f"Against B : {pick_a_person(item_2)}")

    """saves the follwers of the persons in a variable called item_1_follower and item_2_follower"""
    a = item_1["follower_count"]
    # print(a)

    b = item_2["follower_count"]
    # print(b)


    """ask the user to guess who has more followers on instagram."""
    guess = input("Who has more followers? Type 'A' or 'B'.").lower()
    print("\n" * 20)
    print(higher_lower)

    if a > b:
        if guess == "a":
            score += 1
            print(f"You're Right! Current score : {score}")
        elif guess == "b":
            print(f"Sorry! that's wrong. Final score : {score}")
            continue_game = False
        else:
            print("you entered an unexpected input. Your game has ended!")
            continue_game = False
    elif a < b:
        if guess == "a":
            print(f"Sorry! that's wrong. Final score : {score}")
            continue_game = False
        elif guess == "b":
            score += 1
            print(f"You're Right! Current score : {score}")
        else:
            print("you entered an unexpected input. Your game has ended!")
            continue_game = False
    else:
        print("wrong")



