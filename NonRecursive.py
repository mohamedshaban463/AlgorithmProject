def max_product_of_three(A):
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')

    min1 = float('inf')
    min2 = float('inf')

    for x in A:

        
        if x > max1:
            max3 = max2
            max2 = max1
            max1 = x
        elif x > max2:
            max3 = max2
            max2 = x
        elif x > max3:
            max3 = x

        
        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x

    option1 = max1 * max2 * max3
    option2 = max1 * min1 * min2

    return max(option1, option2)