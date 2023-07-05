def contgExtract(sArray):
    a_list = []
    repeateds = []
    extracts = []
    eMatrix = []

    for i in sArray:
        a_list.append(i)

    for i in range(0, len(a_list) -1):
        if a_list[i] == a_list[i+1]:
            repeateds.append(a_list[i])
        elif a_list[i] == a_list[i-1]:
            repeateds.append(a_list[i])
            eMatrix.append(repeateds)
            repeateds = []

    return eMatrix
            
chars = str(input("Indique las letras a enlistar: "))

print("Letras contiguas:", contgExtract(chars))
