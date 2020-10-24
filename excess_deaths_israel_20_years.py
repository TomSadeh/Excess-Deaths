import pandas as pd
from matplotlib import pyplot as plt

def invert(string):
    return string[::-1]

df = pd.read_csv(r'C:\Users\User\Documents\Projects\Daily Excess Deaths\excess deaths results.csv')

x = 7
w = 6
areaname = invert('%59 מהנתונים נמצאים בשטח האפור')

df['rolling2020'] = df['2020'].rolling(x, min_periods = w).mean()
df['rolling2019'] = df['2019'].rolling(x, min_periods = w).mean()
df['rolling2018'] = df['2018'].rolling(x, min_periods = w).mean()
df['rolling2017'] = df['2017'].rolling(x, min_periods = w).mean()
df['rolling2000'] = df['2000'].rolling(x, min_periods = w).mean()
df['2.50%'] = df.loc[:,'2000':'2020'].quantile(0.025, axis = 'columns')
df['97.50%'] = df.loc[:,'2000':'2020'].quantile(0.975, axis = 'columns')
df['rolling2.5%'] = df['2.50%'].rolling(x, min_periods = w).mean()
df['rolling97.5%'] = df['97.50%'].rolling(x, min_periods = w).mean()

df['Average 2000-2019'] = df.loc[:,'2000':'2019'].mean(axis = 'columns')
df['Average 2000-2002'] = df.loc[:,'2000':'2002'].mean(axis = 'columns')
df['Average 2010-2019'] = df.loc[:,'2010':'2019'].mean(axis = 'columns')
df['Average 2017-2019'] = df.loc[:,'2017':'2019'].mean(axis = 'columns')
df['rolling2000-2019'] = df['Average 2000-2019'].rolling(x, min_periods = w).mean()
df['rolling2017-2019'] = df['Average 2017-2019'].rolling(x, min_periods = w).mean()
df['rolling2000-2002'] = df['Average 2000-2002'].rolling(x, min_periods = w).mean()
df['rolling2010-2019'] = df['Average 2010-2019'].rolling(x, min_periods = w).mean()

plt.plot(df['Date'], df['rolling2020'], color = 'tab:blue', alpha = 1, label = '2020')
#plt.plot(df['Date'], df['rolling2019'], color = 'tab:red', alpha = 0.5, label = '2019')
#plt.plot(df['Date'], df['rolling2018'], color = 'tab:olive', alpha = 0.5, label = '2018')
#plt.plot(df['Date'], df['rolling2017'], color = 'tab:olive', alpha = 0.5, label = '2017')
#plt.plot(df['Date'], df['rolling2000'], color = 'tab:olive', alpha = 0.5, label = '2000')
#plt.plot(df['Date'], df['rolling2000-2002'], color = 'tab:olive', alpha = 0.5, label = invert('ממוצע 0002-2002'))
plt.plot(df['Date'], df['rolling2000-2019'], color = 'black', alpha = 0.5, label = invert('ממוצע 9102-0002'))
#plt.plot(df['Date'], df['rolling2010-2019'], color = 'black', alpha = 0.5, label = invert('ממוצע 9102-0102'))
plt.plot(df['Date'], df['rolling2017-2019'], color = 'tab:orange', alpha = 0.75, label = invert('ממוצע 9102-7102'))

plt.annotate(areaname,(90,18.5), xytext = (120,18.5), arrowprops = dict(arrowstyle = '->', alpha = 0.75))
plt.fill_between(df['Date'], df['rolling2.5%'], df['rolling97.5%'], color = 'silver', alpha = 0.5, linewidth = 0)
plt.xticks(ticks = [0,31,60,91,121,152,182,213,244,275,305,335], labels = ['Jan', 'Feb', 'Mar', "Apr", 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.title(invert('שיעור תמותה יומי מתוקנן לגיל בישראל למיליון נפש בשנים 0202-0002'))
plt.ylabel(invert(' ימים') + str(x) + invert('שיעור תמותה, ממוצע נע של '))
plt.xlabel(invert('חודש'))
plt.legend()

plt.savefig(r'C:\Users\User\Documents\Projects\Daily Excess Deaths\fig_excess_deaths.png', dpi = 500)