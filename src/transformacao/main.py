import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json('../data/data.jsonl', lines=True)

pd.options.display.max_columns = None

df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

df['_data_coleta'] = datetime.now()

df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)

df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

conn = sqlite3.connect('../data/quotes.db')

df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

conn.close()

print(df.head())


