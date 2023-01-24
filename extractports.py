import re

def extract_ips_ports(text):
    ip_pattern = "Nmap scan report for (.*)"
    port_pattern = "^(\d+)"
    ips_ports = {}
    for line in text.split("\n"):
        ip_match = re.match(ip_pattern, line)
        if ip_match:
            ip = ip_match.group(1)
            ports = []
            continue
        port_match = re.match(port_pattern, line)
        if port_match:
            port = port_match.group(1).replace("/tcp", "").replace("/udp", "")
            ports.append(port)
        if not line.strip():
            ips_ports[ip] = ports
    return ips_ports

def main():
    with open('nmapoutput.txt', 'r') as f:
        text = f.read()
        ips_ports = extract_ips_ports(text)
    with open('extract.txt', 'w') as f:
        for ip, ports in ips_ports.items():
            ports_str = ",".join(ports)
            f.write(f"{ip} {ports_str}\n")
            print(f"{ip} {ports_str}")

if __name__ == '__main__':
    main()
