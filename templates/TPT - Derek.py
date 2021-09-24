var1 = 3
var2 = "Mr. Mortensen"
var3 = 'f'
var4 = 0.4

print("{}: Integer\n" + "{}: String\n" + "{}: Character\n" + "{}: double or float", var1, var2, var3, var4)

# Challenge 2

# Basic Solution

list1 = [5, 3, 4, 1, 2]
list2 = [0, 0, 0, 0, 0]
list2[0] = list1[3]
list2[1] = list1[4]
list2[2] = list1[1]
list2[3] = list1[2]
list2[4] = list1[0]

# Alternate Solution

list2 = [list1[3], list1[4], list1[1], list1[2], list1[0]]

# Advanced Solution

def orderList(list):  # Selection Sort; find the lowest number and put it at the front

    for i in range(len(list)):
        startingIndex = i
        smallestIndex = i
        for j in range(i + 1, len(list)):
            if list[j] < list[i]:
                smallestIndex = j
        list[i] = list[smallestIndex]
    print(list)


# Challenge 3

# Basic Solution

averageList = [23, 41, 90, 55, 71, 83]

averageList[0] += 3
averageList[1] += 3
averageList[2] += 3
averageList[3] += 3
averageList[4] += 3
averageList[5] += 3

average = (averageList[0] + averageList[1] + averageList[2] + averageList[3] + averageList[4] + averageList[5])/6

print(average)


# Advanced Solution

def findAverage(list):
    sum = 0
    for num in list:
        sum += num + 3
    print(sum/len(list))