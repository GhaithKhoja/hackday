"""API Endpoint for user search."""
from flask import jsonify, request
from collections import Counter
import requests
import hackday

@hackday.app.route('/api/v1/search/', methods=['GET'])
def search_repositories():
    """Return a JSON response of search results."""
    
    # Make sure the user provided a username to the endpoint
    username = request.args.get("username")
    
    # if no username was provided return an error
    if not username:
        return hackday.utils.return_bad_request()
        
    # Build request that will be sent to the github API
    # Num of repos per page
    max_page_count = 30
    # Keep in track the repos we have searched
    repos = []
    # URL and headers that we will use to access the API
    url = f"https://api.github.com/search/repositories?q=user:{username}&per_page={max_page_count}&page=1"
    headers = {
        "Authorization": f"Bearer {hackday.credentials.GITHUB_KEY}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    
    # Create context that we will return in JSON format
    context = {}
    # Total repo count
    context["total_repo_count"] = 0
    # Total stargazers
    context["total_stargazers"] = 0
    # Total fork count
    context["total_fork_count"] = 0
    # Average size of repos
    context["avg_repo_size"] = 0
    # Counter object that will keep track of languages used and their usage count
    language_list = Counter()
    
    # Start making requests to the github API until we searched all repos
    while True:
        # Make a request
        response = requests.get(url, headers=headers)
        
        # If request is successful 
        if response.status_code == 200:
            # Turn data to JSON
            data = response.json()
            
            # Increment total repo count
            context["total_repo_count"] += data["total_count"]
            
            # Append repos
            repos.extend(data['items'])
            
            # Check if there are more pages
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                break
        else:
            break 
        
    # Iterate through repos to fill information
    for repo in repos:
        # Add stargazers
        context["total_stargazers"] += repo["stargazers_count"]
        # Add fork count
        context["total_fork_count"] += repo["forks_count"]
    
        
    return jsonify(**context)