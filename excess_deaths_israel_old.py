import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def invert(string):
    return string[::-1]

df = pd.read_csv(r'C:\Users\User\Documents\Projects\excess deaths israel.csv')


x = 7

areaname = invert('%59 מהערכים נמצאים בשטח האפור')
df['rolling2020'] = df['2020'].rolling(x).mean()
df['rolling2019'] = df['2019'].rolling(x).mean()
df['rolling2018'] = df['2018'].rolling(x).mean()
df['rolling2017'] = df['2017'].rolling(x).mean()
df['rolling2000'] = df['2000'].rolling(x).mean()
df['rolling2000-2019'] = df['Average 2000-2019'].rolling(x).mean()
df['rolling2017-2019'] = df['Average 2017-2019'].rolling(x).mean()
df['rolling2.5%'] = df['2.50%'].rolling(x).mean()
df['rolling97.5%'] = df['97.50%'].rolling(x).mean()

plt.plot(df['Date'], df['rolling2020'], color = 'tab:blue', alpha = 1, label = '2020')
#plt.plot(df['Date'], df['rolling2019'], color = 'tab:red', alpha = 0.5, label = '2019')
#plt.plot(df['Date'], df['rolling2018'], color = 'tab:olive', alpha = 0.5, label = '2018')
#plt.plot(df['Date'], df['rolling2017'], color = 'tab:olive', alpha = 0.5, label = '2017')
#plt.plot(df['Date'], df['rolling2000'], color = 'tab:olive', alpha = 0.5, label = '2000')
plt.plot(df['Date'], df['rolling2000-2019'], color = 'black', alpha = 0.5, label = invert('ממוצע 9102-0002'))
plt.plot(df['Date'], df['rolling2017-2019'], color = 'tab:orange', alpha = 0.75, label = invert('ממוצע 9102-7102'))
plt.annotate(areaname,(75,17.5), xytext = (80,20), arrowprops = dict(arrowstyle = '->', alpha = 0.75))
plt.fill_between(df['Date'], df['rolling2.5%'], df['rolling97.5%'], color = 'silver', alpha = 0.5)
plt.xticks(ticks = [0,31,60,91,121,152,182,213,244,275,305,335], labels = ['Jan', 'Feb', 'Mar', "Apr", 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.title(invert('שיעור תמותה יומי בישראל למיליון נפש בשנים 0202-0002'))
plt.ylabel(invert(' ימים') + str(x) + invert('שיעור תמותה יומי למיליון נפש, ממוצע נע של '))
plt.xlabel(invert('חודש'))
plt.legend()


plt.savefig(r'C:\Users\User\Documents\Projects\fig_excess_deaths.png', dpi =300)