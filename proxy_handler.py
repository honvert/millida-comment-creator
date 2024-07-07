import random
import requests
from .log_handler import log_error, log_debug

def load_proxies(file_path):
    with open(file_path, "r") as file:
        proxies = file.readlines()
    return [proxy.strip() for proxy in proxies if proxy.strip()]

def make_request_with_proxy(url, headers, cookies, payload, proxies, method="POST"):
    while proxies:
        proxy = random.choice(proxies)
        proxies_dict = {"https": proxy}
        
        try:
            if method == "POST":
                response = requests.post(url, headers=headers, data=payload, proxies=proxies_dict)
            else:
                response = requests.get(url, headers=headers, cookies=cookies, proxies=proxies_dict)

            if response is not None:
                log_debug(f"Proxy {proxy} used successfully.")
                return response
            else:
                log_debug(f"Proxy {proxy} failed. Removing from list.")
                proxies.remove(proxy)
        except requests.exceptions.RequestException as e:
            log_error(f"Request failed with proxy {proxy}. Error: {e}")
            proxies.remove(proxy)

    log_error("No valid proxies available.")
    return None
