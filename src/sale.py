import pandas as pd

class Sale():
    def __init__(self, sale_id, client_id, product, category, amount, date):
        self.sale_id = sale_id
        self.client_id = client_id
        self.product = product
        self.category = category
        self.amount = amount
        self.date = date

    def to_dict(self):
        nuevo_sale = pd.DataFrame({"sale_id" : [self.sale_id], "client_id" : [self.client_id], "product" : [self.product], "category" : [self.category], "amount" :  [self.amount], "date" : [self.date]})
        with open(r"C:\Users\Usuario\Desktop\Proyecto_final_Musk\PROYECTO-FINAL-MUSK-I-AKI\data\sales.csv", "r", encoding="utf-8") as archivo:
            lista_ventas = pd.read_csv(archivo)
        lista_ventas = pd.concat([lista_ventas,nuevo_sale], axis=0,ignore_index=True)
        print(lista_ventas)
        with open(r"C:\Users\Usuario\Desktop\Proyecto_final_Musk\PROYECTO-FINAL-MUSK-I-AKI\data\sales.csv", "w", encoding="utf-8") as archivo:
            lista_ventas.to_csv(archivo, index=False)
        print(lista_ventas)
        




      

