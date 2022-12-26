import json

with open("test_json.json","r") as fp:
    string=fp.read()
    print(type(string))
    json_dict=json.loads(string)
    print(type(json_dict))
    #print(data["myinfo"]["Address"]["City"])
    print(json_dict["myinfo"]["Technologies"]["Skills"])
    for skill in json_dict["myinfo"]["Technologies"]["Skills"]:
        print(skill)
    fp.seek(0) # bring the file pointer to the beginning
    json_dict=json.load(fp)
    json_dict["myinfo"]["First Name"]="Kiran"
    json_dict["myinfo"]["Last Name"]="Purkar"
    json_dict["myinfo"]["Age"]=30
    json_dict["myinfo"]["Technologies"]["Skills"][0] = "Dockers"
    json_dict["myinfo"]["Technologies"]["Skills"][1] = "AWS"
    json_dict["myinfo"]["Technologies"]["Skills"][2] = "Kubernetes"
    print(json_dict)
    #print(type(newdata)) # dictionary
    #print(dir(json))

with open("modified_json.json","w") as ft:
    #json_str=json.dumps(json_dict,indent=4)
    #print(json_str)
    #ft.write(json_str)
    json.dump(json_dict,ft,indent=4)
