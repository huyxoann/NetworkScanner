import scapy.all
from scapy.layers.inet import ICMP, IP


def get_os_using_scapy(ip_address):
    try:
        packet = IP(dst=ip_address) / ICMP()
        reply = scapy.all.sr1(packet, timeout=1, verbose=0)

        if reply:
            if reply.ttl <= 64:
                print(f"{ip_address}: Unix/Linux.")
                return ""
            else:
                print(f"{ip_address}: Windows.")
                return "Window"
        else:
            print(f"No response received from {ip_address}.")
            return ""
    except Exception as e:
        print("Error:", str(e))
