import requests
import random
import string
from .log_handler import log_error, log_info, log_debug
from .proxy_handler import make_request_with_proxy

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def login(account, proxies, config):
    login_url = config["urls"]["login_url"]
    username, password = account
    cookies = config["cookies"]
    cookies["PHPSESSID"] = generate_random_string()
    
    payload = {
        "login": username,
        "password": password
    }
    
    response = make_request_with_proxy(login_url, headers=config["headers"], cookies=cookies, payload=payload, proxies=proxies)
    
    if response and response.status_code == 200:
        log_info(f"Login successful for {username}")
        return True, cookies["PHPSESSID"]
    else:
        log_error(f"Login failed for {username}. Status Code: {response.status_code if response else 'No response'}")
        return False, None
