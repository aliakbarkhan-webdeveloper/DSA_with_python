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


# code for min heap

def min_heapify(arr,n,root ):

    smallest=root
    left=2*root+1
    right=2*root+2
    if left<n and arr[left]<arr[smallest]:
        smallest=left
    if right<n and arr[right]<arr[smallest]:
        smallest=right
    if smallest!=root:
        arr[root],arr[smallest]=arr[smallest],arr[root]

        min_heapify(arr,n,smallest)

def build_min_heap(arr):
    n=len(arr)
    for i in reversed(range(n//2)):
        min_heapify(arr,n,i)

build_min_heap(heap)
print(heap)

#Heap sort