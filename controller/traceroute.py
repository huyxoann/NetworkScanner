from scapy.all import *
from scapy.layers.inet import ICMP, IP


def traceroute(target, ttl):
    pkt = IP(dst=target, ttl=ttl) / ICMP()
    reply = sr1(pkt, verbose=False, timeout=5)

    if reply is None:
        result = f"{ttl}. *"
        print(result)
        return result

    elif reply.type == 11:
        result =f"{ttl}. {reply.src} (Intermediate Router)"
        print(result)
        return result
    elif reply.type == 0:
        result =f"{ttl}. {reply.src} (Destination Reached)"
        print(result)
        return result
