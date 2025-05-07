import sqlite3


conn = sqlite3.connect('enrollment.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS enrollment (
    student_id INTEGER,
    semester TEXT,
    course TEXT
)
''')

# Insert data
enrollment_data = [
    (101, '2023A', 'Math'),
    (102, '2023A', 'Math'),
    (103, '2023A', 'Math'),
    (104, '2023A', 'Math')
]

cursor.executemany('INSERT INTO enrollment VALUES (?, ?, ?)', enrollment_data)
conn.commit()

conn.close()
