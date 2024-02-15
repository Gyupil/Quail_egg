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
    def __init__(self, name, allergic_info, selling_restaurant):
        self.name = name
        self.allergic_info = allergic_info
        self.selling_restaurant = selling_restaurant

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
    restaurant = Restaurant(info[0], info[1], info[2], info[3], info[4])
    restaurants.append(restaurant)
restaurant_info.close()

menus = []
menu_info = open("menu_info.txt", 'r+')
for line in menu_info:
    info = line.split()
    menu = Menu(info[0], info[1])
    menus.append(menu)
menu_info.close()

total_info = {}
for menu in menus:
    for restaurant in restaurants:
        if restaurant.restaurant_name == menu.selling_restaurant:
            total_info[menu] = restaurant

users = []
user_info = open("user_info.txt", 'r+')
if user_info != "":
    for line in user_info:
        info = line.split()
        user = User(info[0], info[1], info[2])
        users.append(user)
user_info.close()


def check_allergic(user_list, menu_dict):
    for i in menu_dict.keys():
        for j in user_list:
            if i.allergic_info == j:
                del menu_dict[i]


print("Here are the restaurants:")
