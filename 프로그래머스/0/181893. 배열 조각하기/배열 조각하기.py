def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]  # query[i] 포함해서 앞부분만 남김
        else:
            arr = arr[query[i]:]    # query[i]부터 끝까지 남김
    return arr