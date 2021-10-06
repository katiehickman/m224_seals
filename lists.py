app = Flask(__name__)

# Challenge 1
var1 = 3
var2: str = "Mr. Mortensen"
var3: chr = 'f'
var4: float = 0.4

print(var1 + ': Integer')
print(var2 + ': String')
print(var3 + ': Character')
print(var4 + ': Float')


# Challenge 2
list1 = [5, 3, 4, 1, 2]
list2 = [list1[3], list1[4], list1[1], list1[2], list1[0]]


# Challenge 3
averageList = [23, 41, 90, 55, 71, 83]

averageList[0] += 3
averageList[1] += 3
averageList[2] += 3
averageList[3] += 3
averageList[4] += 3
averageList[5] += 3

average = (averageList[0] + averageList[1] + averageList[2] + averageList[3] + averageList[4] + averageList[5])/6

print(average)