from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi
from datadog_api_client.v1.api.events_api import EventsApi
from datadog_api_client.v1.model.event_create_request import EventCreateRequest


configuration = Configuration()
# configuration.api_key["apiKeyAuth"] = "696dd587e120faa9521069a499240bff"
# configuration.api_key["appKeyAuth"] = "f4d6556ddf9e50de7eb54bb62cb97f123ee1bdac"
# configuration.server_variables["site"] = "us5.datadoghq.com"

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