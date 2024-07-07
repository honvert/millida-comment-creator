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
   pip install -r requirements.txt
   ```
3. **Configure the script**:
   
   Edit `config.json` to set the `server_Id` for Millida.net.
   Ensure `headers` are correctly configured.
   Set `use_proxy` to true if using proxies, and specify the `proxy_file`.

4. Prepare comment data:
   
   Populate `comment_texts.txt` with various comments to be randomly sent.

5. Set up author IDs:

   Input `author IDs` into author_ids.txt for use in comments.

## Usage
