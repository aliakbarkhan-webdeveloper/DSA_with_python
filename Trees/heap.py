def max_heapify(arr,n,root ):

    largest=root
    left=2*root+1
    right=2*root+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=root:
        arr[root],arr[largest]=arr[largest],arr[root]

        max_heapify(arr,n,largest)

def buildHeap(arr):
    n=len(arr)
    for i in reversed(range(n//2)):
        max_heapify(arr,n,i)


heap=[100,5,3,2,8,15,6,102]
buildHeap(heap)
print(heap)



