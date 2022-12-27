import json

cricketers_file="cricketers.json"

def create_file():
    with open(cricketers_file,"w") as fp:
        json.dump([],fp)

def add_cricketer(name,country):
    list_obj=display_cricketers()
    list_obj.append({"name":name,"country":country})
    with open(cricketers_file,"w") as fp:
           json.dump(list_obj,fp,indent=4)

def delete_cricketer(name):
    all_data=display_cricketers()
    all_data=[each_record for each_record in all_data if each_record['name']!=name ]
    #print(all_data)
    with open(cricketers_file, "w") as fp:
        for each_record in all_data:
            json.dump(all_data,fp,indent=4)

def display_cricketers():
    with open(cricketers_file, "r") as fp:
        return json.load(fp)

