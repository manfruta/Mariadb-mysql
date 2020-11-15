Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f1(packet):

    import time as tiempito
    if (packet['TCP']['dstport'] == 3306):
        try:
            time= int(tiempito.time())
            try:
                packet.mapa[time] = (packet['IP']['len']*8) + 14 + packet.mapa[time]

            except:
                packet.mapa[time] = (packet['IP']['len']*8) + 14
            print (packet.map)
        except:
            map = {}
            packet.global_var('mapaayuda',map)
            packet.mapaayuda[time] = (packet['IP']['len']*8) + 14
            print (packet.mapaayuda)
    return packet
