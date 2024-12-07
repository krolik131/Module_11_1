import matplotlib.pyplot as plt
import pandas as pd

name = pd.Series({'Вася': 40, 'Петя': 15, 'Маша': 20, 'Даша': 25})
plt.title('Как разделить пицу, в соответсвии кто сколько заплатил')
plt.pie(name, labels=name.index)
plt.show()