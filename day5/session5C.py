# Bitwise Operators &, |
number1 = 8                        # 1 0 0 0
number2 = 4                        # 0 1 0 0
result1 = number1 & number2         # 0 0 0 0
result2 = number1 | number2         # 1 1 0 0
result3 = number1 ^ number2         # 1 1 0 0

print('Result1: ',result1)
print('Result2: ',result2)
print('Result3: ',result3)

# Shift Operators >>. <<

number3 = 8                         # 0 0 0 0 1 0 0 0 -> 8
number4 = 2                         # 0 0 0 0 0 0 1 0 -> 8>>2 -> 2
result4 = number3>>number4 # 8>>2
# 0 0 0 0 1 0 0 0  << 2
# 0 0 1 0 0 0 0 0
result5 = number3<<number4 # 8<<2
print('result4:',result4) # 2
print('result5:',result5) # 32

data = 12
key = 2
send_data_to_fionna = data >> key # 12/2power3
print('send_data_to_fionna:',send_data_to_fionna)

data_recieved_by_fionna = send_data_to_fionna<<key
print('data_recieved_by_fionna:',data_recieved_by_fionna)
