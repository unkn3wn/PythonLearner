# we use import to import a certain library
    # we import all the modules inside random
import random
number = random.randint(1,10)

print(number)


# randint chooses a something random for example 
# here we have 1 and 10 as ranges
number = random.randint(1,10)
print(number)



# here we have a list
cards = ["jack", "queen", "king"]
# we use random.shuffle to mix the order of the list 
random.shuffle(cards)
# for every card in cards 
for card in cards:
    # we print the shuffled card
    print(card)