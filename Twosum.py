#Leetcode Problem1 Twosum
nums = input("Input: ")
target = int(input("target = "))
number = [int(x) for x in nums if x.isnumeric()]
out = []
for x,y in enumerate(number):
    for i,j in enumerate(number):
        if y+j == target:
            out.append(x)
            out.append(i)
print("Output:",out)