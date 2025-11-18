# memory_bank.py
# In-memory memory bank for demo. For production use persistent storage.
import json, os
class MemoryBank:
    def __init__(self, filepath=None):
        self.filepath = filepath
        if filepath and os.path.exists(filepath):
            with open(filepath,'r') as f:
                self.store = json.load(f)
        else:
            self.store = {}

    def get(self, user_id):
        return self.store.get(user_id, {"weak_topics":{}, "history":[]})

    def update_weakness(self, user_id, topic, score):
        usr = self.store.setdefault(user_id, {"weak_topics":{}, "history":[]})
        prev = usr["weak_topics"].get(topic, {"count":0, "avg":0.0})
        cnt = prev["count"] + 1
        avg = (prev["avg"]*prev["count"] + score)/cnt
        usr["weak_topics"][topic] = {"count":cnt, "avg":avg}

    def add_history(self, user_id, record):
        usr = self.store.setdefault(user_id, {"weak_topics":{}, "history":[]})
        usr["history"].append(record)

    def save(self):
        if not self.filepath:
            return
        with open(self.filepath,'w') as f:
            json.dump(self.store, f, indent=2)
