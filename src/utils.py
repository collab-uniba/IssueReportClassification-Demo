from github import Github
from urllib.parse import urlparse
from typing import Dict

def extract_github_issue(url: str, access_token: str = None) -> Dict[str, str]:
    """
    Extract the title andA body of a GitHub issue from its URL.

    Args:
        url: The URL of the GitHub issue.
        access_token: An access token to authenticate with the GitHub API (optional).

    Returns:
        A dictionary containing the title and body of the GitHub issue.

    Raises:
        ValueError: If the URL is not a valid GitHub issue URL, or if there is an error fetching the issue from the GitHub API.
    """
    # Parse the URL to extract the repository and issue number
    parsed_url = urlparse(url)
    if parsed_url.netloc != 'github.com' or '/issues/' not in parsed_url.path:
        raise ValueError('Invalid GitHub issue URL')
    parts = parsed_url.path.strip('/').split('/')
    repo_owner, repo_name, issue_number = parts[0], parts[1], int(parts[3])

    # Initialize a PyGithub object using an access token, if provided
    if access_token:
        github_client = Github(access_token)
    else:
        github_client = Github()

    try:
        # Get the repository and issue objects using the PyGithub API
        repository = github_client.get_repo(f'{repo_owner}/{repo_name}')
        github_issue = repository.get_issue(issue_number)
    except Exception as e:
        raise ValueError(f'Unable to fetch issue from GitHub API: {str(e)}')

    # Extract the issue title and body
    title = github_issue.title
    body = github_issue.body

    return {'title': title, 'body': body}
