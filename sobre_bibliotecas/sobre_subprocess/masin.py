import subprocess
import sys
# encoding é cp850
cmd = ['ls' '-lah' '/']
system = sys.platform 
encoding = 'cp850'

# if system == "win32":
#     cmd = ['ping', '127.0.0.1']
#     encoding = 'cp850'

proc = subprocess.run(
     cmd, capture_output=True,
     text=True, encoding=encoding,
     shell=True
)

print(proc.stdout)