Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f4(packet):
    try:
        if packet['IP']['src'] == '172.17.0.2' and packet['IP']['addr'] == '172.17.0.3' and packet['IP']['proto'] == 6:
            print("--------------11111111111111111111111111111-------------------")
            if packet['MYSQL']['packet_number'] == 2 and packet['MYSQL']['packet_length'] == 7:
                print("--------------2222222222222222222-------------------")

                packet['MYSQL']['response_code']= '0xff'
                print(packet['MYSQL']['response_code'])
                return packet

    except:
            return None
