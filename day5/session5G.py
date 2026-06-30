'''
BINGO: Flat 100 off, min amount 200
GET500: Flat 500 off, min amount 1000
JUMBO: flat 300 off, min amount 500
'''
amount_in_cart = int(input('Enter Amount: '))
promo_code = input('Enter Promo Code: ').upper()

#task: try the logic with if else ladder

if promo_code == "BINGO":

    if amount_in_cart >= 200:

        discount = amount_in_cart * 0.50

        if discount > 200:
            discount = 200

        print("Promo Code Applied")
        print("Discount: ₹", discount)
        print("Final Amount: ₹", amount_in_cart - discount)

    else:
        print("Minimum purchase should be ₹200")

elif promo_code == "JUMBO":

    if amount_in_cart >= 500:

        discount = amount_in_cart * 0.30

        print("Promo Code Applied")
        print("Discount: ₹", discount)
        print("Final Amount: ₹", amount_in_cart - discount)

    else:
        print("Minimum purchase should be ₹500")

elif promo_code == "GET500":

    if amount_in_cart >= 1000:

        discount = 500

        print("Promo Code Applied")
        print("Discount: ₹", discount)
        print("Final Amount: ₹", amount_in_cart - discount)

    else:
        print("Minimum purchase should be ₹1000")

else:

    print("Invalid Promo Code")