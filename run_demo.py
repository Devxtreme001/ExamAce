# run_demo.py
"""
Simple runner to execute the ExamAce demo flow locally.
This mirrors the Kaggle notebook main flow so judges can run demo with:
    python run_demo.py
"""
import json, os
from src.memory_bank import MemoryBank
from src.planner_agent import planner_create_plan
from src.content_agent import generate_mcq_stub, generate_summary_stub
from src.evaluator_agent import run_test_and_update

def main():
    USER_ID = "demo_user"
    mem = MemoryBank(filepath="demo_output_samples/memory.json")
    # sample input
    chapter = "Features of Indian Economy"
    chapter_text = (
        "The Indian economy has several distinctive features. "
        "It is characterized by coexistence of modern and traditional sectors. "
        "A large proportion of the population is dependent on agriculture. "
        "The economy has seen high population growth. "
        "There is a vast pool of human resources with low per capita income."
    )
    # Planner
    plan = planner_create_plan([chapter], days=3, memory_summary={})
    print("PLAN:", plan)
    # Content
    mcqs = generate_mcq_stub(chapter, n=10)
    print("Generated", len(mcqs), "MCQs. Sample:", mcqs[0])
    # Simulate user answers (6 correct, 4 wrong)
    user_answers = {q["id"]: (q["answer"] if i<6 else "Distractor C") for i,q in enumerate(mcqs[:10])}
    # Evaluator
    score, results = run_test_and_update(USER_ID, mcqs[:10], user_answers, mem)
    print(f"SCORE: {score*100:.1f}%")
    # Save outputs
    os.makedirs("demo_output_samples", exist_ok=True)
    with open("demo_output_samples/memory.json","w") as f:
        json.dump(mem.store, f, indent=2)
    print("Saved demo outputs to demo_output_samples/")
    return 0

if __name__ == "__main__":
    main()
