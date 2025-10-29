import matplotlib.pyplot as plt

fh = open("StudentExercise.csv")

hours = []

next(fh)

for line in fh:
    words = line.split(',')
    if len(words[0]) > 0:
        hours.append(float(words[0]))

plt.hist(hours, bins=10)

plt.show()
