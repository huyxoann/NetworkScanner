import socket


def find_service_by_port(port):
    try:
        service = socket.getservbyport(port)
        return service
    except OSError:
        return "Unknown"


def find_open_ports_with_service(hostname, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            result = s.connect_ex((hostname, port))

            if result == 0:
                service = find_service_by_port(port)
                open_ports.append((port, service))

    return open_ports


def open_ports_with_service(target, start_port, end_port):
    ports = []
    open_ports_with_service = find_open_ports_with_service(target, start_port, end_port)
    if open_ports_with_service:
        for port, service in open_ports_with_service:
            ports.append([port, service])

    return ports
