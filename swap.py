def swap_pairs(values):
    i = 0
    while i < len(values)-1:
        values[i], values[i+1] = values[i+1], values[i]
        i += 2

values =[1,2,3,4,5]
alias = values
swap_pairs(values)

print(values)
print(alias)
