import os
import json
from google.cloud import pubsub_v1
from fake_web_events import Simulation

path = os.path.dirname(os.path.dirname(__file__))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{path}/config/service-account.json"

topic = ""
publisher = pubsub_v1.PublisherClient()
simulation = Simulation(user_pool_size=100, sessions_per_day=1000)
events = simulation.run(duration_seconds=60)


def put_message(data):
    data = json.dumps(data) + "\n"
    response = publisher.publish(topic=topic, data=data.encode("utf-8"))
    print(data)
    return response.result()


for event in events:
    put_message(event)
