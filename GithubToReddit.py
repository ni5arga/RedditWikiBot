import praw
from github import Github
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

def mirror_wiki_pages(wiki_pages, path_prefix=""):
    for wiki_page in wiki_pages:
        page_name = f"{path_prefix}/{wiki_page.name}" if path_prefix else wiki_page.name

        if not mirror_config and page_name.startswith('config/'):
            print(f"Skipping config wiki page: {page_name}")
            continue

        print(f"Processing wiki page: {page_name}")
        file_path = f"wiki/{page_name}.md"

        try:
            file = repo.get_contents(file_path, ref="main")
            file_content = file.decoded_content.decode('utf-8')

            subreddit.wiki[page_name].edit(content=file_content, reason=f"Mirror {page_name} from GitHub")

            print(f"Wiki page {page_name} mirrored successfully.")
        except Exception as e:
            print(f"Error mirroring wiki page {page_name}: {e}")

        if hasattr(wiki_page, 'pages') and callable(getattr(wiki_page, 'pages')):
            subpages = wiki_page.pages()
            mirror_wiki_pages(subpages, path_prefix=page_name)

mirror_wiki_pages(wiki_pages)
