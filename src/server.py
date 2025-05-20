import socket
import sys
import os

CHUNK_SIZE = 4096


def start_udp_server(filename: str, host: str = '0.0.0.0', port: int = 8080):
    print(f"Serving {os.path.abspath(filename)}")

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print("Waiting for request...")

        data, client_address = s.recvfrom(1024)
        if data.decode() != "REQ":
            print("Invalid request")
            return

        print(f"Request from {client_address}")
        s.sendto(os.path.basename(filename).encode(), client_address)

        with open(filename, 'rb') as f:
            print("Sending...")
            while chunk := f.read(CHUNK_SIZE):
                s.sendto(chunk, client_address)

        s.sendto(b"EOF", client_address)
        print(f"Finished sending to {client_address}")


if __name__ == "__main__":
    start_udp_server(sys.argv[1])
