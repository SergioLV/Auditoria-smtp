def vul4(packet):
    try:
        if packet['TCP']['payload']==b'quit\r\n':
            packet['IP']['addr']=231321
        return packet
    except:
        return None

