import json
import pandas as pd
from datetime import datetime


def leer_datos_clientes():
    with open(r"C:\Users\Usuario\Desktop\Proyecto_final_Musk\PROYECTO-FINAL-MUSK-I-AKI\data\clients.json","r", encoding="utf-8") as archivo_clientes:
        archivo_clientes_dict = json.load(archivo_clientes)
        return archivo_clientes_dict

def leer_datos_ventas():
    with open(r"C:\Users\Usuario\Desktop\Proyecto_final_Musk\PROYECTO-FINAL-MUSK-I-AKI\data\sales.csv", "r", encoding="utf-8") as archivo_ventas:
        archivo_ventas_pd = pd.read_csv(archivo_ventas)
        return archivo_ventas_pd 
 
def numero_de_clientes():
    return len(leer_datos_clientes())

def numero_de_ventas():
    return len(leer_datos_ventas())
          
def total_ingresos_cliente(client_id):
        return sum(leer_datos_ventas()[leer_datos_ventas()["client_id"] == client_id]["amount"])
                
def numero_ventas_cliente(client_id):
    from sales_collection import salestCollection
    return len(salestCollection().sales_by_client(client_id))

def ingreso_promedio_venta_cliente(client_id):
    return total_ingresos_cliente(client_id)/ numero_ventas_cliente(client_id)

def cliente_mayor_gasto_país():
    df_ventas = leer_datos_ventas() #pasamos a dataframe df_ventas
    datos_cliente = {"client_id" : [],  #creamos el diccionario para agrupar por pais e ID
                     "pais" : []
                     }
    for i in leer_datos_clientes(): #Con este bucle recorremos el archivo clients para añadir cada uno de las ID como de los paises a una lista en el diccionario anterior.
        datos_cliente["client_id"].append(i["client_id"])#Vamos añadiendo la ID de cada cliente
        datos_cliente["pais"].append(i["country"])#Vamos añadiendo el pais de cada cliente
    df_datos_cliente = pd.DataFrame(datos_cliente)#Creamos un dataframe con el diccionario que contiene las ID y clientes
    df_suma_por_cliente = df_ventas.groupby("client_id")["amount"].sum()#Agrupamos las ventas por ID y sumamos lo de cada cliente
    df_final = df_datos_cliente.merge(df_suma_por_cliente,on="client_id",how="outer")
    return df_final.set_index("pais")["amount"].to_dict()
    

def total_ventas_categoría():
    return leer_datos_ventas().groupby("category")["amount"].sum()


def cliente_más_ventas_en_una_categoría_específica(categoria):
    filtro_por_categoria = leer_datos_ventas()[leer_datos_ventas()["category"] == categoria]
    suma_total_cliente = filtro_por_categoria.groupby("client_id")["amount"].sum()
    cliente_con_mas_venta_categoria = suma_total_cliente.max()
    id_cliente_con_mas_venta = suma_total_cliente.idxmax()
    datos_cliente_con_mas_venta_categoria = filtro_por_categoria[filtro_por_categoria["client_id"] == id_cliente_con_mas_venta]
    print(f"El cliente con mas ventas en la categoria {categoria} es el cliente con ID {id_cliente_con_mas_venta} y un valor de {cliente_con_mas_venta_categoria}€")
    return datos_cliente_con_mas_venta_categoria
    
def clientes_superan_gasto_mínimo(gasto_minimo):
    suma_ventas_por_cliente = leer_datos_ventas().groupby("client_id")["amount"].sum()
    cantidad_de_clientes = 0
    for i in range(len(suma_ventas_por_cliente)):
        if suma_ventas_por_cliente.iloc[i] > gasto_minimo:
            cantidad_de_clientes +=1
    return cantidad_de_clientes

def ventas_acumuladas_mes_a_mes():
    df_ventas_acumuladas_mes_a_mes = leer_datos_ventas()
    df_ventas_acumuladas_mes_a_mes["date"] = pd.to_datetime(df_ventas_acumuladas_mes_a_mes["date"]).dt.to_period("M")
    df_ventas_acumuladas_mes_a_mes_dict = df_ventas_acumuladas_mes_a_mes.groupby("date")["amount"].sum().to_dict()
    df_final = {str(clave) : valor for clave, valor in df_ventas_acumuladas_mes_a_mes_dict.items()}
    return df_final

def suma_absoluta_ventas():
    return leer_datos_ventas()["amount"].sum()
    print
def mostrar_clientes_caracteristicas():
    clients = []
    for i in range(numero_de_clientes()):
        cliente = {
            "client_id" : leer_datos_clientes()[i]["client_id"],
            "name" : leer_datos_clientes()[i]["name"],
            "total_spent" : total_ingresos_cliente(leer_datos_clientes()[i]["client_id"]),
            "sale_count" : numero_ventas_cliente(leer_datos_clientes()[i]["client_id"]),
            "average_sale" : total_ingresos_cliente(leer_datos_clientes()[i]["client_id"])/ numero_ventas_cliente(leer_datos_clientes()[i]["client_id"])
        }
        clients.append(cliente)
    return clients


def crear_archivo_final():
    archivo_final_dict = {
        "summary" : {"total_clients": numero_de_clientes(), "total_sales" : numero_de_ventas(), "total_revenue" : suma_absoluta_ventas()},
        "clients" : mostrar_clientes_caracteristicas(),
        "top_client_by_country" :cliente_mayor_gasto_país(),
        "sales_by_category" : total_ventas_categoría().to_dict(),
        "high_spending_clients" : clientes_superan_gasto_mínimo(500),
        "monthy_sales" : ventas_acumuladas_mes_a_mes()
        
    }
    return json.dumps(archivo_final_dict, indent = 4)



print(crear_archivo_final())





        
                    
                

                

   
    



    



    
    


