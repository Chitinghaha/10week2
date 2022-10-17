import json
import yaml
import datetime

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
        with open('inventories.json', 'w') as file:
            json.dump(data, file)
        file.close()

        # record yaml
        recording = {'name': data[buy_doc]['name'], 'price': data[buy_doc]['price'], 'time': datetime.datetime.now()}
        recording_list = []
        recording_list.append(recording)

        with open('history.yaml', 'a') as file:
            yaml.dump(recording_list, file)
        file.close()

        f.close()


money = int(input('輸入金額'))
valid_doc(money)
buy_doc = int(input('輸入商品編號'))
output(buy_doc)

