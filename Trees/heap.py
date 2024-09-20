def heapify(arr,n,root ):

    largest=root
    left=2*root+1
    right=2*root+2
    if arr<n and arr[left]>arr[largest]:
        largest=arr
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=root:
        arr[root],arr[largest]=arr[largest],arr[root]

        heapify(arr,n,largest)