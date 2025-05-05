import mysql.connector

host_name = "172.31.86.125" # IPv4 privada de "MV Bases de Datos"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_employees"  


def get_employees():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"employees": result}


import boto3

ficheroUpload = "data.csv"
nombreBucket = "gcr-output-01"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print("Ingesta completada")
