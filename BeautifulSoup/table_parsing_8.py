import pandas as pd
import json

data = pd.read_html('https://parsinger.ru/4.8/6/index.html', header=0, encoding='utf-8')
df = data[0].loc[:,['Марка Авто','Год выпуска','Тип двигателя','Стоимость авто']]
print (df)
filtered_table=df[(df['Стоимость авто'] <= 4000000) & (df["Год выпуска"] >= 2005) & (df["Тип двигателя"] == "Бензиновый")].sort_values('Стоимость авто')
a=filtered_table.to_dict(orient='records')
print(json.dumps(a, indent=4, ensure_ascii=False))