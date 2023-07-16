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

def my_stack_function(arr, s1, s2):
    for i in arr:
        s1.push(i)
    
    while s1.isEmpty() == False:
        aux = s1.top()
        s1.pop()
        while s2.isEmpty() == False and aux < s2.top():
            s1.push(s2.top())
            s2.pop()
        else:
            s2.push(aux)

    return s2.items
    
print("Pila ordenada:", my_stack_function(array, pila1, pila2))
