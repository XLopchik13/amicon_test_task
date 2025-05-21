import socket
import sys


def request_tcp_file(save_as: str, server_ip: str = '127.0.0.1', port: int = 8080):
    """Запрашивает файл у TCP сервера и сохраняет его на диск"""
    print(f"Requesting from {server_ip}:{port}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        filename = b""
        while True:
            ch = s.recv(1)
            if ch == b'\n':
                break
            filename += ch
        print("Downloading...")
        with open(save_as, 'wb') as f:
            while chunk := s.recv(4096):
                f.write(chunk)
    print(f"Downloaded as {save_as}")


if __name__ == "__main__":
    request_tcp_file(sys.argv[1])
