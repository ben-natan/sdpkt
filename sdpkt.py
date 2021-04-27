from scapy.all import *
import argparse
# import os
import time

parser = argparse.ArgumentParser(description='Send TCP/UDP packets')

parser.add_argument('-t', '--tcp', action='store_true')
parser.add_argument('-u', '--udp', action='store_true')
parser.add_argument('-i', '--interval', type=float, default=0.5)
parser.add_argument('-d', '--dst', type=str, required=True)
parser.add_argument('-p', '--port', type=int ,required=True)

args = parser.parse_args()

ip = args.dst
port = args.port
interval = args.interval


if (args.tcp):
    print("Sending SYN TCP packets to " + ip + " every " + str(interval) + "s.")
    while 1:
        send(IP(dst=ip)/TCP(dport=port, flags='S'))
        time.sleep(interval)


if (args.udp):
    print("Sending UDP packets to " + ip + " every " + str(interval) + "s.") 
    while 1:
        send(IP(dst=ip)/UDP(dport=port)/Raw(load="123"))
        time.sleep(interval)