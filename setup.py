import os
import sys
import re
import subprocess
import json
# setup.py dependant on boto3
which_python_process = subprocess.run(
    ["which", "python"],
    check=False,
    encoding="utf-8",
    capture_output=True
)
process = subprocess.run(
        ["python", "-m", "pip", "install", "boto3"],
        check=False,
        encoding="utf-8",
        capture_output=True
    )
current_path = os.getenv("PATH")
subprocess_path = subprocess.run(
    ["echo", "\"$PATH\""],
    check=False,
    encoding="utf-8",
    capture_output=True,
    shell=True
)
virtual_env = os.getenv("VIRTUAL_ENV")
virtual_env_cmd = subprocess.run(
    ["echo", "\"$VIRTUAL_ENV\""],
    check=False,
    encoding="utf-8",
    capture_output=True,
    shell=True
)
with open("/home/datalore/setup_log.txt", "w+") as f:
    f.write("Current path: " + current_path + "\n")
    f.write("Subprocess path: " + subprocess_path.stdout + "\n")
    f.write("Virtual env: " + virtual_env + "\n")
    f.write("Which python:")
    f.write(which_python_process.stdout)
    f.write(process.stdout)
    f.write("\nError output:\n")
    f.write(process.stderr)
    f.flush()

