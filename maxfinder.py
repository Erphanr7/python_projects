def row_maximum(data):
    maxfinder = []

    for i in range(len(data)):
        if len(data[i]) > 0:
            maxfinder.append(max(data[i]))
        else:
            maxfinder.append(None)

    return maxfinder

data = [[3,8,2],[],[-5,-1,-4]]
maximum = row_maximum(data)

print (maximum)
