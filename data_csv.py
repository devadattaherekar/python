import csv

cricketers_file="cricketers.csv"

def create_file():
    with open(cricketers_file,"w") as fp:
        pass

def add_cricketer(name,country):
    with open(cricketers_file,"a",newline="") as fp:
        data=csv.writer(fp)
        data.writerow([name,country])

def delete_cricketer(name):
    all_data=display_cricketers()
    all_data=[each_record for each_record in all_data if each_record['name']!=name ]
    #print(all_data)
    with open(cricketers_file, "w",newline="") as fp:
        data=csv.writer(fp)
        for each_record in all_data:
            data.writerow([each_record['name'],each_record['country']])


def display_cricketers():
    with open(cricketers_file, "r") as fp:
        data=csv.reader(fp)
        return [{"name":each_row[0],"country":each_row[1]} for each_row in data]
