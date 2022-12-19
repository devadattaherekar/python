cricketers=[]

def add_cricketer(name,country):
    cricketers.append({"name":name,"country":country})

def delete_cricketer(name):
    for record in cricketers:
        if record["name"]==name:
            cricketers.remove(record)

def display_cricketers():
    return cricketers