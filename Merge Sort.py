print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")

print("Merge Sort")
print("")

print("[26, 22, 91, 67, 15, 49, 59, 32, 2, 17]")
print("")

def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_list(left, right, arr)


def merge_two_sorted_list(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = (b[j])
            j+=1
        k+=1
    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = (b[j])
        j+=1
        k+=1
    print(arr)
if __name__ == '__main__':
    arr = [26, 22, 91, 67, 15, 49, 59, 32, 2, 17]
    merge_sort(arr)
    print("")
    print(arr)
