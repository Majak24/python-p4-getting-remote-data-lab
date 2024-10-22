import requests

class GetRequester:
    def __init__(self, url):
        """
        Initialize GetRequester with a URL.
        
        Args:
            url (str): The URL to send requests to
        """
        self.url = url
    
    def get_response_body(self):
        """
        Send a GET request to the URL and return the response body as bytes.
        
        Returns:
            bytes: The response body as bytes
        """
        response = requests.get(self.url)
        return response.content
    
    def load_json(self):
        """
        Get the response body and convert it from JSON to Python data structure.
        
        Returns:
            dict/list: Python data structure converted from JSON
        """
        response = requests.get(self.url)
        return response.json()