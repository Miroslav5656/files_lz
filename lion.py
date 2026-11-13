import docx
import matplotlib.pyplot as plt
import pandas as pd
d=docx.Document('lion.docx') #чтение файла
t=''.join(i.text for i in d.paragraphs).lower()
c=''.join(j if j.isalpha() else ' ' for j in t)
w=c.split()
k={} #cловарь слов
for i in w:
    k[i]=k.get(i, 0) + 1
b={} #словарь букв
for j in c:
    if j.isalpha():
        b[j]=b.get(j, 0) + 1
n=len(w) #таблица статистики
tab=pd.DataFrame({'Слово': list(k.keys()),'Частота встречи, раз': list(k.values()),'Частота встречи в %': [round(i / n * 100, 2) for i in k.values()]})
tab=tab.sort_values(by='Частота встречи, раз', ascending=False).reset_index(drop=True)
of='lion_statistics.xlsx'
writer=pd.ExcelWriter(of)
tab.to_excel(writer, sheet_name='Статистика слов')
writer.close()
print(f"Анализ файла 'lion.docx' завершен.")
print(f"Всего слов в тексте: {n}.")
sb=dict(sorted(b.items(), key=lambda x: x[1], reverse=True)) #гистограмма букв
plt.figure(figsize=(12, 6))
plt.bar(sb.keys(), sb.values(), color='blue', edgecolor='black')
plt.xlabel("Буквы")
plt.ylabel("Количество вхождений")
plt.title("Гистограмма встречаемости букв в тексте (lion.docx)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()