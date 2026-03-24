import socket

target = input("Enter target (domain or IP): ")

try:
    target_ip = socket.gethostbyname(target)
except:
    print("Invalid target ")
    exit()

print(f"\nScanning Target: {target_ip}")
print("Scanning ports...\n")

start = int(input("Enter start port: "))
end = int(input("Enter end port: "))

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("\nScan Completed ")
input("Press Enter to exit...")

