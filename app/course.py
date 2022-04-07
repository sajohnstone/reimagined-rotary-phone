# Third-party imports...
import logging

import requests

log = logging.getLogger(__name__)

BASEURL = "https://staging-rest.edapp.com/v2/catalog"


class Course:
    def get_course(self):
        url = f"{BASEURL}/courses"
        headers = {"Authorization": "bearer 9fe82a79-b2c9-4195-8dee-25f0fe2a92d8"}
        response = requests.get(url, headers=headers)
        log.debug(f"response from service ${response}")
        if response.ok:
            return response
        else:
            return None
