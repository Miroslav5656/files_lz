import pandas as pd
import matplotlib.pyplot as plt
import pyarrow.parquet as pq
t = pq.read_table('titanic.parquet') #читает таблицу
c = t.to_pandas()
c.to_csv('titanic.csv', index=False) #сохраняем в csv
n = c.groupby('Pclass').size() #колво пассажиров в каждом классе
s = c[c['Survived']==1].groupby('Pclass').size()/n*100 #процент выживыших
ns = c[c['Survived']==0].groupby('Pclass').size()/n*100 #процент погибших
sd = pd.DataFrame({'Выжил':s,'Не выжил':ns})
sd.index = ['Первый класс','Второй класс','Третий класс']
g = sd.plot(kind='bar',stacked=True,color=['green','red']) #создаем график
plt.xlabel('Класс билета')
plt.ylabel('Доля пассажиров (%)')
plt.title('Выживаемость пассажиров Титаника')
plt.legend(title='Статус')
plt.ylim(0,100)
plt.show()