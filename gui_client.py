import socket
import threading
import tkinter as tk
from tkinter import simpledialog, filedialog
import time

HOST = 'localhost'
PORT = 9999

USER_COLORS = [
    "DarkRed", "DarkGreen", "DarkBlue", "Teal", "SlateBlue",
    "SaddleBrown", "DarkOrange", "Purple", "SeaGreen", "Tomato"
]
user_color_map = {}

def get_color(nickname):
    if nickname not in user_color_map:
        color = USER_COLORS[hash(nickname) % len(USER_COLORS)]
        user_color_map[nickname] = color
    return user_color_map[nickname]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

nickname = simpledialog.askstring("닉네임 설정", "사용할 닉네임을 입력하세요")
client_socket.send(nickname.encode())

def receive():
    while True:
        try:
            msg = client_socket.recv(4096).decode()
            timestamp = time.strftime("%H:%M:%S")
            display_msg = f"[{timestamp}] {msg}"

            if "귓속말" in msg:
                tag = "whisper"
            elif msg.startswith("[시스템]"):
                tag = "system"
            else:
                sender = msg.split("]")[0].strip("[").split(" ")[0]
                tag = f"user_{sender}"
                if not chat_log.tag_names().__contains__(tag):
                    chat_log.tag_config(tag, foreground=get_color(sender))

            chat_log.insert(tk.END, display_msg + "\n", tag)
            chat_log.see(tk.END)
        except:
            break

def send():
    msg = msg_entry.get()
    if msg:
        client_socket.send(msg.encode())
        timestamp = time.strftime("%H:%M:%S")
        display_msg = f"[{timestamp}] me ({nickname}): {msg}"
        chat_log.insert(tk.END, display_msg + "\n", "me")
        chat_log.see(tk.END)
        msg_entry.delete(0, tk.END)

def send_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if path:
        try:
            with open(path, "rb") as f:
                image_data = f.read()
            filename = path.split("/")[-1]
            client_socket.send(b"[IMAGE]")
            client_socket.send(filename.encode())
            client_socket.send(image_data)
            chat_log.insert(tk.END, f"\n[이미지 전송] {filename}")
            chat_log.see(tk.END)
        except Exception as e:
            chat_log.insert(tk.END, f"\n[오류] 이미지 전송 실패: {e}")
            chat_log.see(tk.END)

root = tk.Tk()
root.title(f"채팅 클라이언트 - {nickname}")

chat_log = tk.Text(root, height=20, width=50)
chat_log.pack()

chat_log.tag_config("whisper", foreground="DarkOrchid")
chat_log.tag_config("system", foreground="Gray", font="맑은고딕 9 italic")
chat_log.tag_config("me", foreground="black", font="맑은고딕 10 bold")

msg_entry = tk.Entry(root, width=40)
msg_entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(root, text="전송", command=send)
send_button.pack(side=tk.LEFT)

image_button = tk.Button(root, text="이미지 전송", command=send_image)
image_button.pack(side=tk.RIGHT)

threading.Thread(target=receive, daemon=True).start()
root.mainloop()
