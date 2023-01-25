print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")

print("Bubble Sort")
print("")

print("[26, 22, 91, 67, 15, 49, 59, 32, 2, 17]")
print("")

def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums [j+1] = temp

                print(nums)



nums = [26, 22, 91, 67, 15, 49, 59, 32, 2, 17]
sort (nums)
print("")
print(nums)