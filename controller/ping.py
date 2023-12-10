import time

import scapy.all as scapy


def ping_to_device(ip):
    packet = scapy.IP(dst=ip) / scapy.ICMP()  # Tạo gói tin ICMP Echo Request

    try:
        sent_time = time.time()
        reply = scapy.sr1(packet, timeout=5, verbose=False)  # Gửi và nhận phản hồi
        received_time = time.time()
        if reply:
            print(f"Reply from {reply.src}: bytes={len(reply)}, time={(received_time - sent_time) * 1000:.2f} ms")
            return [reply.src, len(reply), (received_time - sent_time) * 1000]
        else:
            return []
    except Exception as e:
        print(f"Error: {str(e)}")

    time.sleep(1)


