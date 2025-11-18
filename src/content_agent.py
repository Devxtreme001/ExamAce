# content_agent.py
# Content agent: generate summaries and MCQs for a topic.
# NOTE: In the demo, LLM calls are stubbed to deterministic templates.
import time

def generate_summary_stub(topic_text):
    # Simple extract: first 2 sentences (demo)
    return " ".join(topic_text.split(".")[:2]) + "."

def generate_mcq_stub(topic_name, n=5):
    """
    Generates n template MCQs for demo purposes.
    Replace with LLM/Gemini generation in production.
    """
    mcqs = []
    for i in range(n):
        q = {
            "id": f"{topic_name[:8].replace(' ','_')}_{i}",
            "topic": topic_name,
            "question": f"What is an important fact {i+1} about {topic_name}?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A",
            "explanation": f"Because {topic_name} states important fact {i+1}."
        }
        mcqs.append(q)
    time.sleep(0.1)
    return mcqs

# For parallel execution demo: you can call generate_mcq_stub in multiple threads/processes.
