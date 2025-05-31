import requests

def post_to_pastebin(content, api_dev_key):
    """Post content to Pastebin anonymously."""
    url = 'https://pastebin.com/api/api_post.php'
    data = {
        'api_dev_key': api_dev_key,
        'api_option': 'paste',
        'api_paste_code': content,
        'api_paste_private': '1',  # Make paste unlisted
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return {'success': True, 'link': response.text}
    else:
        return {'success': False, 'message': response.text}
