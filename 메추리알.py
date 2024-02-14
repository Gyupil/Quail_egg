class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, running_time, enter_age, star_point):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.running_time = running_time
        self.enter_age = enter_age
        self.star_point = star_point

    def __repr__(self):
        return f'{self.restaurant_name}'


class Menu:
    def __init__(self, name, restaurant, allergic_info):
        self.name = name
        self.restaurants = restaurant
        self.allergic_info = allergic_info

    def __repr__(self):
        return f'{self.name}'


class User:
    def __init__(self, name, allergic_info, age):
        self.name = name
        self.allergic_info = allergic_info
        self.age = age

    def __repr__(self):
        return f'{self.name}'


restaurants = []
restaurant_info = open("restaurant_info.txt", 'r+')
for line in restaurant_info:
    info = line.split(', ')
    restaurant = Restaurant(info[0], info[1], info[2], info[3])
    restaurants.append(restaurant)
restaurant_info.close()

menus = []
menu_info = open("menu_info.txt", 'r+')
for line in menu_info:
    info = line.split()
    menu = Menu(info[0], info[1], info[2])
    menus.append(menu)
menu_info.close()

users = []
user_info = open("user_info.txt", 'r+')
if user_info != "":
    for line in user_info:
        info = line.split()
        user = User(info[0], info[1], info[2])
        users.append(user)
user_info.close()
