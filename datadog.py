import os
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi
from datadog_api_client.v1.api.events_api import EventsApi
from datadog_api_client.v1.model.event_create_request import EventCreateRequest

configuration = Configuration()
configuration.api_key["apiKeyAuth"] = os.getenv("DD_API_KEY")
configuration.api_key["appKeyAuth"] = os.getenv("DD_APP_KEY")
configuration.server_variables["site"] = os.getenv("DD_SITE")

print(f"API Key: {configuration.api_key["apiKeyAuth"]}")
print(f"APP Key: {configuration.api_key["appKeyAuth"]}")
print(f"Site: {configuration.server_variables["site"]}")

body = EventCreateRequest(
    title="Python-Event",
    text="This is an event from a Python script",
    alert_type="warning",
    priority="normal",
    source_type_name="python",
    host="macosx",
    tags=[
        "event:DiegoEvent",
        "source:python-app",
    ],
)

with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts()
    print(response)
    api_instance = EventsApi(api_client)
    response = api_instance.create_event(body=body)
    print(response)