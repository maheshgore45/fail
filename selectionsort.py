def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    print("Enter number of elements:")
    n = int(input())
    arr = []

    print("Enter elements:")
    for i in range(n):
        arr.append(int(input()))

    print("Before Selection Sort:")
    print(*arr)

    selection_sort(arr)

    print("After Selection Sort:")
    print(*arr)



#Enter number of elements:
#5
#Enter elements:
#9
#2
#7
#4
#14
#Before Selection Sort:
#9 2 7 4 14
#After Selection Sort:
#2 4 7 9 14