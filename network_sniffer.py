import socket #socket is an interface to communicate with network tarffic
from scapy.all import sniff #scapy is a network traffic captring library
from scapy.layers.inet import IP, TCP, UDP, ICMP #import IP, TCP, UDP, ICMP these ar used to captre source adres

def packet_callback(packet): # call back function for source and destination IP
    if packet.haslayer(IP):
        sc_ip = packet[IP].src
        dst_ip = packet[IP].dst
        size = len(packet)
        try: #try statemnt will used to find source and destination name
            sc_name = socket.gethostbyaddr(sc_ip)[0]

        except:#except statement is used handle error
            sc_name = "Unknown"

        try:
            dst_name = socket.gethostbyaddr(dst_ip)[0]
        except:
            dst_name = "Unknown"

        print("Source IP:", sc_ip, "(", sc_name, ")")
        print("Destination IP:", dst_ip, "(", dst_name, ")")
        print("Packet Size:", size, "bytes")

        if packet.haslayer(TCP): #condition will caheck TCP address is available
            print("Protocol: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)
        elif packet.haslayer(UDP):#condition will caheck UDP address is available
            print("Protocol: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)
        elif packet.haslayer(ICMP):#condition will caheck ICMP address is available
            print("Protocol: ICMP")
            print("Source Port:", packet[ICMP].sport)
            print("Destination Port:", packet[ICMP].dport)

        else: #condition will print other if sours not found
            print("Protocol: Other")

        print("-" * 50) #used print the symbol after evry ip address shown
sniff(prn=packet_callback, count=25) # capture 25 packet
