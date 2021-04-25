
listR = [1,5,6,8,9,7,3] 
yIndex = 1


# def max_heapify(array, i):

#       left = 2 * i
#       right = 2 * i + 1
#       length = len(array) - 1  # for termination condition check
#       largest = i

#       if left <= length and array[i] < array[left]:
#           largest = left
#       if right <= length and array[largest] < array[right]:
#           largest = right
#       if largest != i:
#           array[i], array[largest] = array[largest], array[i]
#           max_heapify(array, largest)
# max_heapify(listR,yIndex)
# print(listR)




def max_heapify(array, i): 
    largest = i     # node in the tree that has children
    left = 2 * i # used to build left part of tree
    right = 2 * i + 1 # used to build right part of the tree
    length = len(array) - 1
    # Creating an iterative version of the max_heapify function.
    while i <= length:

        # if the left part of the array is bigger than current index of the array, change the current node to satisfy heap property
        if array[left] >= array[i]:
            largest = left
        # else 
        else:
            
            largest = i
        # if the right part of the array is bigger than current index of the array, change the current node to satisfy heap property
        if array[right] >= array[largest]:
            largest = right

        # else if the current node value does not equal i
        if largest != i:
            # swap the current index of the array with the largest node in the tree
            temp = array[i]

            array[i] = array[largest]

            array[largest] = temp
        #  else break out of the loop
        else:
            break

max_heapify(listR,yIndex)

print("Iterative Heap: ",listR)