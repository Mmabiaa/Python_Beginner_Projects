import matplotlib.pyplot as plt

ages = [2, 50, 70, 40,30,50,59,4,84,34,30,30,48,2,7,18,30,34,90,50]

range =(0,100)
bins = 10

plt.hist(ages,bins, range, color='green', histtype='bar', rwidth=0.7)
plt.xlabel('Ages')
plt.ylabel('Bins')
plt.title('Histogram Plot')
plt.show()