import subprocess

def get_bssid():
    bssid = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("utf-8")
    result = ''
    for i in range(7):
        if i == 0 or i == 6:
            result = result + bssid.split("BSSID")[1].split(":")[i].strip()
        else:
            result = result + bssid.split("BSSID")[1].split(":")[i].strip() + ":"
    return result.split("\n")[0].upper()