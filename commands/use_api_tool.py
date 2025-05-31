"""
A simple tool to directly use any API.
"""
import requests

def use_api(url, method='GET', headers=None, data=None):
    """
    Function to use any API with provided parameters.

    Args:
        url (str): The API endpoint.
        method (str): The request method, default is 'GET'.
        headers (dict): Additional headers for the request.
        data (dict): Data to send in the request, applicable for POST requests.

    Returns:
        dict: The API response as a dictionary.
    """
    response = requests.request(method, url, headers=headers, data=data)
    return response.json()
