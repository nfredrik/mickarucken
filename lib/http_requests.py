import json
import urequests
from datacake_keys import DATACAKE_URL, DATACAKE_SERIAL
from http import HTTPStatus
# TODO:  remove?
#HTTP_STATUS_OK = 200


class DataCakeError(Exception):
    ...


class HttpAliveError(Exception):
    ...


def http_alive(url: str = 'http://detectportal.firefox.com/') -> None:
    response = urequests.get(url)
    if response.status_code != HTTPStatus.OK:
        raise HttpAliveError(f"Error, failed to connect: {response.status_code}")

    print(response.content)
    if 'success' not in response.content:
        raise HttpAliveError(f"Error, fail to connect to get correct data: {response.content}")


# Have datacake url as parameter?
def post_values(temp: float, hum: int) -> None:
    payload = {
        "serial": DATACAKE_SERIAL,
        "temperature": temp,
        "humidity": hum}
    json_payload = json.dumps(payload)

    response = urequests.post(DATACAKE_URL, data=json_payload)
    if response.status_code != HTTPStatus.OK:
        raise DataCakeError(f"Error, failed to post data! {response.status_code}")
