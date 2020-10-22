def vul1(packet):
    import re
    try:
        pattern = re.compile('size=')
        if packet['TCP']['payload']:
            comand = packet['TCP']['payload']
            match = re.search(pattern,str(comand))
            if match:
                packet['TCP']['payload']=b'221 Goodbye\r\n'
        return packet
    except:
        return None

