from app.sources.client.http import HTTPClient

class NewRelicClient(HTTPClient):
    """
    Client for interacting with the New Relic REST API v2.
    """

    def __init__(self, api_key: str):
        super().__init__(base_url="https://api.newrelic.com/v2/")
        self.headers = {
            "Api-Key": api_key,
            "Content-Type": "application/json"
        }

    def list_applications(self):
        """Get all applications."""
        return self.get("applications.json")

    def get_application(self, app_id: int):
        """Get a specific application's details."""
        return self.get(f"applications/{app_id}.json")

    def get_application_metrics(self, app_id: int):
        """Get metrics for a specific app."""
        return self.get(f"applications/{app_id}/metrics.json")
