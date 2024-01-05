# RedditWikiBot
RedditWikiBot is a bot that facilitates the synchronization of Reddit wiki pages with a GitHub repository and vice versa.
It is a Reddit bot written in Python which mirrors subreddit wiki pages to your GitHub repository and can also mirror them back to the subreddit pages if they are updated or changed in the GitHub repository.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

RedditWikiBot consists of two main scripts:
- **RedditToGithub.py**: Mirrors subreddit wiki pages to a specified GitHub repository.
- **GithubToReddit.py**: Mirrors GitHub repository wiki pages to a specified subreddit.

## Features

- Bidirectional synchronization of wiki pages between Reddit and GitHub.
- Customizable configuration to skip certain pages or directories.
- Error handling for various scenarios, such as missing files or network issues.

## Requirements

- Python 3.x
- PRAW (Python Reddit API Wrapper)
- PyGithub

## Installation

1. Clone the GitHub repository:

   ```bash
   git clone https://github.com/ni5arga/RedditWikiBot.git
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in project root directory with the following credentials.

```env
# Reddit API credentials
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_reddit_user_agent
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password

# GitHub credentials
GITHUB_TOKEN=your_github_token
GITHUB_REPO_OWNER=REPO_OWNER_USERNAME
GITHUB_REPO_NAME=YOUR_REPO_NAME

# Other configurations
SUBREDDIT_NAME=your_subreddit_name
MIRROR_CONFIG=TRUE/FALSE (Setting true will mirror config/ files too, recommended to keep false)
```
Replace `your_reddit_client_id`, `your_reddit_client_secret`, `your_reddit_user_agent`, `your_reddit_username`, `your_reddit_password`, `your_github_token`, and `your_subreddit_name` with your actual credentials.
 
## Usage 
### RedditToGitHub.py
Run the following command to mirror subreddit wiki pages to the GitHub repository:

```bash
python RedditToGithub.py
```
### GithubToReddit.py
Run the following command to mirror GitHub repository wiki pages to the subreddit:

```bash
python GithubToReddit.py
```

## Contributing
Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated!


