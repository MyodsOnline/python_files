import subprocess

data = (
    subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
)
# profiles = [i.split(':') for i in data if 'All User Profile' in i]
