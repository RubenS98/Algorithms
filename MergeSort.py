#QuickSort Sorting Algorithm by:
#Ruben Sanchez A01021759
#Cristopher Cejudo A01025468

import random #Helps to generate a random array

#MergeSort Function
def mergeSort(array):
    i = 0 #iterates left array
    j = 0 #iterates right array
    k = 0 #iterates the array merged

    if len(array) >1:
        mid = len(array)//2
        left = array[mid:] #Left array will be half size of the array rounded up
        right = array[:mid] #Left array will be half size of the array rounded down

        mergeSort(left) #Merge left size
        mergeSort(right) #Merge right size

        #Compare the elements one by one and order them from samaller to grater
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i] #Smaller element is in the left array
                i+=1
            else:
                array[k] = right[j] #Smaller element is in the right array
                j+=1
            k+=1

        #Check for any element left
        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1
#End MergeSort Function

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

mergeSort(array)
print ("Arreglo ordenado:")
for i in range(len(array)):
    print (array[i]),
#End Main
