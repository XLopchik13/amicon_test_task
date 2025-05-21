import socket
import sys
import struct

CHUNK_SIZE = 4096


def request_udp_file(save_as: str, server_ip: str = '127.0.0.1', port: int = 8080):
    """Отправляет запрос UDP серверу, принимает и сохраняет файл"""
    print(f"Requesting from {server_ip}:{port}")

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"REQ", (server_ip, port))
        resp, _ = s.recvfrom(1024)
        if resp != b"OK":
            print("Server not ready")
            return

        with open(save_as, 'wb') as f:
            while True:
                data, server = s.recvfrom(CHUNK_SIZE + 8)
                header = data[:8]
                chunk = data[8:]

                packet_id, is_last, _ = struct.unpack('!IB3s', header)
                s.sendto(f"ACK {packet_id}".encode(), server)
                f.write(chunk)

                if is_last == 1:
                    break

    print(f"Downloaded as {save_as}")


if __name__ == "__main__":
    request_udp_file(sys.argv[1])
