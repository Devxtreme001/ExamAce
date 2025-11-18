# evaluator_agent.py
# Evaluator handles test administration, grading and memory updates.
from difflib import SequenceMatcher

def grade_mcq(user_answer, correct_option):
    return 1 if user_answer.strip().upper() == correct_option.strip().upper() else 0

def fuzzy_score(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def grade_free_text(user_answer, reference_text, threshold=0.6):
    return 1 if fuzzy_score(user_answer, reference_text) >= threshold else 0

def run_test_and_update(user_id, questions, user_answers, memory_bank):
    """
    questions: list of question dicts (each has 'answer' or 'reference_text' for free text)
    user_answers: dict qid->answer
    memory_bank: MemoryBank instance
    returns: score, per_question_result
    """
    total = 0
    correct = 0
    results = []
    for q in questions:
        total += 1
        qid = q.get("id")
        ans = user_answers.get(qid, "")
        if q.get("type","mcq") == "mcq":
            res = grade_mcq(ans, q["answer"])
        else:
            res = grade_free_text(ans, q.get("reference_text",""))
        correct += res
        results.append({"id":qid, "correct":res})
        # Update weakness: store low score as weakness
        topic = q.get("topic","general")
        memory_bank.update_weakness(user_id, topic, 1.0 - (res))
    score = correct / total if total else 0
    memory_bank.add_history(user_id, {"test_size":total, "score":score})
    return score, results
