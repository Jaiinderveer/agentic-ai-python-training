class Restaurant:
    pass

class Menu:
    pass

class Dish:
    pass

# Create Object in Memory
# Object Construction Statement

dish1 = Dish()
dish1.name = 'Noodles'
dish1.price = 300
dish1.category = 'Chinese Veg'
dish1.rating = 4.5

dish2 = Dish()
dish2.name = 'Burger'
dish2.price = 100
dish2.category = 'Veg'
dish2.rating = 3.5

dish3 = Dish()
dish3.name = 'Pizza'
dish3.price = 400
dish3.category = 'Italian Veg'
dish3.rating = 4.5

dishes = [dish1, dish2, dish3]

menu = Menu()
menu.name = 'Johns Special'
menu.type = 'vegetarian'
menu.dishes = dishes # 1 to many mapping

restaurant = Restaurant()
restaurant.name = 'Johns Cafe'
restaurant.phone = '+91 99999 11111'
restaurant.email = 'info@johnscafe.com' 
restaurant.address = 'redwood Shores'
restaurant.operating_hours = '10:00 to 23:00'
restaurant.rating = 4.5 
restaurant.price_per_person = 500
restaurant.menu = menu # 1 to 1 mapping

# update attribute in object
restaurant.price_per_person = 400
# delete attributes from object
del restaurant.price_per_person

restaurant.delivery_timings = '18:00 to 20:00'

print('restaurant:', restaurant)
print('menu:', menu)

print('dish1:', dish1)
print('dish2:', dish2)
print('dish3:', dish3)

print('data in restaurant:', vars(restaurant))
print('data in menu:', vars(menu))
print('data in dish1:', vars(dish1))
print('data in dish2:', vars(dish2))
print('data in dish3:', vars(dish3))