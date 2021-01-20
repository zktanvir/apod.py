

class NoApiKey(Exception):
    def __init__(self, message="No api key was provided. Get one from https://api.nasa.gov"):
        self.message = message
        super().__init__(self.message)

class InvalidApiKey(Exception):
    def __init__(self, message="Invalid api key was provided. Get one at https://api.nasa.gov"):
        self.message = message
        super().__init__(self.message)
