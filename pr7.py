import socket
import sys

HOST, TCP_PORT, UDP_PORT = '127.0.0.1', 12345, 12346
MSG = "Hello, Server! This is the {} Client."


def run_tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, TCP_PORT))
    s.listen(1)

    print("\n[TCP] Server listening...")
    c, addr = s.accept()

    print(f"[TCP] Connected by {addr}")
    print(f"[TCP] Client says: {c.recv(1024).decode()}")

    c.send(b"Message received loud and clear!")
    c.close()
    s.close()


def run_tcp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, TCP_PORT))

    s.send(MSG.format("TCP").encode())
    print("\n[TCP] Sent client message")
    print(f"[TCP] Server says: {s.recv(1024).decode()}")

    s.close()


def run_udp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, UDP_PORT))

    print("\n[UDP] Server listening...")
    data, addr = s.recvfrom(1024)

    print(f"[UDP] Received from {addr}: {data.decode()}")
    s.sendto(b"Got your UDP packet!", addr)

    s.close()


def run_udp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.sendto(MSG.format("UDP").encode(), (HOST, UDP_PORT))
    print("\n[UDP] Sent packet")

    data, addr = s.recvfrom(1024)
    print(f"[UDP] Server says: {data.decode()}")

    s.close()


if __name__ == "__main__":
    print(
        "=== Computer Networks Lab: Experiment 7 ===\n"
        "1. TCP Server\n"
        "2. TCP Client\n"
        "3. UDP Server\n"
        "4. UDP Client\n"
        "5. Exit"
    )

    choice = input("\nEnter choice (1-5): ")

    funcs = {
        '1': run_tcp_server,
        '2': run_tcp_client,
        '3': run_udp_server,
        '4': run_udp_client
    }

    if choice in funcs:
        funcs[choice]()
    elif choice == '5':
        sys.exit(0)
    else:
        print("Invalid choice.")
