# orchestrator.py
# Very small orchestrator that routes messages between agents in demo.
from a2a_protocol import make_msg
import time

class Orchestrator:
    def __init__(self):
        self.messages = []

    def send(self, msg):
        # Append message and print minimal log for demo
        self.messages.append(msg)
        print(f"[ORCH] {time.ctime()} {msg['sender']} -> {msg['receiver']} : {msg['type']}")

    def last_messages(self, n=10):
        return self.messages[-n:]
