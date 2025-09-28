import random

subjects =[
    "Amitabh bacchan",
    "Abhishek bacchan",
    "Virat kohli",
    "Salman khan",
    "Akshay Kumar",
    "Shah rukh khan"
]

actions = [
    " was got in slum",
    " is playing a 3 patti front of",
    " has made hit man front of",
    " is not man people told him",
    " is friend of rahul gandi public saw",
    " is like a dog public spoke",
    " is playing with monkeys in"
]

places = [
    "india gate",
    "tajmahal",
    "red fort",
    "cannought place",
    "sarogini market"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    
    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print('\n'+ headline)
    heading = input("\nDo you want to another news (yes/no)").strip().lower()
    if heading == 'no':
        print("it's okay")
        break


print('thanks for using the fake news healines')