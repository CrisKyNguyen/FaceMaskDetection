import time
import sys

import processBar
for i in range(100):
    time.sleep(0.1)
    completed = i+1
    print(f'\r Process: {processBar.strBar(completed)} {processBar.formatNumber(completed)}%   ', end='')