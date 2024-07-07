# millida-comment-creator

The Millida Comment Generator automates the process of creating comments on the Millida.net platform using HTTP's proxies from `proxies.txt`.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Logging](#logging)
- [Important Notes](#important-notes)
- [Author](#author)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/honvert/millida-comment-generator.git
   cd millida-comment-generator
   ```
2. **Install dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```
3. **Configure the script**:
   
   Edit `config.json` to set the `server_Id` for Millida.net.
   Ensure `headers` are correctly configured.
   Set `use_proxy` to true if using proxies, and specify the `proxy_file`.

4. Prepare comment data:
   
   Populate `comment_texts.txt` with various comments to be randomly sent.

## Usage
1. Run the script main.py:

```bash
python3 main.py
```

  The script will initiate the login process using configured accounts and proxies, and randomly send comments from `comment_texts.txt`.

## Configuration
`config.json`: Contains URLs, headers, cookies, proxy settings, and file paths for accounts and comments.

## Logging
Logs are stored in `log.txt` for tracking script execution.
Logs are also output to the `terminal` for real-time monitoring

## Author
Author: [honvert]
Contact: [hongvertin@gmail.com]
