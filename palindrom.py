def palindrom (sentences):
    ns_sentences = ""
    s_inverted = ""

    if type(sentences) == str:
        for chars in sentences:
            if chars == " ":
                continue
            else:
                ns_sentences = ns_sentences + chars

        print("Palabra-Frase sin espacios: ", ns_sentences)
        
        for chars in ns_sentences:
            s_inverted = chars + s_inverted

        print("Palabra-Frase Invertida: ", s_inverted)

        if s_inverted == ns_sentences:
            return True
        else:
            return False

    else:
        errorMsg = "Valores Incorrectos"
        return errorMsg

word1 = str(input("Indique una palabra o frase;\n"
                  "Si es Palíndrome, será True; sino, será False\n"
                  "Palabra-Frase: "))
print(palindrom(word1))
