import random, destinations
from typing import List

dallas_entertainment = ['Dallas Museum of Art','Perot Museum of Nature and Science','Dealey Plaza','Dallas Arboretum & Botanical Garden',
'Meadows Museum','Deep Ellum','Dallas Zoo','Dallas World Aquarium','Fair Park','Hall of State','Crow Museum of Asian Art',
'Dallas Holocaust and Human Rights Museum','Epic Waters Indoor Waterpark','Dallas Farmers Market','Highland Park Village',
'Winspear Opera House','Bishop Arts District','The Sixth Floor Museum at Dealey Plaza']

austin_entertainment = ['Congress Bridge Bats','WonderSpaces','Texas State Capitol Building','Town Lake','Barton Springs Pool',
'6th Street','South Congress Avenue','the Domain','McKinney Falls State Park','Museum of the Weird','Zilker Park',
'Veloway and Wildflower Center','Circuit of the Americas','Austin Public Library','ACL',"Antone's Nightclub"]

houston_entertainment = ['Museum of Natural Science','Space Center Houston','Houston Zoo','Twilight Epiphany Skyspace',
'Discovery Green',"The Children's Museum of Houston",'Downtown Aquarium','19th Street in the Heights','Revival Market',
"Pete's Dueling Piano Bar",'Museum of Fine Arts','Whiskey River','Cockrell Butterfly Center','1940 Air Terminal Museum',
'The Galleria','Contemporary Arts Museum',"Art Car Museum"]

san_antonio_entertainment = ['The Alamo','Texas Wine Trail','River Walk','Menger Bar','San Antonio Botanical Garden',
'San Antonio Missions Natoinal Historic Park','Natural Brdige Wildlife Ranch','Majestic Theatre','Natural Bridge Caverns',
'Ghost Tour','Rodeo','Buckhorn Saloon and Texas Ranger Museum','San Antonio Market Square','San Antonio Fire Museum',
'San Antonio Museum of Art','Tower of the Americas']


# def thing_to_do(destination, city_list):
#     destination = destinations.final_destination(0,3)
#     city_list = dallas_entertainment or austin_entertainment or houston_entertainment or san_antonio_entertainment
#     thing_to_do = random.randint(city_list)
#     for thing_to_do in city_list:
#         if thing_to_do == destination:

def thing_to_do(destination):
    
