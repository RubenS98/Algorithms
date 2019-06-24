#Ruben Sanchez A01021759
#Cristopher Cejudo A01025468

def bubbleSort(numbers):
    #Ciclo para hacer Bubble Sort
    #n-1 veces
    for i in range(0, len(numbers)):
        #Ciclo para pasar por cada pareja de
        #números en la lista de números
        for j in range (len(numbers)-1-i):
            #Si un espacio es más chico que
            #el espacio anterior, sus valores
            #se intercambian
            if(numbers[j]>numbers[j+1]):
                number=numbers[j]
                numbers.pop(j)
                numbers.insert(j+1, number)

print("Input the data. The numbers must be introduced in one line separated by commas.")
print("Example: 11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31")
numbers = [int(number) for number in input().split(',')]

#numbers = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
print("")

bubbleSort(numbers)
print("Sorted: ", numbers)
