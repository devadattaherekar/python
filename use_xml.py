import xmltodict

with open("test_xml.xml","r") as fp:
    str_data=fp.read()
    #print(dir(xmltodict))
    xml_dict=xmltodict.parse(str_data)
    print(type(xml_dict))
    print(xml_dict["myinfo"]["Address"]["City"])
    xml_dict["myinfo"]["Address"]["City"]="Bangalore"
    xml_dict["myinfo"]["First_Name"]="Kiran"
    xml_dict["myinfo"]["Technologies"]["Skills"][0] = "Dockers"
    xml_dict["myinfo"]["Technologies"]["Skills"][1] = "AWS"
    xml_dict["myinfo"]["Technologies"]["Skills"][2] = "Kubernetes"

with open("modified_test_xml.xml","w") as ft:
    xml_str=xmltodict.unparse(xml_dict,pretty=True)
    ft.write(xml_str)