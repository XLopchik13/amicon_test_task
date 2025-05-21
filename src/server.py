import socket
import sys
import os


def start_tcp_server(filename: str, host: str = '0.0.0.0', port: int = 8080):
    """Запускает TCP сервер, который принимает входящие соединения и передаёт указанный файл"""
    print(f"Serving {os.path.abspath(filename)}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print(f"Request from {addr}")
            conn.sendall(os.path.basename(filename).encode() + b'\n')
            with open(filename, 'rb') as f:
                print("Sending...")
                while chunk := f.read(4096):
                    conn.sendall(chunk)
            print(f"Finished sending to {addr}")


if __name__ == "__main__":
    start_tcp_server(sys.argv[1])
