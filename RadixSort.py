#Ruben Sanchez A01021759
#Cristopher Cejudo A01025468

#Función principal
def radixSort(numbers):
    #Se inicializa digit en 1
    #para que primero se ordenen
    #los números según los valores
    #de sus unidades
    digit=1
    #Ciclo que ejecuta Counting Sort
    #con cada dígito, empezando con el
    #de las unidades, hasta llegar
    #al dígito más significativo
    #que tenga el número más grande
    #de la lista
    while(max(numbers)/digit>=1):
        countSort(numbers, digit)
        digit*=10

#Counting Sort para ordenar los números
#con base en un dígito en específico
def countSort(numbers, digit):
    #Creación de listas
    temp=[]
    digits=[]

    #Llenado de lista temporal que guardará
    #los números dados por un tiempo
    for i in range (0, len(numbers)):
        temp.append(0)

    #Llenado de lista que guardará
    #cuantas veces aparece cada dígito
    #(0, 1, 2, 3, ..., 9) en los
    #números dados por el usuario
    for i in range (0, 10):
        digits.append(0)

    #Se obtiene un dígito específico de
    #cada número en la lista (depende del
    #valor de digit) y se le suma 1 al
    #espacio de digits que corresponda
    #al valor del dígito del número
    for x in numbers:
        digits[int((x/digit)%10)]+=1

    #A cada espacio de digits, se le
    #suma el valor del espacio anterior
    #para que los valores de digits
    #representen realmente en que
    #posiciones deben ir los números
    #dados
    for i in range(1, len(digits)):
        digits[i]+=digits[i-1]

    #Ciclo que mete cada número del arreglo
    #original en el espacio que le toca en
    #la lista temporal, basándose en los valores
    #de digits, para que al final la lista temporal
    #tenga a los números ordenados por dígito
    for i in range(len(temp)-1, -1, -1):
        temp[digits[int((numbers[i]/digit)%10)]-1]=numbers[i]
        #Se le tiene que restar 1 al valor del espacio
        #de digits para que el siguiente número que tenga
        #el mismo dígito no quede en el mismo espacio
        digits[int((numbers[i]/digit)%10)]-=1

    #Numbers se actualiza con el arreglo ordenado
    for i in range(0, len(numbers)):
        numbers[i]=temp[i]

print("Input the data. The numbers must be introduced in one line separated by commas.")
print("Example: 11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31")
numbers = [int(number) for number in input().split(',')]

radixSort(numbers)
print("")

print("Sorted: ", numbers)
