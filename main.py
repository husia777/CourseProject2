import psycopg2
import csv
import pandas
import json
import requests


def db_connecting():
    """
    Функция подключения к базе данных
    :return: Возвращает
    """
    try:
        connection = psycopg2.connect(user="postgres"
                                      , password="postgres"
                                      , host="127.0.0.1"
                                      , port="5432"
                                      ,database="course_project")
        connection.autocommit = True
        print('Подключение к базе данных установленно')
        return connection
    except:
        print('Ошибка подключение')
        return False

def get_data_s():
    with open('suppliers.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for i in range(len(data)):
        data[i]['id'] = i+1
    return data

def insert_data_in_suppliers():
    data = get_data_s()
    with open("file.sql", 'w', encoding='utf-8') as file:
        for i in data:
            product = [j.replace("'", "''") for j in i['products']]
            updated_data_for_suppliers = f"""UPDATE products SET suppliers_id = {i['id']} WHERE product_name in ('{"', '".join(product)}');\n """
            file.write(updated_data_for_suppliers)



def main():
    conn = db_connecting()
    cursor = conn.cursor()
    get_data_s()
    insert_data_in_suppliers()

if __name__ == "__main__":
    main()