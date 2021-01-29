#!/usr/bin/env/ python2.7

import scapy.all as scapy
import optparse


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP/IP Range")
    options, argument = parser.parse_args()
    return options


def scan(ip):
    # scapy.arping(ip)
    # create arp packets
    arp_request = scapy.ARP()
    arp_request.pdst = ip
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # print(arp_request.summary())
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    # print (arp_request_broadcast.summary())
    arp_request_broadcast.show()
    # scapy.ls(scapy.ARP()) # reveals all the fields that can be set in the scapy.ARP Class
    # scapy.ls(scapy.Ether()) # reveals all the fields that can be set in the scapy.Ether Class
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    # answered = scapy.srp(arp_request_broadcast, timeout=1)[0]
    # print (unanswered.summary())
    client_list = []
    for element in answered_list:
        # print (element[1].show())
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def display_result(responses):

    print("IP \t\t\tMac Address \n-----------------------------------------------------------------------------")
    for element in responses:

        print (element["ip"] + "\t\t" + element["mac"])
        print ("-----------------------------------------------------------------------------")
    # print (client_list)


options = get_argument()
display_result(scan(options.target))
