checkout={
    'value':1000,
    'coupons': {
        'restaurant coupons': {
            '1': {
            'name': 'Flat ₹100 Off',
            'discount':  '₹100'
        }
        },
        'Payment Coupons':{
             '2': {
            'name': 'Flat 5% Off',
            'condition': 'Upto ₹30',
            'source_of_payment': 'BHIM Payments App',
            'discount': '5% * value'
        },
        '3': {
            'name': 'Flat 10% Off',
            'condition': 'Upto ₹100',
            'source_of_payment': 'Utkarsh Small Finance Bank Debit Card',
            'discount': '10% * value'
        }
        }
       
    }
}