from app.sources.client.newrelic.newrelic import NewRelicClient


class NewRelicDataSource:
    """
    Data source to fetch data from New Relic APIs.
    """

    def __init__(self, client: NewRelicClient):
        self.client = client

    def get_applications(self):
        """Fetch list of applications."""
        return self.client.get("/applications.json")

    def get_alert_policies(self):
        """Fetch all alert policies."""
        return self.client.get("/alerts_policies.json")

    def get_plugins(self):
        """Fetch available plugins."""
        return self.client.get("/plugins.json")

    def get_users(self):
        """Fetch all users."""
        return self.client.get("/users.json")
