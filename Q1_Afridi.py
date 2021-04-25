import heapq

# open the file and read the data into a list
file = open("rand1000000.txt","r")
data = file.read().split(" ")
for index,element in enumerate(data):
    data[index] = element.strip()
data = [int(x) for x in data if x != '']

# this function creates two sublists of size 50 to sort with radix and bucket sort
def makesubL(arr,numOfsubs):
    output = []
    # setting the size of the sublists, which is 50
    subArrayLength = len(arr)//numOfsubs
    # put first half of the data read in from input file in one sublist and second half into second sublist
    for i in range(subArrayLength,len(arr)+1,subArrayLength):
        output.append(arr[i - subArrayLength : i])
    return output
    
# print(makesubL(data, 100))
sublists = makesubL(data, 100)


def mergeFunc(arr):
    heap = []
    output = []
    i = 0
    # remove first element of array and push it onto the heap
    for i in range(len(arr)):
        element = (arr[i].pop(0),i)
        heap.append(element)
    heapq.heapify(heap)

    # 
    while len(heap) > 0:
        smallest,index = heapq.heappop(heap)
        output.append(smallest)
        if len(arr[index]) > 0:
            heapq.heappush(heap,(arr[index].pop(0),index))
    return output

def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # output will be sorted array
    output = [0] * (n) 
  
    # count array should be empty on intialization 
    count = [0] * (10) 
  
    # keep the number of occurences found in the count array
    for i in range(0, n): 
        index = (arr[i] / exp1) 
        count[int(index % 10)] += 1
  
    # the current element of count should contain the position of the digit in the output array
    for i in range(1, 10): 
        count[i] += count[i - 1] 
  
    # constructing the  output of the array
    i = n - 1
    while i >= 0: 
        index = (arr[i] / exp1) 
        output[count[int(index % 10)] - 1] = arr[i] 
        count[int(index % 10)] -= 1
        i -= 1
  
    # copy output into new array so that it holds all sorted numbers
    i = 0
    for i in range(0, len(arr)): 
        arr[i] = output[i] 
  
def radixSort(arr): 
  
    # Find max number of digits to sort
    max1 = max(arr) 
  
    # Apply counting sort on every digit.
    exp = 1
    while max1 / exp > 0: 
        countingSort(arr, exp) 
        exp *= 10

def insertionSort(b):
    # Iterate through the entire array to set up the key to sort around. Exit loop once everything is sorted.
    for i in range(1, len(b)):
        up = b[i]
        # Locate where to insert the key value into the array.
        j = i - 1
        while j >= 0 and b[j] > up: 
            b[j + 1] = b[j]
            j -= 1
        # insert the key into the new position found.
        b[j + 1] = up     
    return b     
             
def bucketSort(x):
    norm = max(x)
    arr = []
    slot_num = 10 # 10 buckets, each
                  # bucket's size is 0.1
    for i in range(slot_num):
        arr.append([])
         
    # place the elements of the array into their respective buckets
    for j in x:
        index_b = int(slot_num * (j/(norm+1)))
        arr[index_b].append(j)
     
    #  sort numbers in the buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
         
    # combine all the buckets
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
 
# Driver Code


# print(len(sublists))

for i in range(50):
    radixSort(sublists[i])
    bucketSort(sublists[i+50])
newArr = mergeFunc(sublists)
print(newArr)

