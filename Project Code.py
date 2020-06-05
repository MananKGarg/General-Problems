def ispow2(n):
    if (n == 0):
        return False
    elif (n ==1):
        return False
    while (n != 1):
        if(n % 2 != 0):
            return  False
        n = n // 2
    return True

def no2(n):

    count = 0
    while(n != 1 ):
        n = n//2
        count += 1
    return count



t = int(input())

for k in range(t):
    string = input()
    string = string.split()
    nums = [int(i) for i in string]


    if ( (nums[0] == 0) or (nums[1] == 0)):
        print("-1")
    elif (nums[0] == nums[1]):
        print("0")

    elif(nums[0]*nums[1] > 0):

        nums[0] = abs(nums[0])
        nums[1] = abs(nums[1])

        if (nums[1] > nums[0]):



            if ( ispow2(nums[1] // nums[0])):

                p = no2(nums[1]//nums[0])

                if p == 1:
                    print("1")
                elif p == 2:
                    print("1")
                elif p % 3 == 0:
                    print((p//3))
                else:
                    print((p//3) + 1)
            else:
                print("-1")
        else:
            if (ispow2(nums[0] // nums[1])):

                p = no2(nums[0] // nums[1])

                if p == 1:
                    print("1")
                elif p == 2:
                    print("1")
                elif p % 3 == 0:
                    print((p//3))
                else:

                    print((p // 3) + 1)
            else:
                print("-1")











