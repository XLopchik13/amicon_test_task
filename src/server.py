import socket
import sys
import os
import struct
import time

CHUNK_SIZE = 4096
ACK_TIMEOUT = 2


def start_udp_server(filename: str, host: str = '0.0.0.0', port: int = 8080):
    """Запускает UDP сервер, который ожидает запрос от клиента и передаёт файл"""
    print(f"Serving {os.path.abspath(filename)}")

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print("Waiting for request...")

        data, client = s.recvfrom(1024)
        if data.decode() != "REQ":
            print("Invalid request")
            return
        s.sendto(b"OK", client)

        with open(filename, 'rb') as f:
            packet_id = 0
            while True:
                chunk = f.read(CHUNK_SIZE)
                is_last = int(chunk == b'')
                header = struct.pack('!IB3s', packet_id, is_last, b'\x00\x00\x00')
                payload = header + chunk

                while True:
                    s.sendto(payload, client)
                    try:
                        s.settimeout(ACK_TIMEOUT)
                        ack, _ = s.recvfrom(1024)
                        ack_id = int(ack.decode().split()[1])
                        if ack_id == packet_id:
                            break
                    except socket.timeout:
                        print(f"Resending packet {packet_id}")
                if is_last:
                    break
                packet_id += 1
        print("Finished.")


if __name__ == "__main__":
    start_udp_server(sys.argv[1])
