#!/usr/bin/env/ python2.7

import scapy.all as scapy


def scan(ip):
    scapy.arping(ip)


scan("10.0.2.1/24")
