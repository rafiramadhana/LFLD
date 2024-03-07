import json
import logging

class StructuredMessage(object):
    def __init__(self, message, **kwargs):
        self.kwargs = kwargs
        self.kwargs["message"] = message
    def __str__(self):
        return json.dumps(self.kwargs)
fmt = StructuredMessage
logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.info(fmt('Hello world', user_id='1', user_location='YK'))