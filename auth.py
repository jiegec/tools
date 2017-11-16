#!/usr/bin/env python3
import yaml
import requests
import hashlib
from typing import Tuple

login_url = "https://net.tsinghua.edu.cn/do_login.php"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1)" \
             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"


def load_config(path:str="config/account.yaml") -> Tuple[str, str]:
    with open(path) as f:
        config = yaml.load(f)
        username = config["account"]["username"]
        password = config["account"]["password"]

        return username, password


def hex_md5_password(password:str) -> str:
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
