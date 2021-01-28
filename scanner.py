#!/usr/bin/env/ python2.7

import scapy.all as scapy


def scan(ip):
    # scapy.arping(ip)

    # create arp packets
    arp_request = scapy.ARP()
    arp_request.pdst = ip
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # print(arp_request.summary())
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    print (arp_request_broadcast.summary())
    arp_request_broadcast.show()
    # scapy.ls(scapy.ARP()) # reveals all the fields that can be set in the scapy.ARP Class
    # scapy.ls(scapy.Ether()) # reveals all the fields that can be set in the scapy.Ether Class
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print (answered.summary())


scan("10.0.2.1/24")
