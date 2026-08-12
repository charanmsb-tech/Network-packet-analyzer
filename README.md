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

  ## How to Install

Before running the Network Packet Analyzer, make sure Python is installed on your system. Python is required to execute the program and Scapy is used for capturing and analyzing network packets.

### Step 1: Install Python

Download and install Python from the official Python website. During installation, make sure to enable the **"Add Python to PATH"** option.

### Step 2: Install Scapy

Open Command Prompt or Terminal in you system and install the Scapy library using:
```bash
**pip install scapy**

## How to run
After installing Python and Scapy, download or clone this repository to your system.

Open the project folder in Command Prompt, Terminal, or VS Code.

Run the Python program using:

```bash
python network_sniffer.py
