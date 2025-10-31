import matplotlib.pyplot as plt

def avg(ls):
    sum = 0
    for num in ls:
        sum += num
    return sum/len(ls)

def aboveAvg(ls, avg):
    above = 0
    for num in ls:
        if num > avg:
            above += 1
    return (above/len(ls))*100

def median(ls):
    ls.sort()
    if len(ls)%2 == 0:
        return (ls[len(ls)//2]+ls[(len(ls)//2)-1])/2
    else:
        return ls[len(ls)//2]

fh = open("StudentExercise.csv")

hours = []

next(fh)

for line in fh:
    words = line.split(',')
    if len(words[0]) > 0:
        hours.append(float(words[0]))

plt.hist(hours, bins=10)

average = avg(hours)
median = median(hours)

print("average:",average)

print("percentage of students above average:", aboveAvg(hours,average), "%")

print("median:", median)

plt.show()





