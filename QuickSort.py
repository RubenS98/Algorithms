#QuickSort Sorting Algorithm by:
#Ruben Sánchez A01021759
#Cristopher Cejudo A01025468

import random #Helps to generate a random array

#Pivotear Function
def pivotear(array,left,right):
    pivote = array[right] #We use the last element of the array as pivot
    i = left - 1

    for j in range(left, right):

        if   array[j] <= pivote:
            #Swap the small number with the greater number
            i = i+1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

    #Last Swap so samaller elements are at the left of the pivot and greater elements at the right of the pivot
    array[right] = array[i+1]
    array[i+1] = pivote

    return ( i+1 )
#End Pivotear Function

#QuickSort Function
def quickSort(array,left,right):
    if left < right:

        position_pivote = pivotear(array, left, right)

        quickSort(array, left, position_pivote-1) #QuickSort on the left array
        quickSort(array, position_pivote+1, right) #QuickSort on the right array
#End QuickSort Function

#Random Array Generator Function
def randomArray(arrlength):
    array = [0] * arrlength
    for i in range(0, arrlength):
        array[i] = random.randint(1,50)
    return array
#End Random Array Generator Function

#Main
array = randomArray(5)

print ("Arreglo generado:")
for i in range(len(array)):
    print (array[i]),
print ""

quickSort(array,0,len(array)-1)
print ("Arreglo ordenado:")
for i in range(len(array)):
    print (array[i]),
#End Main
