import yaml

with open("test_yaml.yaml","r") as fp:
    str_data=fp.read()
    yaml_dict=yaml.load(str_data,Loader=yaml.FullLoader)
    print(type(yaml_dict))
    print(yaml_dict["myinfo"]["Address"]["City"])
    yaml_dict["myinfo"]["Address"]["City"]="Bangalore"
    yaml_dict["myinfo"]["First Name"]="Kiran"
    yaml_dict["myinfo"]["Technologies"]["Skills"][0] = "Dockers"
    yaml_dict["myinfo"]["Technologies"]["Skills"][1] = "AWS"
    yaml_dict["myinfo"]["Technologies"]["Skills"][2] = "Kubernetes"
    #print(dir(yaml))

with open("modified_test_yaml.yaml","w") as ft:
    yaml.dump(yaml_dict,ft)
