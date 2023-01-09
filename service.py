from smartcard.System import readers
import subprocess
from time import sleep
cmd='rundll32.exe user32.dll, LockWorkStation'
while True:
    r = readers()
    if len(r) < 1:
        subprocess.call(cmd)
    sleep(1)
