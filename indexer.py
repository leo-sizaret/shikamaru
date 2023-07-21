from substrateinterface import SubstrateInterface

substrate = SubstrateInterface(url="wss://sharingan.madara.zone")

def subscription_handler(obj, update_nr, subscription_id):
    block_number = obj['header']['number']
    print(f"Bonjour! Getting block #{block_number}")

    block = substrate.get_block(block_number=block_number)
    print(block)

    # if update_nr > 2:
    #     return {'message': 'Subscription will cancel when a value is returned', 'updates_processed': update_nr}


result = substrate.subscribe_block_headers(subscription_handler)