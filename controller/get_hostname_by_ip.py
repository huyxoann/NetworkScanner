import socket
import collections


def get_hostname_by_ip(ip=""):
    temp = ip.split(".")[3]
    if temp == "1":
        return "Router"
    try:
        hostname = socket.gethostbyaddr(ip)[0]

        return hostname
    except socket.herror:
        return "Generic"
