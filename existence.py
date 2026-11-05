def first_positions(data, target):
    exist = []
    i = 0
    while i < len(data):
        j = 0
        position = -1
        
        while j < len(data[i]):
            if data[i][j]== target:
               position = j
               break
            j += 1
        exist.append(position)
        i += 1
    return exist


data = [[4,2,4],[],[7,2],[1,5]]
target = 2

exist = first_positions (data, target)

print (exist)
