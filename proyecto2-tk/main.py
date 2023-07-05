from tkinter import *

def w1():
    def palindrom ():
        sentences = str(in_e_w.get())
        ns_sentences = ""
        s_inverted = ""

        for chars in sentences:
            if chars == " ":
                continue
            else:
                ns_sentences = ns_sentences + chars

        for chars in ns_sentences:
            s_inverted = chars + s_inverted
        
        if sentences == "":
            o_l_w.config(text="Entrada Vacía")
        else:
            if s_inverted == ns_sentences:
                o_l_w.config(text="Verdadero")
            else:
                o_l_w.config(text="Falso")

    def reset_1():
        in_e_w.delete(0, END)
        o_l_w.config(text="...Esperando Entrada...")

    
    w_palindrom = Toplevel()
    w_palindrom.title("Palindrome")
    
    mf_w = Frame(w_palindrom)
    mf_w.pack()

    in_f_w = LabelFrame(mf_w, text="Entrada")
    in_f_w.grid(padx=10, pady=10, row=0, column=0)
    in_l_w = Label(in_f_w, text="Escriba aqui:")
    in_l_w.grid(padx=5, pady=5, row=0, column=0)
    in_e_w = Entry(in_f_w, width=40)
    in_e_w.grid(padx=5, pady=5, row=0, column=1)

    o_f_w = LabelFrame(mf_w, text="Resultado")
    o_f_w.grid(padx=5, pady=5, row=1, column=0)
    o_l_w = Label(o_f_w, text="...Esperando Entrada...")
    o_l_w.grid(padx=5, pady=5, row=0, column=0)

    b1_w = Button(mf_w, text="Validar", command=palindrom)
    b1_w.grid(padx=5, pady=5, row=2, column=0)
    b2_w = Button(mf_w, text="Reiniciar", command=reset_1)
    b2_w.grid(padx=5, pady=5, row=3, column=0)

def w2():
    def word_finder ():
        sentences = str(in_e1_w.get())
        word = str(in_e2_w.get())
        ns_sentences = ""

        for chars in sentences:
            if chars == " ":
                continue
            else:
                ns_sentences = ns_sentences + chars
        if sentences == "" and word == "":
            o_l_w.config(text="Entradas Vacías")
        elif sentences == "":
            o_l_w.config(text="Frase Vacía")
        elif word == "":
            o_l_w.config(text="Palabra Vacía")
        else:
            if word in ns_sentences:
                o_l_w.config(text="Verdadero")
            else:
                o_l_w.config(text="Falso")

    def reset_2():
        in_e1_w.delete(0, END)
        in_e2_w.delete(0, END)
        o_l_w.config(text="...Esperando Entrada...")
    
    w_wordfinder = Toplevel()
    w_wordfinder.title("Encuentra-Palabras")

    mf_w = Frame(w_wordfinder)
    mf_w.pack()

    in_f_w = LabelFrame(mf_w, text="Entradas")
    in_f_w.grid(padx=10, pady=10, row=0, column=0)
    in_l1_w = Label(in_f_w, text="Frase:")
    in_l1_w.grid(padx=5, pady=5, row=0, column=0)
    in_e1_w = Entry(in_f_w, width=40)
    in_e1_w.grid(padx=5, pady=5, row=0, column=1)
    in_l2_w = Label(in_f_w, text="Palabra a buscar:")
    in_l2_w.grid(padx=5, pady=5, row=1, column=0)
    in_e2_w = Entry(in_f_w, width=40)
    in_e2_w.grid(padx=5, pady=5, row=1, column=1)

    o_f_w = LabelFrame(mf_w, text="Resultado")
    o_f_w.grid(padx=5, pady=5, row=1, column=0)
    o_l_w = Label(o_f_w, text="...Esperando Entrada...")
    o_l_w.grid(padx=5, pady=5, row=0, column=0)

    b1_w = Button(mf_w, text="Validar", command=word_finder)
    b1_w.grid(padx=5, pady=5, row=2, column=0)
    b2_w = Button(mf_w, text="Reiniciar", command=reset_2)
    b2_w.grid(padx=5, pady=5, row=3, column=0)
    
