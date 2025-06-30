# benchmarks/codingagent/script/eval.py
import os, subprocess, json

def evaluate(env_root, **kwargs):
    # run the agent’s solution
    res = subprocess.run(
        ["python", os.path.join(env_root, "solution.py")],
        capture_output=True, text=True
    )
    # simple pass/fail: exit code 0 means success
    return {"success": res.returncode == 0, "stdout": res.stdout, "stderr": res.stderr}
