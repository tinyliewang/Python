import random
nums = list(range(0, 10))
random.shuffle(nums)
target = [str(nums.pop()) for i in range(4)]
while 1:
    choice = list(input("input your choice\n"))
    if choice == target:
        print("you got it")
        break
    else:
        a = b = 0
        for i, num in enumerate(choice):
            if num == target[i]:
                a += 1
            elif num in target:
                b += 1
        print("{}A{}B".format(a, b))
