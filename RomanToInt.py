#Leetcode Problem14 Roman to Integer

Roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,"IV":4,"IX":9, "XL":40,"XC":90, "CD":400, "CM":900} #Added the special case of each conditions
s = input("Input: ")
total = 0
i = 0 #Index
if 1 <= len(s) <= 15:
    while i < len(s):
        if s[i:i+2] in Roman: #Check whether it has special condition or not
            print(Roman[s[i:i+2]])
            total += Roman[s[i:i+2]]
            i += 2 #To count index when we check for each condition
        else:
            print(Roman[s[i]])
            total += Roman[s[i]]
            i += 1
print("Output:",total)


# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         Roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,"IV":4,"IX":9, "XL":40,"XC":90, "CD":400, "CM":900} #Added the special case of each conditions
#         s = input("Input: ")
#         total = 0
#         i = 0 #Index
#         if 1 <= len(s) <= 15:
#             while i < len(s):
#                 if s[i:i+2] in Roman: #Check whether it has special condition or not
#                     print(Roman[s[i:i+2]])
#                     total += Roman[s[i:i+2]]
#                     i += 2 #To count index when we check for each condition
#                 else:
#                     print(Roman[s[i]])
#                     total += Roman[s[i]]
#                     i += 1
#         return total
#         print("Output:",total)
# Solution("III")