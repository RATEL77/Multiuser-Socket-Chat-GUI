import socketserver
import threading

clients = {}  # socket: nickname
lock = threading.Lock()

def broadcast(message, exclude=None):
    with lock:
        for sock in clients:
            if sock != exclude:
                try:
                    sock.send(message.encode())
                except:
                    pass

def update_user_count():
    msg = f"[시스템] 현재 접속자 수: {len(clients)}명"
    broadcast(msg)

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.nickname = self.request.recv(1024).decode()
        with lock:
            clients[self.request] = self.nickname
        broadcast(f"[시스템] {self.nickname} 님이 입장했습니다.")
        update_user_count()

        try:
            while True:
                data = self.request.recv(4096)
                if not data:
                    break

                if data.startswith(b"[IMAGE]"):
                    filename = self.request.recv(1024).decode()
                    image_data = self.request.recv(65536)
                    broadcast(f"[{self.nickname}] 이미지 수신: {filename}", exclude=self.request)
                    continue

                msg = data.decode()

                if msg.strip() == "/users":
                    nick_list = ', '.join(clients.values())
                    self.request.send(f"[시스템] 현재 접속자: {nick_list}".encode())
                    continue

                if msg.startswith("@"):
                    try:
                        to_nick, message = msg[1:].split(" ", 1)
                        for sock, nick in clients.items():
                            if nick == to_nick:
                                sock.send(f"[귓속말] {self.nickname}: {message}".encode())
                                break
                    except:
                        self.request.send("[시스템] 귓속말 형식 오류. 예: @닉네임 내용".encode())
                else:
                    broadcast(f"[{self.nickname}] {msg}", exclude=self.request)
        finally:
            with lock:
                del clients[self.request]
            broadcast(f"[시스템] {self.nickname} 님이 퇴장했습니다.")
            update_user_count()

if __name__ == "__main__":
    HOST, PORT = '', 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTcpHandler)
    print("서버 시작 (기능 통합 버전)")
    server.serve_forever()
