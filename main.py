import sqlite3
import random,string

def create_con(db_name):
    con = None
    try:
        con = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return con

def create_table(con, sql):
    try:
        cursor = con.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

db_name = 'hw.db'

con = create_con(db_name)

create_products_table_sql = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) DEFAULT 0.0 NOT NULL,
quantity INTEGER DEFAULT 0 NOT NULL
)
'''

#create_table(con, create_products_table_sql)

def insert_products(con):
    for i in range (15):
        product_title = ''.join(random.choices(string.ascii_uppercase, k=12))
        price = random.randint(10,1000)
        quantity = random.randint(1,100)

        try:
            sql = '''INSERT INTO products (product_title, price, quantity) 
            VALUES (?, ?, ?)
            '''
            cursor = con.cursor()
            cursor.execute(sql, (product_title,price,quantity))
            con.commit()
        except sqlite3.Error as e:
            print(e)

#if con != None:
#    insert_products(con)
#    con.close()

def set_quantity_by_id(con,id,quantity):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = con.cursor()
        cursor.execute(sql,(quantity,id))
        con.commit()
    except sqlite3.Error as e:
            print(e)

def set_price_by_id(con, id, price):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = con.cursor()
        cursor.execute(sql,(price,id))
        con.commit()
    except sqlite3.Error as e:
            print(e)

def delete_by_id(con, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = con.cursor()
        cursor.execute(sql,(id,))
        con.commit()
    except sqlite3.Error as e:
            print(e)

def select_all_products(con):
    try:
        sql = '''SELECT * FROM products'''
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
            print(e)

def select_products_by_price_and_quantity(con, price,quantity):
    try:
        sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
        cursor = con.cursor()
        cursor.execute(sql,(price,quantity))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
            print(e)

def select_products_by_title(con, product_title):
    try:
        sql = '''SELECT * FROM products WHERE UPPER(product_title) LIKE UPPER(?)'''
        cursor = con.cursor()
        cursor.execute(sql,(product_title,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
            print(e)

if con != None:
    insert_products(con)
    set_quantity_by_id(con, 2, 67)
    set_price_by_id(con, 2, 607)
    delete_by_id(con,3)
    select_all_products(con)
    select_products_by_price_and_quantity(con, 500,5)
    select_products_by_title(con, '%bop%')
    con.close()