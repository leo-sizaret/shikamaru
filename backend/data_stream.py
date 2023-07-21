"""Module with classes for data fetching data streams from L3 source."""

from substrateinterface import SubstrateInterface


class DataStream:
    """Class that is used to get the data from L3 source."""
    def __init__(self, source_url="wss://sharingan.madara.zone", batch_size=1):
        self.batch_size = batch_size
        self.source_url = source_url
        self.client = None

    def get_batch(self):
        self.client = SubstrateInterface(url=self.source_url)
        self.client.subscribe_block_headers(self.get_block)

    def get_block(self, obj, update_nr, subscription_id):
        block_number = obj['header']['number']
        print(f"Bonjour! Getting block #{block_number}")
        block = self.client.get_block(block_number=block_number)
        print(block)


DataStream().get_batch()
