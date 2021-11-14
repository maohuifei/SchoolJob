import matplotlib.pyplot as plt

name_list = ['LQP', 'JZW', 'ZRZ', 'LPH']
num_list = [1.5, 3.6, 2.8, 3]
num_list1 = [1, 3, 2, 1]
plt.bar(range(len(num_list)), num_list, label='IQ', fc='y')
plt.bar(range(len(num_list)), num_list1, bottom=num_list, label='EQ', tick_label=name_list, fc='r')
plt.legend()
plt.show()