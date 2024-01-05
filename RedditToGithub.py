import praw
from github import Github, InputFileContent, GithubException
from dotenv import load_dotenv
import os

load_dotenv()

reddit_client_id = os.getenv('REDDIT_CLIENT_ID')
reddit_client_secret = os.getenv('REDDIT_CLIENT_SECRET')
reddit_user_agent = os.getenv('REDDIT_USER_AGENT')
reddit_username = os.getenv('REDDIT_USERNAME')
reddit_password = os.getenv('REDDIT_PASSWORD')

github_token = os.getenv('GITHUB_TOKEN')
github_repo_owner = os.getenv('GITHUB_REPO_OWNER')
github_repo_name = os.getenv('GITHUB_REPO_NAME')

reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent,
                     username=reddit_username,
                     password=reddit_password)

github = Github(github_token)
repo = github.get_user(github_repo_owner).get_repo(github_repo_name)

subreddit_name = os.getenv('SUBREDDIT_NAME')

mirror_config = os.getenv('MIRROR_CONFIG', 'TRUE').upper() == 'TRUE'

subreddit = reddit.subreddit(subreddit_name)
wiki_pages = subreddit.wiki

print(f"GitHub Repo Name: {github_repo_name}")
print(f"Subreddit Name: {subreddit_name}")
print(f"Mirror Config: {mirror_config}")

print("Entering loop...")

for wiki_page in wiki_pages:
    if not mirror_config and wiki_page.name.startswith('config/'):
        print(f"Skipping config wiki page: {wiki_page.name}")
        continue
    
    print(f"Processing wiki page: {wiki_page.name}")
    file_path = f"wiki/{wiki_page.name}.md"
    file_content = wiki_page.content_md
    
    try:
        file = repo.get_contents(file_path, ref="main")
        repo.update_file(file_path, f"Mirror {wiki_page.name} from {subreddit_name}", file_content, file.sha, branch="main")
        print(f"Wiki page {wiki_page.name} mirrored successfully.")
    except GithubException as e:
        if e.status == 404:
            repo.create_file(file_path, f"Mirror {wiki_page.name} from {subreddit_name}", file_content, branch="main")
            print(f"Wiki page {wiki_page.name} created successfully.")
        else:
            print(f"Error mirroring wiki page {wiki_page.name}: {e}")
