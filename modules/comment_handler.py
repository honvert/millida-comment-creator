import random
import requests
from .log_handler import log_error, log_info, log_debug
from .proxy_handler import make_request_with_proxy

def post_comment(session_id, proxies, config, author_ids, comment_texts):
    comment_url = config["urls"]["comment_url"]
    headers = config["headers"]
    cookies = config["cookies"]

    author_id = random.choice(author_ids)
    comment_text = random.choice(comment_texts)

    payload = {
        "folder": "comments",
        "script": "create",
        "commentId": "0",
        "serverId": config["server_id"], # serverid
        "authorId": author_id,
        "commentText": comment_text
    }
    
    response = make_request_with_proxy(comment_url, headers=headers, cookies=cookies, payload=payload, proxies=proxies, method="POST")
    
    if response and response.status_code == 200:
        log_info("Comment posted successfully.")
    else:
        log_error(f"Failed to post comment. Status Code: {response.status_code if response else 'No response'}")
