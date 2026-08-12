# Network-packet-analyzer
**Description:**
A basic network packet sniffer built using Python and Sacpy.
The program captures the network packets from the local system and 
displays basic information about each packet.

**Objective:**
The objective of this project is to understand how network traffic is represented and learn how to capture and analyze basic packets.

## Technologies Used
- Python
- Scapy
- Socket Module

## Features
- 1.Captures network packets
- 2.Displays Source IP address
- 3.Displays Destination IP address
- 4.Displays packet size
- 5.Identifies TCP, UDP, and ICMP protocols
- 6.Displays TCP/UDP source and destination ports
- 7.Attempts to resolve IP addresses to hostnames

# How It Works
The program uses Scapy's Sniff() function to capture network packets. each captured Packets id passed to the packet_callback() function for analysis.

The program Checks whether the packets contains an IP layer and then extracts:
- Source IP
- Destination IP
- Packet size
- Hostname
- Protocol
- Source and destination ports for TCP/UDP packets
