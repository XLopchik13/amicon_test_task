import socket
import sys

CHUNK_SIZE = 4096


def request_udp_file(save_as: str, server_ip: str = '127.0.0.1', port: int = 8080):
    """Отправляет запрос UDP серверу, принимает и сохраняет файл"""
    print(f"Requesting from {server_ip}:{port}")

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        s.sendto(b"REQ", (server_ip, port))

        filename, _ = s.recvfrom(1024)
        print("Downloading...")

        with open(save_as, 'wb') as f:
            while True:
                try:
                    chunk, _ = s.recvfrom(CHUNK_SIZE)
                    if chunk == b"EOF":
                        break
                    f.write(chunk)
                except socket.timeout:
                    print("Timeout: missing packets")
                    break

    print(f"Downloaded as {save_as}")


if __name__ == "__main__":
    request_udp_file(sys.argv[1])
