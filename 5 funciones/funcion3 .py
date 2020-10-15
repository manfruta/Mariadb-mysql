Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f3(packet):
    try:

        if  packet['TCP']['dstport'] == 3306 and packet['IP']['src'] == '172.17.0.3' and  packet['IP']['addr'] == '172.17.0.2':
            print("aaaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111111aaaaaaaaaaaaaaaaaaaaaaa")

            if packet['MYSQL']['command'] == 3 and packet['MYSQL']['query']== "select * from test2.tablaoverwacht":

                print("aaaaaaaaaaaaaaaaaaaaaaaaaww222222222222222222222222222222222222aaaaaaaaaaaaaaaaaaaaaaa")

                packet['MYSQL']['query']= "DELETE FROM tablalol WHERE id = 10"

                print(packet['MYSQL']['packet_length'])

                print(packet['MYSQL']['query'])
                return packet

    except:

            return None
