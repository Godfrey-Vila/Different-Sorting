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

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi -1)
        quick_sort(elements, pi+1, end)
        print(elements)
if __name__ == '__main__':
    elements = [26, 22, 91, 67, 15, 49, 59, 32, 2, 17]
    quick_sort(elements, 0, len(elements)-1)
    print("")
    print(elements)