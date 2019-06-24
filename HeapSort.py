#Ruben Sanchez A01021759
#Cristopher Cejudo A01025468

#Función principal
def heapSort(numbers):
    #Ciclo para hacer la función de heapify con cada
    #nodo padre existente en la lista de números
    for i in range(int((len(numbers)/2)-1), -1, -1):
        heapify(numbers, i)

    #Ciclo para intercambiar el nodo raíz con el
    #último nodo, guardar el último nodo en un arreglo
    #auxiliar, reducir el tamaño del heap y
    #usar heapify en el nodo raíz para que el heap
    #vuelva a ser max-heap
    for i in range(len(numbers)-1, -1, -1):
        #Intercambio
        number=numbers[0]
        numbers[0]=numbers[i]
        numbers[i]=number
        #Guardar en arreglo auxiliar
        numbersSorted.insert(0, numbers[i])
        #Reducir tamaño
        numbers.pop(i)
        #Función heapify en nodo raíz
        heapify(numbers, 0)

#Funcion para cambiar a un nodo de lugar en caso de que
#este no sea más grande que sus hijos
def heapify(numbers, i):
    max=i

    #Si el nodo actual tiene un hijo izquierdo y este es más
    #grande que su padre, entonces el hijo izquierdo se guarda
    #como el nodo con el valor más alto
    if(len(numbers)>(max*2+1) and numbers[max*2+1]>numbers[max]):
        max=i*2+1

    #Si el nodo actual tiene un hijo derecho y este es más
    #grande que su padre y que el otro hijo, entonces el hijo derecho
    #se guarda como el nodo con el valor más alto
    if(len(numbers)>(i*2+2) and numbers[i*2+2]>numbers[max]):
        max=i*2+2

    #Si el nodo actual no se quedo guardado como el más grande,
    #entonces el valor del nodo actual se intercambia con el de
    #su hijo más grande y el proceso de heapify se hace con el
    #nodo hijo que ahora tiene el valor que antes tenía su padre
    if(max!=i):
        number=numbers[max]
        numbers[max]=numbers[i]
        numbers[i]=number
        heapify(numbers, max)


print("Input the data. The numbers must be introduced in one line separated by commas.")
print("Example: 11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31")
numbers = [int(number) for number in input().split(',')]
numbersSorted=[]
heapSort(numbers)
print("")
print("Sorted: ", numbersSorted)
