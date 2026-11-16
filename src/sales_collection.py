import pandas as pd

class Sales_Collection:
    def __init__(self):
        with open(r"C:\Users\Usuario\Desktop\Proyecto_final_Musk\PROYECTO-FINAL-MUSK-I-AKI\data\sales.csv", "r", encoding="utf-8") as archivo:
            self.lista_ventas = pd.read_csv(archivo, index_col= False)

    def sales_by_client(self,client_id):
        ventas_cliente_selecciado = self.lista_ventas[self.lista_ventas["client_id"] == client_id]
        return ventas_cliente_selecciado

    def total_amount_by_client(self,client_id):
        ventas_cliente_selecciado = self.lista_ventas[self.lista_ventas["client_id"] == client_id]
        print(ventas_cliente_selecciado["amount"].sum())

    def total_amount_by_category(self,category):
        ventas_categoria_Seleccionada = self.lista_ventas[self.lista_ventas["category"] == category]
        print(ventas_categoria_Seleccionada["amount"].sum())

    def average_sale_by_client(self,client_id):
        ventas_cliente_selecciado = self.lista_ventas[self.lista_ventas["client_id"] == client_id]
        print(ventas_cliente_selecciado["amount"].describe()["mean"])

