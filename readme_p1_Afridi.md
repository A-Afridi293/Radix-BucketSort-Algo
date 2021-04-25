FUNCTION mergeFunc(arr):
heap = empty array
output = empty array
i = 0
loop through length of array:
element = (arr[i].pop(0),i)
heap.append(element)
ENDFOR
heapq.heapify(heap)
ENDIF
while heap still has elements to give:
smallest,index = heapq.heappop(heap)
output.append(smallest)
IF len(arr[index]) > 0:
heapq.heappush(heap,(arr[index].pop(0),index))
ENDIF
ENDWHILE
RETURN output

k= number of sub arrays
n = number of elements 1000000

My Psuedo Code meets O(nlogK) becuase removing the smallest element from a minimum heap data structure has a constant time complexity of O(1). After removing the smallest element we now have to re-heapify our heap. Since we removed the smallest element from the heap we have violated the heap property and becuase of this we now have to utilize the heapify function to ensure that the minimum node is now the root node. It is important we use a heap rather than a simple list becasuse if we transverse the data in a linear fashion using the list, this drastically reduces the effeciency of the program. The use of the heap datas strucutre shown in my psuedo code stategically traverses the data and provides effiency towards our program.

The heapify function has a time complexity of O(lg k) and thus if we combine the 2 time complexities we can concur that the dominating term is lg(k). Since we are sortin n amount of elements and the cost of using the heap to merge the list is O(lg K) we know our over all time complexity is O(n) \* O(lg k) and thus equates to O(n lg k).

Question 3) As seen in the reference.PNG we can clearly see that even when O(nk) is an almost perfect algorithm with a very low time constant, O(n lg k ) is still more effecient. The O(n lg K ) is the graph in red and the rest are various simulations of O(nk) for varying time constants.
