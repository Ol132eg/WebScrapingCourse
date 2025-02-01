import pandas as pd

data = pd.read_html('https://parsinger.ru/table/5/index.html', header=0)
df = data[0]

print(df.sum(axis=0).round(3).to_dict())
