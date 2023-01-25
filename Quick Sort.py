print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")

print("Merge Sort")
print("")

print("[26, 22, 91, 67, 15, 49, 59, 32, 2, 17]")
print("")

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements):
    pivot_index = 0
    pivot = elements[pivot_index]

    start = pivot_index + 1
    end = len(elements) - 1

    while start < end:
        while elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

def quick_sort(elements):
    partition(elements)

if __name__ == '__main__':
    elements = [26, 22, 91, 67, 15, 49, 59, 32, 2, 17]
    quick_sort(elements)
    print(elements)