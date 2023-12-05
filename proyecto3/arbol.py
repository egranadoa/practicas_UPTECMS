import random

class Frutal:
    def __init__(self, name, h, fruit):
        self.name = name
        self.h = h
        self.fruit = fruit
        
    def getName(self):
        return self.name
    
    def getH(self):
        return self.h
    
    def getFruit(self):
        return self.fruit
    
    def setName(self, name):
        self.name = name
        return self.name
    
    def setH(self, h):
        self.h = h
        return self.h
    
    def setFruit(self, fruit):
        self.fruit = fruit
        return self.fruit
        
    def crecer(self):
        old_h = self.h
        self.setH(self.h + 1)
        print(self.name, 'pasó de', old_h, 'metros a', self.h, 'metros')
        
    def darFruto(self):
        print(self.name, 'dió un(a)', self.fruit)
        
    def cortar(self):
        print(self.name, 'cortado')
        del self
        
         
class Citrico(Frutal):
    def __init__(self, name, h, fruit, color):
        super().__init__(name, h, fruit)
        self.color = color
        
    def darFruto(self):
        print(self.name, 'dió un(a)', self.fruit, 'de color', self.color)
        

def genTrees(n):
    
    names = ["manzano", "peral", "naranjo", "limonero", "mango"]
    fruits = ["manzana", "pera", "naranja", "limón", "mango"]
    colors = ["rojo", "verde", "naranja", "amarillo"]
    trees = []

    for i in range(n):
        name = names[random.randint(0, len(names) - 1)]
        h = random.randint(1, 100)
        fruit = fruits[random.randint(0, len(fruits) - 1)]
        color = colors[random.randint(0, len(colors) - 1)]

        if name == "naranjo" or name == "limonero":
            arbol = Citrico(name, h, fruit, color)
            trees.append(arbol)
        else:
            arbol = Frutal(name, h, fruit,)
            trees.append(arbol)

    return trees  
        
        
arboles = genTrees(3)
print('Datos de arboles generados:')
for tree in arboles:
    if isinstance(tree, Citrico):
        print(f'''Nombre: {tree.name}
Altura: {tree.h}
Fruto que da: {tree.fruit}
Color de la fruta: {tree.color}
''')
    else:
        print(f'''Nombre: {tree.name}
Altura: {tree.h}
Fruto que da: {tree.fruit}
''')
   
