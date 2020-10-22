def vul5(packet):
    try:
        if packet['TCP']['payload']==b'250-Nice to meet you.\r\n250-8BITMIME\r\n250-SIZE\r\n250-SMTPUTF8\r\n250-AUTH=CRAM-MD5 PLAIN LOGIN ANONYMOUS\r\n250 AUTH CRAM-MD5 PLAIN LOGIN ANONYMOUS\r\n':
            packet['IP']['addr']=231321
        return packet
    except:
        return None
