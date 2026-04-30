def max_product_of_three(array):
    if len(array) < 3:
        return "Error: Array must have at least 3 elements"
    
    
    return find_extremes(array, 0, float('-inf'), float('-inf'), float('-inf'), float('inf'), float('inf'))

def find_extremes(array, index, max1, max2, max3, min1, min2):
    
    if index == len(array):
        return max(max1 * max2 * max3, min1 * min2 * max1)
    
    num = array[index]
    
    
    if num > max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num > max2:
        max3 = max2
        max2 = num
    elif num > max3:
        max3 = num
        
    
    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2:
        min2 = num
        
    
    return find_extremes(array, index + 1, max1, max2, max3, min1, min2)