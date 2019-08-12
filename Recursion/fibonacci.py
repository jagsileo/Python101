def printFibonacci(n, store):
    if n <= 0:
        return 0
    elif n == 1:
  
        return 1
    elif n == 2:

        return 1
    elif len(store) >= n:
        return store[n-1]
    else:
        store.append(printFibonacci(n-1, store) + printFibonacci(n-2, store))
        return store[n-1]

def main() :
    store = [1,1]
    print(printFibonacci(100, store))


if __name__ == "__main__":
    main()