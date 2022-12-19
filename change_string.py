import sys

print("Name of the script is ",sys.argv[0])

if len(sys.argv)!=3:
    print("This script works with only 2 arguments")
    print("First argument has to be string")
    print("Second argument has to be action to be performed")
    print("Actions are upper/lower/title/capitalize/swapcase")
    sys.exit(-1)
else:
    #print("First argument is ",sys.argv[1])
    user_string=sys.argv[1]
    #print("Second argument is ",sys.argv[2])
    string_operation=sys.argv[2]
    #print("Total number of args is",len(sys.argv))
    if string_operation=="upper":
        print(user_string.upper())
    elif string_operation=="lower":
        print(user_string.lower())
    elif string_operation == "title":
        print(user_string.title())
    elif string_operation == "capitalize":
        print(user_string.capitalize())
    elif string_operation == "swapcase":
        print(user_string.swapcase())
    else:
        print("invalid action kindly use upper/lower/title/capitalize/swapcase only ")
        sys.exit(2)

    sys.exit(0)
