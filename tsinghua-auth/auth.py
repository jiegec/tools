#!/usr/bin/env python3
import yaml
import hashlib
import os
from typing import Tuple

import requests
import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
# http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True


login_url = "https://net.tsinghua.edu.cn/do_login.php"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1)" \
             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"


def load_config(path: str = os.path.dirname(os.path.realpath(__file__)) + "/config/account.yaml") -> Tuple[str, str]:
    with open(path) as f:
        config = yaml.load(f)
        username = config["account"]["username"]
        password = config["account"]["password"]

        return username, password


def hex_md5_password(password: str) -> str:
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    return "{MD5_HEX}%s" % password


def try_connections() -> bool:
    try:
        res = requests.get("http://www.baidu.com")
    except requests.HTTPError:
        return False
    return res.status_code == 200


def go_online() -> bool:
    username, password = load_config()
    param = [
        ("action", "login"),
        ("username", username),
        ("password", hex_md5_password(password)),
        ("ac_id", "1")
    ]
    res = requests.post(login_url, data=param)
    if res.status_code != 200:
        return False
    else:
        return True


def main() -> None:
    try:
        if go_online():
            print("Auth succeeded")
        else:
            print("Auth failed")
    except:
        print("Auth failed")


if __name__ == "__main__":
    main()
