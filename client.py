import data_json

def user_add_cricketer():
    name=input("Enter name ")
    country=input("Enter country ")
    data_json.add_cricketer(name, country)


def user_delete_cricketer():
    name=input("Enter name ")
    data_json.delete_cricketer(name)

def user_search_cricketer():
    all_records = data_json.display_cricketers()
    name = input("Enter name ")
    count_records=0
    for each_record in all_records:
        if each_record["name"]==name:
            print(each_record)
            break
        count_records+=1
    if count_records==len(all_records):
        print("Record is not present!")

def user_display_cricketers():
    all_cricketers = data_json.display_cricketers()
    for record in all_cricketers:
        print(f'{record["name"]} plays for {record["country"]}')
        #print(record)

select_choice="""
1. Add Cricketer
2. Delete Cricketer
3. Search Cricketer
4. Display Cricketers
5. Quit
"""

def menu():
    data_json.create_file()
    choice=int(input(select_choice))
    while choice!=5:
        if choice==1:
            user_add_cricketer()
        elif choice==2:
            user_delete_cricketer()
        elif choice==3:
            user_search_cricketer()
        elif choice==4:
            user_display_cricketers()
        else:
            break
        choice=int(input(select_choice))


menu() # function call


