def count_signs(values):
    count_pos = 0
    count_zero = 0
    count_neg = 0
    
    for i in range(len(values)):
        if values[i] > 0:
            count_pos += 1 
        elif values[i] == 0:
            count_zero += 1
        else:
            count_neg += 1
            
    return count_zero, count_neg, count_pos
    

values = [3,0,-2,7,-1,0]
count_zero, count_neg, count_pos = count_signs(values)

print(count_pos, count_zero, count_neg)
