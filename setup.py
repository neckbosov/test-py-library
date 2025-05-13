import os
import sys
import re
import subprocess
import json
# setup.py dependant on boto3
subprocess.run(
        ["python", "-m", "pip", "install", "boto3"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

