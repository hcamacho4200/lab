import requests


def kuma_push(kuma_push_url, push_status, push_message):
    params = {
        "status": push_status,
        "msg": push_message
    }
    result = requests.get(kuma_push_url, params=params)
    print(f'Pushing result {result.status_code} push_status: {push_status} msg: {push_message}')


def proxmox_api_call(proxmox_host: str, token: str, api_call):
    """Make a call to the proxmox api

    :param: proxmox_host: the host to run the API call on
    :param: api_call: the api call properly formatted
    :param: token: the auth token
    """
