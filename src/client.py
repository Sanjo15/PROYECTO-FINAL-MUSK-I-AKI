import json

class Cliente():
    def __init__(self, client_id, name, country, signup_date):
        self.client_id = client_id
        self.name = name
        self.country = country
        self.signup_date = signup_date
        
    def to_dict(self):
        nuevo_cliente = { "id_cliente" : self.client_id, "name" : self.name, "country" : self.country, "signup_date" : self.signup_date}
        with open (r"C:\Users\Usuario\Desktop\Proyecto_final_Musk\PROYECTO-FINAL-MUSK-I-AKI\data\clients.json", "r", encoding="utf-8") as f:
            clientes_dict = json.load(f)
            clientes_dict.append(nuevo_cliente)
        with open(r"C:\Users\Usuario\Desktop\Proyecto_final_Musk\PROYECTO-FINAL-MUSK-I-AKI\data\clients.json", "w", encoding="utf-8") as f:
            json.dump(clientes_dict,f,indent=4)
            

