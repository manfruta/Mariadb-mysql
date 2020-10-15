Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f1(packet):
    try:
        if packet['IP']['src'] == '172.17.0.3' and packet['IP']['addr'] == '172.17.0.2' and packet['IP']['proto'] == 6:
            print("-------0-------")
            if packet['MYSQL']['command'] == 3 and packet['MYSQL']['query']== "select * from test2.tablalol":
                print("-------------1-----------------")

                packet['MYSQL']['query']="select r from test2.tablalol"
                print("cambiaso con el rakan"+packet['MYSQL']['query'])
                return packet



    except:
            return None
