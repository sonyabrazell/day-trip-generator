import random

destinations = ['Dallas','Austin','Houston','San Antonio']


# def final_destination(random_destination):
#     random_destination = random.randint(0,3)
#     print(random_destination)
#     print(destinations[random_destination])

def final_destination(first_index,last_index):
    random_destination = random.randint(first_index, last_index)
    # print(random_destination)
    print(destinations[random_destination])
    return(destinations[random_destination])

final_destination(0,3)