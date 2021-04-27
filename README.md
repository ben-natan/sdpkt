# sdpkt (SendPacket)

A python script using scapy for sending simple TCP or UDP packets.


## Usage 
`python3 sdpkt.py [--tcp] [--udp] [--interval IVAL] -d DST -p PORT` </br>

`python3 sdpkt.py [-t] [-u] [-i IVAL] -d DST -p PORT`</br>

`python3 sdpkt.py -h` for help

## Example
`python3 sdpkt.py -t -d 142.250.179.110 -p 443` sends a TCP SYN packet to google.com on port 443
