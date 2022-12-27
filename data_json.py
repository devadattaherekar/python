import json

cricketers_file="cricketers.json"

def create_file():
    with open(cricketers_file,"w") as fp:
        json.dump({},fp)

def add_cricketer(name,country):
    list_obj=display_cricketers()
    list_obj.append({"name":name,"country":country})
    with open(cricketers_file,"w") as fp:
        for record in list_obj:
           json.dump(record,fp,indent=4)

def delete_cricketer(name):
    pass
    """
    all_data=display_cricketers()
    all_data=[each_record for each_record in all_data if each_record['name']!=name ]
    #print(all_data)
    with open(cricketers_file, "w",newline="") as fp:
        data=csv.writer(fp)
        for each_record in all_data:
            data.writerow([each_record['name'],each_record['country']])
    """

def display_cricketers():
    with open(cricketers_file, "r") as fp:
        record=json.load(fp)
        return [record]
        #data=csv.reader(fp)
        #return [{"name":each_row[0],"country":each_row[1]} for each_row in data]
