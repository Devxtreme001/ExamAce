# code_executor.py
# Small utility to run grading code (safe local functions only)
def run_autograder(func, *args, **kwargs):
    """
    Run a local grading function and capture outputs.
    This acts as a Code Execution tool in the agent stack.
    """
    return func(*args, **kwargs)
