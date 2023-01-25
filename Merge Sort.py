print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")

print("Merge Sort")
print("")

print("[26, 22, 91, 67, 15, 49, 59, 32, 2, 17]")
print("")

def merge_sort(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    return sorted_list

if __name__ == '__main__':
    a = [26, 22, 91, 67, 15]
    b = [49, 59, 32, 2, 17]

    print(merge_sort(a, b))