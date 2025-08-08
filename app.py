from flask import Flask
import mysql.connector
app=Flask(__name__)

@app.route('/')
def create_table():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='hrr'
    )
    cur=conn.cursor()
    cur.execute("create table if not exists kevin(id int auto_increment primary key,name varchar(50),mark int)")
    conn.commit()
    conn.close()
    return "table created successfully"





if __name__=='__main__':
    app.run(debug=True)