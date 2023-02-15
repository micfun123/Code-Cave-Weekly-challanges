layer1 = ["1","2","3"]
layer2 = ["4","5","6"]
layer3= ["7","8","9"]
layer4 = ["","0"]

code = str(input("Enter your code: "))
possible = []

#each letter in the code
for i in code:
    #each layer
    for j in layer1:
        if i == j:
            x = layer1.index(i)
            possible.append(layer1[x])

            #get left and right

            try:
                possible.append(layer1[x-1])
            except:
                pass
            try:
                possible.append(layer1[x+1])
            except:
                pass

            #get later down

            possible.append(layer2[x])

    for j in layer2:
        if i == j:
            x = layer2.index(i)
            possible.append(layer2[x])

            #get left and right

            try:
                possible.append(layer2[x-1])
            except:
                pass
            try:
                possible.append(layer2[x+1])
            except:
                pass

            #get later down

            possible.append(layer3[x])
            possible.append(layer1[x])
            
    for j in layer3:
        if i == j:
            x = layer3.index(i)
            possible.append(layer3[x])

            try:
                possible.append(layer3[x-1])
            except:
                pass
            try:
                possible.append(layer3[x+1])
            except:
                pass
            possible.append(layer2[x])
            try:
                possible.append(layer4[x])
            except:
                pass



           

            

    for j in layer4:
        if i == j:
            x = layer4.index(i)
            possible.append(layer3[x])
            possible.append(layer4[x])

    possible = list(set(possible))
print(possible)