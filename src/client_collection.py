import json

class Client_Collection:
    def __init__(self):
        with open (r"C:\Users\Usuario\Desktop\Proyecto_final_Musk\PROYECTO-FINAL-MUSK-I-AKI\data\clients.json", "r", encoding="utf-8") as f:
            self.clientes_dict = json.load(f)
    def get_client_by_id(self,client_id):
            for i in self.clientes_dict:
                if client_id == i["client_id"]:
                    print(i)
    def clients_by_country(self, country):
         for i in self.clientes_dict:
              if country == i["country"]:
                   print(i)

 