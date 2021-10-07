import random

destinations = ['Dallas','Austin','Houston','San Antonio']

entertainment = ['Museum','Shopping','Football','Swimming Hole']

restaurants = ['Whataburger',"Torchy's Tacos", "Amy's",'Hopdaddy']

transportation = ['Public Transit','Carshare','Bikeshare','Taxi']

def final_destination(first_index,last_index):
    random_destination = random.randint(first_index, last_index)
    print(destinations[random_destination])
    return(destinations[random_destination])

def final_entertainment(first_index,last_index):
    random_entertainment = random.randint(first_index, last_index)
    print(entertainment[random_entertainment])
    return(entertainment[random_entertainment])

def final_restaurant(first_index,last_index):
    random_restaurant = random.randint(first_index, last_index)
    print(restaurants[random_restaurant])
    return(restaurants[random_restaurant])

def final_transportation(first_index,last_index):
    random_transportation = random.randint(first_index, last_index)
    print(transportation[random_transportation])
    return(transportation[random_transportation])

def opening_message():
    print("Hey friend! Let's generate your daytrip!")
    print("The trip we have planned for you is:")


opening_message()

print("Where you'll be going: ")

final_destination(0,3)

print("What you'll be doing: ")

final_entertainment(0,3)

print("What you'll be eating: ")

final_restaurant(0,3)

print("How you'll be moving: ")

final_transportation(0,3)

user_confirmation = input("Press 1 if you are happy with your trip as is. Press 2 if you would like to change it. ")
if user_confirmation == '1':
    print('Perfect! Have the best trip!')
elif user_confirmation == '2':
    user_option = input('Press 1 to change entire trip. Press 2 to choose which option to change. ')
    if user_option == '1':
        print("Where you'll be going: ")
        final_destination(0,3)
        print("What you'll be doing: ")
        final_entertainment(0,3)
        print("What you'll be eating: ")
        final_restaurant(0,3)
        print("How you'll be moving: ")
        final_transportation(0,3)
    if user_option == '2':
        user_change = input('Which option would you like to change? 1. Destination 2. Entertainment 3. Restaurant 4. Transportation ')
        if user_change == '1':
            final_destination(0,3)
        elif user_change == '2':
            final_entertainment(0,3)
        elif user_change == '3':
            final_restaurant(0,3)
        elif user_change == '4':
            final_transportation(0,3)