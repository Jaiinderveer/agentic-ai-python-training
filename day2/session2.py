# instagram_user_name is a REFRENCE VARIABLE
instagram_user_name = "Jaiinder" #creational statement | Model
age = 19

# Output Statements | View
print('hashcode of instagram_user_name:',id(instagram_user_name),type(instagram_user_name))
print('hashcode of age:',id(age),type(age))
                # Data in right hand side is known as LITERALS
instagram_user_name = "Yash"
Yash_age = 19

print('hashcode of instagram_user_name:',id(instagram_user_name),type(instagram_user_name))
print('hashcode of age:',id(Yash_age),type(Yash_age))

del Yash_age
del age
print('Yash_age is:', Yash_age)
print('age is:', age)