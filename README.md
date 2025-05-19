# 💬 Multi-User Socket Chat (with GUI)

This project is a real-time multi-user chat application built with Python's `socket` module and `Tkinter` GUI.  
It supports nickname identification, private messaging, image transmission, message timestamps, user color mapping, and system messages.

---

## 🛠 How to Run

### Server
```bash
python Chat_server.py
```

### Client (Run multiple times for multiple users)
```bash
python gui_client.py
```

---

## ✨ Features

- Multi-client connection using threaded TCP server  
- GUI interface using Tkinter  
- Nickname prompt at client start  
- Whisper/private message using `@nickname`  
- Image transfer with file dialog  
- Timestamps shown on all chat messages  
- System messages for user join/leave  
- Unique color per user in chat view  
- `/users` command to show current nicknames  

---

## 📂 File Structure

| File             | Description                                |
|------------------|--------------------------------------------|
| `Chat_server.py` | Socket-based multi-threaded chat server    |
| `gui_client.py`  | GUI client using Tkinter                   |
| `README.md`      | This documentation                         |

---

# 💬 다중 사용자 소켓 채팅 (GUI 포함)

이 프로젝트는 Python의 `socket`과 `Tkinter`를 이용해 만든 실시간 채팅 프로그램입니다.  
다중 사용자 접속, 닉네임 설정, 귓속말, 이미지 전송, 타임스탬프, 접속자 수 표시, 사용자별 색상 등 다양한 기능을 제공합니다.

---

## 🛠 실행 방법

### 서버 실행
```bash
python Chat_server.py
```

### 클라이언트 실행 (2개 이상 실행 가능)
```bash
python gui_client.py
```

---

## ✨ 주요 기능

- 쓰레드 기반 TCP 서버로 다중 사용자 접속 처리  
- Tkinter 기반의 GUI 채팅 인터페이스  
- 클라이언트 실행 시 닉네임 입력  
- `@닉네임` 형식의 귓속말 기능 지원  
- 파일 선택을 통한 이미지 전송  
- 모든 채팅 메시지에 타임스탬프 자동 추가  
- 입장/퇴장 시 시스템 메시지 표시  
- 사용자별 고유 색상 자동 지정  
- `/users` 명령어로 현재 접속자 목록 확인  

---

## 📂 파일 구조

| 파일명            | 설명                             |
|-------------------|----------------------------------|
| `Chat_server.py`  | 소켓 기반 멀티쓰레드 채팅 서버   |
| `gui_client.py`   | Tkinter 기반 GUI 채팅 클라이언트 |
| `README.md`       | 프로젝트 설명 문서                |
