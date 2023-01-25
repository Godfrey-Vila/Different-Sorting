print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")

print("Insertion Sort")
print("")

print("[26, 22, 91, 67, 15, 49, 59, 32, 2, 17]")
print("")

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i -1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
        print(elements)

if __name__ == '__main__':
    elements = [26, 22, 91, 67, 15, 49, 59, 32, 2, 17]
    insertion_sort(elements)

    print("")
    print(elements)