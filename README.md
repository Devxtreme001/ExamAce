# ExamAce (StudyAgents)   
**Track:** Agents for Good — Education

**What It Does:**  
StudyAgent is a multi-agent AI study coach that builds prioritized study plans, generates targeted MCQs with explanations, administers tests, auto-grades performance, and adapts learning paths using long-term memory — with full observability for evaluation.

---

# 🎯 1. Why did i choose to make  this project —
Students preparing for high-stakes board exams waste enormous time on unfocused studying and low-quality practice questions. This leads to low retention, poor prioritization, and high stress.

**ExamAce directly solves this** by:
- Detecting weak topics  
- Prioritizing them in the study plan  
- Generating targeted practice questions  
- Measuring mastery  
- Adapting training over time  

The result: faster improvement, focused practice, and measurable progress.

---

# 🧠 2. Why AGENTS 
Agents are not just a “cool architecture.” They are the only structure that handles this workflow cleanly:

### **Planner Agent**
- Decides *what* the student should study next  
- Orders topics by weakness  
- Creates multi-day plans  
- Sequential decision-making → fits a planner agent perfectly  

### **Content Agent**
- Generates MCQs and explanations in parallel  
- Stateless generation tasks → ideal for parallel agents  

### **Evaluator Agent**
- Administers tests  
- Grades answers deterministically  
- Updates long-term memory  
- Needs a loop (until mastery) → perfect for loop agent  

### **Orchestrator**
- Passes A2A messages between agents  
- Logs everything  
- Produces a transparent, inspectable workflow  

Agents give the system *structure, delegation, and explainability*.  
This is exactly what the rubric is looking for.

---

# 🔗 3. Live Demo & Links
- **Kaggle notebook (runnable demo):**  
  https://www.kaggle.com/code/devxtreme/examace-ai-agent

- **YouTube video (≤3 min):**  
  *ADD HERE AFTER RECORDING*

- **GitHub repo:**  
  *This repo*

---

# 🗂️ 4. Repo Contents
- `src/`  
  - Planner, Content, Evaluator  
  - Orchestrator  
  - MemoryBank  
  - Tools (CodeExec + Search Stub)

- `demo/`  
  Screenshots and exported logs/metrics from running the notebook on Kaggle.

- `architecture.png`  
  Architecture diagram (ASCII + PNG)


---

# ⚙️ 5. Full Feature Checklist (mapping to rubric)

### ✅ Multi-Agent System  
(Required feature)  
- Planner Agent — *notebook Cell 8*  
- Content Agent — *Cell 10–11*  
- Evaluator Agent — *Cell 12–13*  
- Agents communicate via A2A protocol — *Cell 4*

### ✅ Tools  
- Code Execution Tool (auto-grader) — *Cell 14*  
- Search Tool Stub — *Cell 14*  
- Custom MCQ Generator Wrapper — *Cell 10*

### ✅ Sessions & Memory  
- InMemorySessionService — *Cell 6*  
- MemoryBank (long-term learning state) — *Cell 6*

### ✅ Long-running Operations  
- Session state persists; demonstration of pause/resume — *Cell 18* (session creation + state storage)

### ✅ Context Engineering  
- Weak-topic compaction stored in MemoryBank — *Cell 12*  

### ✅ Observability  
- Structured logs (`logs.json`) — *Cell 25*  
- Metrics DataFrame (`metrics.csv`) — *Cell 25–27*

### ✅ Agent Evaluation  
- Evaluator computes before/after accuracy  
- Updates weakness scores  
- Saves performance history — *Cell 12 + Cell 25*

### ⭐ Bonus (documented)
- Gemini placeholders for Planner + Content — *Cell 31*  
- Deployment notes included in docs — *docs/ folder*  
- Video (≤3min) — *pending*

---

# 🧪 6. Quick Demo
1) **Planner output**  
Generates 3-day focused plan prioritizing weak topics.

2) **MCQ generation**  
Creates 20 MCQs with explanations (parallel threads).

3) **Mini-test**  
10-question test graded automatically.

4) **Memory update**  
Weak topics boosted; history appended.

5) **Observability**  
Logs + metrics saved and displayed.

Screenshots for all are in `demo/demo_output_samples/`.

---

# 🚀 7. How to Run
### **Preferred: Kaggle**
1. Open the notebook.  
2. Run all cells top-to-bottom.  
3. All logic works offline (no API keys required).  

### **Optional: Local**
---

# 📦 8. Limitations & Future Work
- Current MCQ generator is stubbed; replace with Gemini/OpenAI in 5 minutes.  
- Deployment to Cloud Run/Agent Engine is documented but not executed (cost-saving).  
- Free-text grading uses fuzzy matching; future improvement could use rubric scoring.

---

# 🔐 9. Safety & Reproducibility
- No API keys included.  
- Stubs ensure the entire system is deterministic and reproducible for judges.  
- All demo outputs were generated inside Kaggle and exported for transparency.

---

# 🧩 10. Submission Assets
- **Kaggle Notebook:** https://www.kaggle.com/code/devxtreme/examace-ai-agent  
- **Video:** *ADD LINK HERE*  
- **GitHub Repo:** *this repo*  

---

# 👤 Contact
Created by Dev — student developer.  
For reproduction or evaluation, run the Kaggle notebook.
