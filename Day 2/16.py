if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())[:n]
    z = max(arr)
    while max(arr) == z:
        arr.remove(max(arr))
    print(max(arr))
  
