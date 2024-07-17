import json
import threading
from queue import Queue
# from modules.auth_handler import login -- del
from modules.comment_handler import post_comment
from modules.proxy_handler import load_proxies
from modules.log_handler import setup_logger, log_info, log_error

def load_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def worker(queue, proxies, config, author_ids, comment_texts):
    while not queue.empty():
        try:
            account = queue.get()
            post_comment(account, proxies, config, author_ids, comment_texts)
        except Exception as e:
            log_error(f"Error posting comment for account {account}: {e}")
        finally:
            queue.task_done()

def main():
    with open("config.json", "r") as file:
        config = json.load(file)
    
    setup_logger(config["log_file"])
    
    proxies = load_proxies(config["proxy_file"])
    author_ids = load_file("author_ids.txt")
    comment_texts = load_file("comment_texts.txt")
    
    num_comments = int(input("Number of comments: "))
    num_threads = int(input("Number of threads: "))
    
    queue = Queue()
    for account in range(num_comments):
        queue.put(account)
    
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(queue, proxies, config, author_ids, comment_texts))
        thread.start()
        threads.append(thread)
    
    queue.join()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
