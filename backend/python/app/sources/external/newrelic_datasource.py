from app.sources.client.newrelic.newrelic import NewRelicClient

class NewRelicDataSource:
    """
    Data source wrapper for New Relic API.
    Uses NewRelicClient to fetch and organize data.
    """

    def __init__(self, api_key: str):
        self.client = NewRelicClient(api_key)

    def fetch_all_applications(self):
        """Fetch all New Relic applications."""
        return self.client.list_applications()

    def fetch_application_details(self, app_id: int):
        """Fetch details for a specific application."""
        return self.client.get_application(app_id)

    def fetch_application_metrics(self, app_id: int):
        """Fetch metrics available for a specific app."""
        return self.client.get_application_metrics(app_id)

