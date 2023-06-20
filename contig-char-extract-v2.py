def contgExtract(sArray):
    repeateds = []
    extracts = []
    eMatrix = []

    for i in range(0, len(sArray) -1):
        if sArray[i] == sArray[i+1]:
            repeateds.append(sArray[i])
        elif sArray[i] == sArray[i-1]:
            repeateds.append(sArray[i])
            eMatrix.append(repeateds)
            repeateds = []

    print(eMatrix)
            

lista1 = ["a", "a", "c", "c", "s", "x", "x", "x", "x", "a"]
contgExtract(lista1)
