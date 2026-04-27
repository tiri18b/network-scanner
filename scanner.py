import socket
from datetime import datetime

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    135: "RPC",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    1433: "MSSQL",
    3389: "RDP",
}

def scan_host(ip: str, ports: dict[int, str], timeout: float = 0.5) -> list[str]:
    open_ports = []
    for port, service in ports.items():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(f"{port}/{service}")
    return open_ports

def main():
    subnet = input("Enter subnet prefix, example 192.168.10.: ").strip()
    start = int(input("Start host number: ").strip() or "1")
    end = int(input("End host number: ").strip() or "254")

    print(f"\nScan started: {datetime.now()}\n")
    for host in range(start, end + 1):
        ip = f"{subnet}{host}"
        found = scan_host(ip, COMMON_PORTS)
        if found:
            print(f"[OPEN] {ip} -> {', '.join(found)}")

if __name__ == "__main__":
    main()
