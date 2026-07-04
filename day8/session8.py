"""
    OOPS - Object Oriented Programming Structure

    2 concepts:
    Object
    Class

    Principle of OOPS:
    1. Think of an Object
    2. Draw/Represent/Textual Represent the Object
    3. From the drawing/representation create a Real Object

    Real World
    Object -> Anything in existence eg: mango, AC, fan, human
    Class -> Drawing/Representation of Object (Architectural Drawing/Blueprint)
             Textual Representation
    
    Computer Science World
    Object -> Storage Container (Homogeneous/Hetrogeneous)
    Class -> Textual Representation of Object, how it will be in memory i.e. the container in memory

"""

"""

    Create a food delivery app, where customer accesses a menu and places an order
    the order can be vissualized on some admin panel or through email
    and inhouse delivery person will deliver the order

    Identify the Objects
    Visualize the Objects
    Relate the Objects
    Code the Objects (Textually Define)
    Create the real objects in memory

    >> Job Role: Forward Deployed Engineers (FDE)

    Object: 
    Resturant 
    
    Attributes: 
    name, phone, email, address, operating_hours, rating, price_per_person, menu

    Menu
    name, type, dishes[]

    Dish
    name, price, category, rating

    User
    name, phone, email, address[], gender, profile_image

    Address
    address_line, city, state, pincode, tag

    DeliveryAgent
    name, phone, email, driving_licence, vehicle, work_hours

    Vehicle
    registration_number, brand, model, year_of_registration, color

    Order
    id, amount, dishes, ?, ? date, time



    Relationship Mapping for Objects
    1 to 1, 1 to *, * to *

    1 Restaurant has 1 Menu
    1 Menu has many Dishes

    SaaS -> * Restaurant has * menu

"""
class Restaurant:
    pass

class Menu:
    pass

class Dish:
    pass

# Create Object in Memory
# Object Construction Statement
restaurant = Restaurant()

menu = Menu()

dish1 = Dish()
dish2 = Dish()
dish3 = Dish()

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