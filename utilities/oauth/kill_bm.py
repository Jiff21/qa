"""
For killing interuppted Browsermob servers locally.
Note psutil is not in requirements.txt for auth, install with pip to use this
file.
"""
import psutil

for process in psutil.process_iter():
    try:
        process_info = process.as_dict(attrs=['name', 'cmdline'])
        if process_info.get('name') in ('java', 'java.exe'):
            print(process_info.get('cmdline'))
            for cmd_info in process_info.get('cmdline'):
                if cmd_info == '-Dapp.name=browsermob-proxy':
                    print('Killing stray admob servers')
                    process.kill()
    except psutil.NoSuchProcess:
        pass
