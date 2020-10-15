Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f2(packet):


    try:
        if packet['IP']['src'] == '172.17.0.3' and  packet['IP']['addr'] == '172.17.0.2':
            print("hhhhhhhhhhhhhhhhhhhhhh11111111111111hhhhhhhhhhhhhhhhhhhhhhh")

            if packet['MYSQL']['command'] == 3 and packet['MYSQL']['query']== "select * from test2.tablaoverwacht":
                print("hhhhhhhhhhhhhhhhhhhhhh222222222222222222222222222hhhhhhhhhhhhhhhhhhhhhhh")

                packet['MYSQL']['query']= "select olaprofe from test2.mitabla"

                print(packet['MYSQL']['query'])
                return packet

    except:
            return None 
