from operator import itemgetter
import requests
import json

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
sumbission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    # Build a dictionary for each article.
    submission_dict = {
    'title': response_dict.get('title', 'No title available'),  # Use .get() to avoid KeyError
    'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
    'comments': response_dict.get('descendants', 0)  # Default to 0 if 'descendants' is missing
}

# Append to the list of dictionaries
sumbission_dicts.append(submission_dict)

submission_dict = sorted(sumbission_dicts, key=itemgetter('comments'),
    reverse=True)

for submission_dict in sumbission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")





# Explore the structure of the data.
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)