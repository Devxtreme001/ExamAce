# a2a_protocol.py
# Simple A2A message builder used by orchestrator and agents.
import uuid, time, json

def make_msg(sender, receiver, typ, payload):
    """
    Create a standardized A2A message.
    type: REQUEST, RESPONSE, REPORT, ACK
    payload: dict
    """
    return {
        "id": str(uuid.uuid4()),
        "timestamp": time.time(),
        "sender": sender,
        "receiver": receiver,
        "type": typ,
        "payload": payload
    }

def pretty(msg):
    return json.dumps(msg, indent=2)
