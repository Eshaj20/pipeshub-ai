from app.sources.external.newrelic_datasource import NewRelicDataSource

if __name__ == "__main__":
    api_key = "YOUR_NEW_RELIC_API_KEY"  # Replace with your own key

    datasource = NewRelicDataSource(api_key)

    print("Fetching all applications...")
    apps = datasource.fetch_all_applications()
    print(apps)

    if apps and "applications" in apps and len(apps["applications"]) > 0:
        first_app_id = apps["applications"][0]["id"]
        print(f"\nFetching details for application ID: {first_app_id}")
        print(datasource.fetch_application_details(first_app_id))

        print(f"\nFetching metrics for application ID: {first_app_id}")
        print(datasource.fetch_application_metrics(first_app_id))

