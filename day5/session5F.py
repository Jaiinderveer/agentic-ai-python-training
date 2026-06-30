promo_codes = {
    'BINGO' : {
        'min_amount': 200,
        'discount': 0.50,
        'max_discount': 200
    },
    'JUMBO' : {
        'min_amount': 500,
        'discount': 0.30,
        'max_discount': 0
    }
}
amount_in_cart = int(input('Enter Amount: '))
promo_code = input('Enter Promo Code: ')

print('~~~~~~~~~~~~~~~~~~~~~')
print('You Entered Amount: ',amount_in_cart)
print('You Entered Promo Code: ',promo_code)
print('~~~~~~~~~~~~~~~~~~~~~')

if promo_code in promo_codes:
    print('Promo Code Valid',promo_code)
    promo_code_rule = promo_codes[promo_code]
    print(promo_code_rule,type(promo_code_rule))
    if amount_in_cart>=promo_code_rule['min_amount']:
        print('Promo code applied successfully')
        
        discount_calculated = promo_code_rule['discount'] * amount_in_cart
        print('Discount Calculated: ₹',discount_calculated)
        
        if discount_calculated> promo_code_rule['max_discount'] and promo_code_rule['max_discount'] != 0:
            amount_to_pay = amount_in_cart - promo_code_rule['max_discount']
            print('amount_to_pay: ₹',amount_to_pay)
        else:
            amount_to_pay = amount_in_cart - discount_calculated
            print('amount_to_pay: ₹',amount_to_pay)
        
    else:
        print('Promo code cannot be applied. Enter items worth', promo_code_rule['min_amount'] - amount_in_cart,'more and try again')
else:
    print('Promo Code Invalid')
    