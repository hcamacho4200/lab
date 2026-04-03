import sys
import subprocess
import json

from src.util import kuma_push


def main(threshold: int, kuma_push_url: str, ha_host: str = 'homeassistant-01.home'):
    """Main entry point

    :param: threshold: the percent free required
    :param: kuma_push_url: the push url to kuma
    """

    push_status = "down"
    push_message = ""
    cmd = f"ssh root@{ha_host} -p 2222 'curl -sSL -H \"Authorization: Bearer $SUPERVISOR_TOKEN\" http://supervisor/host/info'"

    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    json_result = json.loads(output.stdout)
    if json_result['result'] == "ok":
        disk_total = json_result['data']['disk_total']
        disk_free = json_result['data']['disk_free']
        percent_free = disk_free / disk_total * 100
        if percent_free < float(threshold):
            push_message = f"Disk Free Alert: {disk_total} {disk_free} {percent_free}"
        else:
            push_message = f"Disk Free OK: {disk_total} {disk_free} {percent_free}"
            push_status = "up"
    else:
        push_message = f"Result: {json_result['result']}, message: {json_result['message']}"
    
    kuma_push(kuma_push_url, push_status, push_message)


if __name__ == '__main__':
    main(*sys.argv[1:])
