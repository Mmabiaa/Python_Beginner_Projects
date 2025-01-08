import matplotlib.pyplot as plt

labels = ('Python', 'Java', 'JavaScript', 'C++')
sizes =[45, 19, 16, 20]

plt.pie(sizes,
        labels=labels, autopct='%1.f%%',
        counterclock=False, startangle=105)

plt.show()