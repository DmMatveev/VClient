import os
import sys


class Output:
    def __init__(self):
        self.write = sys.stdout.write
        self.flush('Init')

    def flush(self, out: str):
        os.system('cls')
        self.write(f'Status: {out}')


output: Output = Output()
