def solution(arr, queries):
    for a,b in queries:
        c=arr[a]
        arr[a]=arr[b]
        arr[b]=c


    return arr