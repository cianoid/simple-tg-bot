import os
import subprocess
from typing import Iterable


def launch(command: str, logger) -> Iterable:
    logger.info(f"run {command}")
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="cp866")
    for line in p.stdout.readlines():
        if isinstance(line, str):
            yield line.strip()

    yield p.wait() == os.EX_OK
    return