def w3():
    def contgExtract():
        sArray = str(in_e_w.get())
        a_list = []
        repeateds = []
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
        
        if sArray == "":
            o_l_w.config(text="Entrada Vacía")
        else:
            o_l_w.config(text=f"Letras contiguas: {eMatrix}")

        return eMatrix
    
    def reset_1():
        in_e_w.delete(0, END)
        o_l_w.config(text="...Esperando Entrada...")

    w_contig = Toplevel()
    w_contig.title("Letras Contiguas")
    
    mf_w = Frame(w_contig)
    mf_w.pack()

    in_f_w = LabelFrame(mf_w, text="Entrada")
    in_f_w.grid(padx=10, pady=10, row=0, column=0)
    in_l_w = Label(in_f_w, text="Escriba aqui:")
    in_l_w.grid(padx=5, pady=5, row=0, column=0)
    in_e_w = Entry(in_f_w, width=40)
    in_e_w.grid(padx=5, pady=5, row=0, column=1)

    o_f_w = LabelFrame(mf_w, text="Resultado")
    o_f_w.grid(padx=5, pady=5, row=1, column=0)
    o_l_w = Label(o_f_w, text="...Esperando Entrada...")
    o_l_w.grid(padx=5, pady=5, row=0, column=0)

    b1_w = Button(mf_w, text="Validar", command=contgExtract)
    b1_w.grid(padx=5, pady=5, row=2, column=0)
    b2_w = Button(mf_w, text="Reiniciar", command=reset_1)
    b2_w.grid(padx=5, pady=5, row=3, column=0)    

def w4():
    def charseed():
        a = str(in_e1_w.get())
        b = str(in_e2_w.get())
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

        for i in svalues:
            sums = sums + i
            prodc = prodc * i

        seed = sums + prodc
        
        if a == "" and b == "":
            o_l_w.config(text="Entradas Vacías")
        elif a == "":
            o_l_w.config(text="Caracteres Vacío")
        elif b == "":
            o_l_w.config(text="Valores Vacío")
        else:
            o_l_w.config(text=f"Semilla: {seed}")

        return seed
    
    def reset_2():
        in_e1_w.delete(0, END)
        in_e2_w.delete(0, END)
        o_l_w.config(text="...Esperando Entrada...")
    
    w_seed = Toplevel()
    w_seed.title("Encuentra-Palabras")

    mf_w = Frame(w_seed)
    mf_w.pack()

    in_f_w = LabelFrame(mf_w, text="Entradas")
    in_f_w.grid(padx=10, pady=10, row=0, column=0)
    in_l1_w = Label(in_f_w, text="Caracteres:")
    in_l1_w.grid(padx=5, pady=5, row=0, column=0)
    in_e1_w = Entry(in_f_w, width=40)
    in_e1_w.grid(padx=5, pady=5, row=0, column=1)
    in_l2_w = Label(in_f_w, text="Valores para Semilla:")
    in_l2_w.grid(padx=5, pady=5, row=1, column=0)
    in_e2_w = Entry(in_f_w, width=40)
    in_e2_w.grid(padx=5, pady=5, row=1, column=1)

    o_f_w = LabelFrame(mf_w, text="Resultado")
    o_f_w.grid(padx=5, pady=5, row=1, column=0)
    o_l_w = Label(o_f_w, text="...Esperando Entrada...")
    o_l_w.grid(padx=5, pady=5, row=0, column=0)

    b1_w = Button(mf_w, text="Validar", command=charseed)
    b1_w.grid(padx=5, pady=5, row=2, column=0)
    b2_w = Button(mf_w, text="Reiniciar", command=reset_2)
    b2_w.grid(padx=5, pady=5, row=3, column=0)   

root = Tk()
root.title("Proyecto 2 Programacion")
root.geometry("320x280")

mf = Frame(root)
mf.pack()

in_l = LabelFrame(mf, text="Menu Principal")
in_l.grid(padx=10, pady=10, row=0, column=0)

b1 = Button(in_l, text="Palindrome", command=w1).grid(padx=15, pady=15, row=0, column=0)
b2 = Button(in_l, text="Encontrar Palabras", command=w2).grid(padx=15, pady=15, row=1, column=0)
b3 = Button(in_l, text="Letras Contiguas", command=w3).grid(padx=15, pady=15, row=2, column=0)
b4 = Button(in_l, text="Gen. de Semillas", command=w4).grid(padx=15, pady=15, row=3, column=0)

mainloop()
