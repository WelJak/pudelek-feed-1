class WykopClientMock:
    def __init__(self, *args, **kwargs):
        pass

    def prepare_link_draft(self, *args, **kwargs):
        return {'data': {'compact': {'photos': {'key': 'photokey'}}}}

    def add_link(self, *args, **kwargs):
        return {'data': {'compact': {'full': {'url': 'www.url.url'}}}}

    def add_entry(self, *args, **kwargs):
        return True
