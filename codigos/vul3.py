def vul2(packet):
    try:
        if packet['TCP']['payload']==b'rcpt TO:<to@example.com>\r\n':
             packet['TCP']['payload']=b'rcpt TO:<from@example.com>\r\n'
             return packet
    except:
        return None
