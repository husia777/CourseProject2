import psycopg2
import json



def get_data_s():
    with open('suppliers.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for i in range(len(data)):
        data[i]['id'] = i+1
        print(data)
    return data

def insert_data_in_suppliers():
    data = get_data_s()
    with open("file.sql", 'w', encoding='utf-8') as file:
        file.write(""" ALTER TABLE products ADD COLUMN suppliers_id INTEGER;""")
        for i in data:
            product = [j.replace("'", "''") for j in i['products']]
            updated_data_for_suppliers = f"""UPDATE products SET suppliers_id = {i['id']} WHERE product_name in ('{"', '".join(product)}');\n """
            file.write(updated_data_for_suppliers)


    with open('file.sql', 'a', encoding='utf-8') as file:
        for i in data:
            file.write(f"""INSERT INTO suppliers VALUES ({i['id']}, '{i['company_name'].replace("'", '')}', '{i['contact'].split(',')[0]}', '{i['contact'].split(',')[1]}','{i['address'].split(';')[0].strip(';')}','{i['address'].split(';')[1].strip(';')}','{i['address'].split(';')[2].strip(';')}','{i['address'].split(';')[3].strip(';')}','{i['address'].split(';')[4].replace("'", '')}', '{i['phone']}','{i['fax'] if len(i['fax'])>0 else 0}','{i['homepage'].replace("'", '') if len(i['homepage'])>0 else 0}');\n""")
    with open("file.sql", 'a', encoding='utf-8') as file:
        file.write("""ALTER TABLE  products ADD CONSTRAINT fk_suppliers_id FOREIGN KEY(suppliers_id)  REFERENCES suppliers(suppliers_id);\n""")


def main():
    get_data_s()
    insert_data_in_suppliers()

if __name__ == "__main__":
    main()

