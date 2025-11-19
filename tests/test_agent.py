# tests/test_agent.py
import subprocess
import sys

def test_run_demo():
    # Run the demo runner; expects exit code 0
    ret = subprocess.call([sys.executable, "run_demo.py"])
    assert ret == 0, "run_demo.py failed (non-zero exit code)"

if __name__ == "__main__":
    test_run_demo()
    print("Integration test passed.")
