import csv
import matplotlib.pyplot as plt

x = []
y1 =[]
y2 =[]
y3 =[]

with open("2020/16 Import fra .csv/Blodsukker Oppgave/blodsukkerdata.csv") as data_csv:
    blodsukkerdata = csv.reader(data_csv, delimiter = ",")
    i = 0
    for l in blodsukkerdata:
        if i == 0:
            y_label = str(l[1])
            y1_label = str(l[1])
            y2_label = str(l[2])
            y3_label = str(l[3])
        else:
            x.append(float(l[0]))
            y1.append(float(l[1]))
            y2.append(float(l[2]))
            y3.append(float(l[3]))
        i += 1

plt.plot(x, y1, label=y1_label)
plt.plot(x, y2, label=y2_label)
plt.plot(x, y3, label=y3_label)
plt.grid()

plt.title("Blodsukker")
plt.legend()
plt.xlabel("Tid")
plt.ylabel("Blodsukker")

plt.show()