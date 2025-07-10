import time
import random
from datetime import datetime

levels = ["INFO", "WARNING", "ERROR"]
users = ["alice", "bob", "charlie"]
ips = ["192.168.1.1", "10.0.0.5", "172.16.0.2"]

messages = [
    "User logged in successfully",
    "Failed login attempt",
    "Connection reset by peer",
    "Disk quota exceeded",
    "Unexpected input received"
]

with open("test.log", "a") as f:
    while True:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level = random.choice(levels)
        user = random.choice(users)
        ip = random.choice(ips)
        message = random.choice(messages)

        line = f"{ts} {level} User: {user} IP: {ip} {message}\n"
        f.write(line)
        f.flush()
        time.sleep(1)
