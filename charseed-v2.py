def charseed(a, b):
    s_chars = []
    s_gen = []
    svalues = []
    sums = 0
    prodc = 1

    for i in b:
        s_gen.append(i)
    for i in a:
        s_chars.append(i)
    
    for i in range(0, len(s_gen)):
        for j in range(0, len(s_chars)):
            if s_gen[i] == s_chars[j]:
                svalues.append(i)
    print("Valores para semilla:", svalues)
    
    for i in svalues:
        sums = sums + i
        prodc = prodc * i

    seed = sums + prodc

    return seed
        

array1 = str(input("Indique las letras a evaluar: "))
array2 = str(input("Indique las letras generadoras: "))

print("Semilla generada:", charseed(array1, array2))
