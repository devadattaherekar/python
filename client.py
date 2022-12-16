import data

def user_add_cricketer():
    name=input("Enter name ")
    country=input("Enter country ")
    data.add_cricketer(name,country)

def user_delete_cricketer():
    pass

def user_search_cricketer():
    pass

def user_display_cricketers():
    all_cricketers=data.display_cricketers()
    for record in all_cricketers:
        print(f'{record["name"]} plays for {record["country"]}')


select_choice="""
1. Add Cricketer
2. Delete Cricketer
3. Search Cricketer
4. Display Cricketers
5. Quit
"""

def menu():
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


