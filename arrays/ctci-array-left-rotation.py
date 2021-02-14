def rotLeft(arr, d):
    n = len(arr)
    arr = arr[d:n]+arr[0:d]
    return arr
