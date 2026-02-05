import sqlite3
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'bank_marketing.db')
CSV_PATH = os.path.join(BASE_DIR, 'data', 'bank_marketing.csv')

# Conectar ao banco
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Criar tabela (apenas colunas existentes)
cursor.execute("""
CREATE TABLE IF NOT EXISTS bank_marketing (
    age INTEGER,
    job TEXT,
    marital TEXT,
    education TEXT,
    default_status TEXT,
    housing TEXT,
    loan TEXT,
    contact TEXT,
    month TEXT,
    day_of_week TEXT,
    target TEXT
)
""")

# Limpar tabela para evitar duplicatas
cursor.execute("DELETE FROM bank_marketing")

# Ler CSV e inserir dados
with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:
        cursor.execute("""
        INSERT INTO bank_marketing (
            age, job, marital, education, default_status,
            housing, loan, contact, month, day_of_week, target
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            int(row['age']),
            row['job'],
            row['marital'],
            row['education'],
            row['default'],
            row['housing'],
            row['loan'],
            row['contact'],
            row['month'],
            row['day_of_week'],
            row['y']
        ))

conn.commit()
conn.close()

print("Banco criado e dados importados com sucesso.")

