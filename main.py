import json
import threading
from queue import Queue
from modules.auth_handler import login
from modules.comment_handler import post_comment
from modules.proxy_handler import load_proxies
from modules.log_handler import setup_logger, log_info, log_error

def load_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def main():
    with open("config.json", "r") as file:
        config = json.load(file)
    
    setup_logger(config["log_file"])
    
    proxies = load_proxies(config["proxy_file"])
    author_ids = load_file("author_ids.txt")
    comment_texts = load_file("comment_texts.txt")
    
    for account in range(int(input("Number of comments: "))):
        post_comment(None, proxies, config, author_ids, comment_texts)
    
    num_threads = int(input("Enter the number of threads to use: "))
    
    account_queue.join()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
