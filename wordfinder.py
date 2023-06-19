def word_finder (word, sentences):
    if type(word) == str and type(sentences) == str:
        validation = word in sentences

        if word in sentences:
            return validation
        else:
            return False

    else:
        errorMsg = "Valores Incorrectos"
        return errorMsg

tofind = str(input("Indique la palabra a buscar: "))
phrase = "adios bonitana despues de usted"

print(word_finder(tofind, phrase))
