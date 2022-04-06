# Third-party imports...
import logging

import requests

log = logging.getLogger(__name__)

BASEURL = "http://jsonplaceholder.typicode.com/todos"

class Todo:
    def get_todos(self):
        response = requests.get(BASEURL)
        log.debug(f"response from service ${response}")
        if response.ok:
            return response
        else:
            return None
