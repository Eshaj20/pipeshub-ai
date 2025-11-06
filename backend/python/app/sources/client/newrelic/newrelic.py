from app.sources.client.http.http_client import HTTPClient


class NewRelicClient(HTTPClient):
    """
    NewRelicClient helps connect to New Relic REST APIs.
    Uses API key authentication.
    """

    def __init__(self, api_key: str):
        base_url = "https://api.newrelic.com/v2"
        headers = {
            "Api-Key": api_key,
            "Content-Type": "application/json",
        }
        super().__init__(base_url=base_url, headers=headers)
