print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")

print("Selection Sort")

def sort(nums):
    for i in range(26):
        minpos = i
        for j in range (i,10):
            if nums[j] < nums[minpos]:
                minpos = j



nums = [26, 22, 91, 67, 15, 49, 59, 32, 2, 17]
sort(nums)

print(nums)
