from app.sources.client.newrelic.newrelic import NewRelicClient
from app.sources.external.newrelic import NewRelicDataSource


def main():
    api_key = "YOUR_API_KEY_HERE"  # Replace with your New Relic API key
    client = NewRelicClient(api_key=api_key)
    datasource = NewRelicDataSource(client)

    print("Fetching applications...")
    apps = datasource.get_applications()
    print(apps)

    print("\nFetching alert policies...")
    alerts = datasource.get_alert_policies()
    print(alerts)


if __name__ == "__main__":
    main()
