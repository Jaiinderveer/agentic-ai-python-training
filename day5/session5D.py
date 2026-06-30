data = 11       # 0 0 0 0 1 0 1 1
result1 = 11>>3  # 0 0 0 0 0 0 0 1
print('result1:', result1)
"""
11: 0 0 0 0 1 0 1 1
-11: 1 1 1 1 0 1 0 0
                  +1
     1 1 1 1 0 1 0 1
     
-11>>3 

        1 1 1 1 0 1 0 1>>3
        1 1 1 1 1 1 1 0
        0 0 0 0 0 0 0 1
                    + 1
        0 0 0 0 0 0 1 0 -> -2
        
13: 0 0 0 0 1 1 0 1
-13: 1 1 1 1 0 0 1 0
                + 1
    1 1 1 1 0 0 1 1

-13>>2
    1 1 1 1 1 1 0 0
    0 0 0 0 0 0 1 1
    0 0 0 0 0 1 0 0 -> -4
"""
data = -13
result2 = data>>2
print('result2:', result2)

# Assignment -> explore below
#AES, SHA-256 etc are the security algorithms
# which uses shifts and bitwise operations