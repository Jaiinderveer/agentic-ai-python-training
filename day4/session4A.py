product = {
    'code':101,
    'name':'Ultraboost',
    'brand':'Adidas',
    'price': 8000,
    'category':'shoes'
}

print(product,id(product),type(product))
print(product['code'],id(product['code']),type(product['code']))
print(product['category'],id(product['category']),type(product['category']))
print(product['brand'],id(product['brand']),type(product['brand']))

shoe_name = 'Adidas'
print(shoe_name,id(shoe_name),type(shoe_name))

product['price'] = 7000

for key in product:
    print(key,product[key])