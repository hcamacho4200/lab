import sys
import subprocess
import json

from util import kuma_push


def main(slug: str, kuma_push_url: str, ha_host: str = 'homeassistant-01.home'):
    """Main entry point

    :param: slug: the slug name of the addin
    :param: kuma_push_url: the push url to kuma
    """

    push_status = "down"
    push_message = ""
    cmd = f"ssh root@{ha_host} -p 2222 'curl -sSL -H \"Authorization: Bearer $SUPERVISOR_TOKEN\" http://supervisor/addons/{slug}/info'"

    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    json_result = json.loads(output.stdout)
    if json_result['result'] == "ok":
        push_message = f"Add-on state: {json_result["data"]["state"]}"
        if json_result["data"]["state"] == "started":
            push_status = "up"
        else:
            push_status = "down"
    else:
        push_message = f"Result: {json_result['result']}, message: {json_result['message']}"
    kuma_push(kuma_push_url, push_status, push_message)


if __name__ == '__main__':
    main(*sys.argv[1:])
