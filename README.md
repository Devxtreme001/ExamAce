# StudyAgent — Capstone Project (Agents for Good — Education)

**One-line:** StudyAgent is a multi-agent AI study coach that builds prioritized study plans, generates targeted MCQs with explanations, administers tests, auto-grades answers, and adapts future learning using long-term memory — with full observability for evaluation.

## Track
Agents for Good — Education

## Elevator pitch (why it matters)
Students preparing for high-stakes exams waste time on unfocused study and low-quality practice. StudyAgent reduces wasted effort by customizing study plans, producing high-quality practice questions, measuring mastery, and adapting future revision — so students get targeted practice where it matters most.

## What this repo contains
- `src/` — core agent code (Planner, Content, Evaluator, Orchestrator, MemoryBank, Tools)
- `notebook/demo_notebook.ipynb` — runnable Kaggle notebook demo with inline docs and screenshots
- `docs/video_script.md` — ready-to-record 2-3 minute demo script
- `README.md` — this file
- `demo/demo_output_samples/` — saved logs, memory dumps, and screenshots

## Features implemented (mapping to judging rubric)
- **Multi-agent system**: Planner (sequential), Content (parallel workers), Evaluator (loop agent). (A2A messaging implemented.)
- **Tools**: Code execution tool (auto-grader); Search tool stub (for citations). Custom MCQ generator wrapper.
- **Sessions & Memory**: InMemorySessionService and MemoryBank (long-term).
- **Long-running ops**: Demonstrated pause/resume via session state in notebook.
- **Context engineering**: Context compaction routine storing top 5 weak topics.
- **Observability**: Structured logs and metrics (pandas DataFrame printed in notebook).
- **Agent evaluation**: Evaluator provides before/after metrics and exports a metrics CSV.

> Note: Gemini placeholders included; if you have Gemini keys, follow the README to plug them in. **No API keys are included in the repo.**

## Quick demo (what judges will see)
1. Input: sample user profile + chapter text.  
2. Planner builds a 7-day plan prioritizing weak topics.  
3. Content agent generates 20 MCQs with explanations (parallel).  
4. Evaluator administers 10-question mini-test, auto-grades, updates MemoryBank.  
5. Notebook shows memory before/after, logs, and metrics dashboard.

## How to run (Kaggle notebook recommended)
1. Clone repo.  
2. Open `notebook/demo_notebook.ipynb` on Kaggle. (All cells are runnable without API keys due to safe stubs.)  
3. Run cells top-to-bottom. Replace stub LLM calls with Gemini/LLM API by setting environment variables (see below).

## Files & what matters
- `src/planner_agent.py` — plan generation and prioritization logic.
- `src/content_agent.py` — MCQ + summary generation (LLM stub).
- `src/evaluator_agent.py` — mock test runner + auto-grader (code execution tool).
- `src/memory_bank.py` — persistent memory interface (JSON in demo).
- `src/orchestrator.py` — A2A message bus orchestrator used in demo.
- `notebook/demo_notebook.ipynb` — the full demo for judges.

## How this meets scoring categories (explicit)
- **Category 1: Pitch** — Problem, solution, value are documented in this README + docs/architecture.md.
- **Category 2: Implementation** — Code is modular, commented, includes session/memory, observability, and agent communication.
- **Bonus** — Gemini placeholders for Planner & Content agents (5 points), deployment notes included in docs/ (5 points), and video_script.md for a <3min video (10 points).

## Limitations & future work
- Current notebook uses LLM stubs for offline demo; swap in a real LLM for live behavior.
- Deployment to Agent Engine or Cloud Run is documented but not executed (to avoid costs).
- Grading for long free-text answers is basic (fuzzy matching); future work: rubric-based scoring.

## Reproducibility & safety
- No keys in repo. Use environment variables to provide keys if you have them. Kaggle demo runs with stubs and is fully reproducible.

## Submission assets
- Kaggle notebook link (add here)
- GitHub repo link (add here)
- Video (≤3min) — use `docs/video_script.md` to record

## Contact
Project by Dev (student). For quick reproduction help, open the demo notebook and run all cells.
