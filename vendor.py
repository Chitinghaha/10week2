import json
import yaml
import datetime



class Inventory:
    def __init__(self,number):
        self.number=number
        
    def open_json(self):
        with open('inventories.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
        
    def reload_json(self,data):
        with open('inventories.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)
        file.close()
        
    def record_yaml(self,recording):
        with open('history.yaml', 'w', encoding='utf-8') as file:
            yaml.dump(recording, file)
        file.close()

    
        
class UI:
    def __init__(self):
        pass
    
    def output_doc(self,data,i):
        print("name:" + i['name'])
        print("price:" + str(i['price']))
        print("number:" + str(i['number']) +'\n')
        
        
    def output_mon(self,money,data,buy_doc):
        print('找零' + str(money - data[buy_doc]['price']))
        
        
    def input_mon(self):
        money = int(input('輸入金額'))
        return money
    
    def input_doc(self):
        buy_doc = int(input('輸入商品編號'))
        return buy_doc
        



class Vendor:
    def __init__(self):
        pass
    
    def  operate(self):
        money = UI.input_mon(self)
        data = Inventory.open_json(self)
        
        # output product
        for i in data:
            if (money >= i['price']) & (i['number'] > 0):
               UI.output_doc(self,data,i)
        
        buy_doc=UI.input_doc(self)
        
        # output money
        UI.output_mon(self,money,data,buy_doc)
        
        # reload json
        data[buy_doc]['number'] = data[buy_doc]['number'] - 1
        Inventory.reload_json(self,data)
        
        # record yaml
        recording = {'name': data[buy_doc]['name'], 'price': data[buy_doc]['price'], 'time': datetime.datetime.now()}
        Inventory.record_yaml(self,recording)
        


myVendor = Vendor()
myVendor.operate()

        
        
"""

def valid_doc(money):
    with open('inventories.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # output product
    for i in data:
        if (money >= i['price']) & (i['number'] > 0):
            print("name:" + i['name'])
            print("price:" + str(i['price']))
            print("number:" + str(i['number']) +'\n')

    f.close()

def output(buy_doc):
    with open('inventories.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        # output money
        print('找零' + str(money - data[buy_doc]['price']))

        # reload json
        data[buy_doc]['number'] = data[buy_doc]['number'] - 1
        with open('inventories.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)
        file.close()

        # record yaml
        recording = {'name': data[buy_doc]['name'], 'price': data[buy_doc]['price'], 'time': datetime.datetime.now()}

        with open('history.yaml', 'w', encoding='utf-8') as file:
            yaml.dump(recording, file)
        file.close()

        f.close()


money = int(input('輸入金額'))
valid_doc(money)
buy_doc = int(input('輸入商品編號'))
output(buy_doc)
"""



