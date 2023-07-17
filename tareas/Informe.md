Informe de Tarea

Autor: Efrain Granado

El presente código está compuesto por los siguientes elementos:

1) Librería random para generar números aleatorios
2) La clase Stack que representa una pila simulada con código de Python
3) Dos pilas generadas a través de la clase Stack, una de entrada y otra para mostrar los elementos ordenados de la entrada
4) una entrada numérica para indicar la cantidad de elementos que tendrá el arreglo de entrada
5) el arreglo generado por la cantidad de elementos y números agregados aleatoriamente
a través de un ciclo

El proceso realizado para ordenar una pila es el siguiente:

1) Se obtiene una pila de entrada
2) Se genera un ciclo principal, donde se asigna el último elemento de la pila a una variable auxiliar y dicho elemento se desapila de la pila de entrada. Esto se repite hasta que la Pila de entrada se vacie por completo
3) Dentro del ciclo principal, hay un segundo ciclo interno, donde si la pila que tendrá elementos ordenados está vacía se apila el número guardado como auxiliar a esa pila. Luego, si la pila no está vacía y la variable auxiliar es menor al último elemento de la Pila ordenada, esté ultimo elemento de la pila ordenada se apila nuevamente a la pila de entrada y luego se desapila de la pila ordenada. Si esta condición del ciclo secundario no se cumple, se apila la variabl auxiliar en la Pila ordenada. Esto se repite hasta que el ciclo principal culmine.

El resultado es una Pila ordenada de menor a mayor.

Actualización 16/07/2023: Se modifica el archivo en la sección de los ciclos para ordenar la pila, convirtiendo esa parte en la función my_stack_function
