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

user_confirmation = input("Are you happy with your daytrip? Y or N ")
    if user_confirmation.upper == 'y':
    print('Perfect! Have the best trip!')
    elif user_confirmation.upper == 'n':
    user_change = input('Which option would you like to change? 1. Destination 2. Entertainment 3. Restaurant 4. Transportation')
        if user_change == '1':
            print(final_destination(0,3))
        elif user_change == '2':
            print(final_entertainment(0,3))
        elif user_change == '3':
            print(final_restaurant(0,3))
        elif user_change == '4':
            print(final_transportation(0,3))

# This is where all of your code lives


# """
# 1. Create lists with all of the options for your trip (destinations, entertainment, restaurants, transportation)
# 2. Randomly select an option from each
# 3. Display those options to the user
# 4. Ask the user if they are satisfied with the trip
# 5. If yes, then print the trip again as the confirmed trip
# 6. If no, generate a new set of trip features, and start over
# """