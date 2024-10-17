import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json('../data/data.jsonl', lines=True)

pd.options.display.max_columns = None

df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

df['_data_coleta'] = datetime.now()

df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)


