#Ruben Sanchez A01021759
#Cristopher Cejudo A01025468
from Node import Node

def insertar(initialNode, nodeNumber):
    if(initialNode==None):
        initialNode=Node(nodeNumber)
        return initialNode

    if(initialNode.number==nodeNumber):
        return initialNode

    if(initialNode.number>nodeNumber):
        initialNode.left=insertar(initialNode.left, nodeNumber)

    if(initialNode.number<nodeNumber):
        initialNode.right=insertar(initialNode.right, nodeNumber)

    return initialNode

def printTree(initialNode, tabs):
    space=""
    for i in range(0, tabs):
        space=space+"\t"

    if(initialNode!=None):
        printTree(initialNode.right, tabs+1)
        print(space+str(initialNode.number))
        print("")
        printTree(initialNode.left, tabs+1)

print("Input the data. The numbers must be introduced in one line separated by commas.")
print("Example: 11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31")
numbers = [int(number) for number in input().split(',')]

#numbers = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]

initial=Node(numbers[0])
#print(numbers[0])
numbers.pop(0)
print("")

for x in numbers:
    initial=insertar(initial, x)

printTree(initial, 0)
