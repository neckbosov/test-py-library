import os
import sys
import re
import subprocess
import json
# setup.py dependant on boto3
process = subprocess.run(
        ["python", "-m", "pip", "install", "boto3"],
        check=False,
        text=True,
        stderr=subprocess.STDOUT,
        capture_output=True
    )

with open("/home/datalore/setup_log.txt", "w+") as f:
    f.write(process.stdout)

process.check_returncode()
