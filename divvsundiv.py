def count_divisible(values, divisor):
    count_div = 0
    count_undiv = 0
    i = 0
    while i < len(values):
        if values[i]% divisor == 0:
            count_div += 1
        else:
            count_undiv += 1
        i +=1
    return count_div, count_undiv
        
values = [6,7,0,12,-9,10]
divisor = 3
count_div, count_undiv = count_divisible(values, divisor)
count = (count_div, count_undiv)
print (count)
