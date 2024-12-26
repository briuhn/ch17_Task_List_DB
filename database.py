import sqlite3

def connect():
    conn = sqlite3.connect('task_list.db')
        with open('task_list_db.sql', 'r') as file:
        sql_script = file.read()
        conn.executescript(sql_script)
    
    return conn

def get_tasks(completed=False):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT taskID, description FROM Task WHERE completed = ?", (int(completed),))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def add_task(description):
    conn = connect()
    conn.execute("INSERT INTO Task (description, completed) VALUES (?, 0)", (description,))
    conn.commit()
    conn.close()

def complete_task(task_id):
    conn = connect()
    conn.execute("UPDATE Task SET completed = 1 WHERE taskID = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect()
    conn.execute("DELETE FROM Task WHERE taskID = ?", (task_id,))
    conn.commit()
    conn.close()
