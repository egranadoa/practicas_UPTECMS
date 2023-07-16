import random

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def top(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)
        
pila1 = Stack()
pila2 = Stack()
array = []
cantidad = int(input("De cuántos números será el arreglo: "))
while cantidad > 0:
    array.append(random.randint(-100, 100))
    cantidad -= 1
print("Arreglo desordenado:", array)

for i in array:
    pila1.push(i)

while pila1.isEmpty() == False:
    aux = pila1.top()
    pila1.pop()
    while pila2.isEmpty() == False and aux < pila2.top():
        pila1.push(pila2.top())
        pila2.pop()
    else:
        pila2.push(aux)

print("Pila ordenada:", pila2.items)
