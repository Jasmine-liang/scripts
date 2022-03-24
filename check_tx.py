# check if nft is minted
from thirdweb import ThirdwebSdk, SdkOptions
from thirdweb.modules.nft import MintArg
from thirdweb_web3.exceptions import TransactionNotFound
import time
import random
import copy
from typing import Dict
from web3 import Web3
from hexbytes import HexBytes
import json
sdk = ThirdwebSdk(SdkOptions(), 'https://rpc-mumbai.maticvigil.com')
sdk.set_private_key('8d3f058fda1ad2a2f6c8d76163051fb6017044111dab5fb44d7a54e8a45deafb')
module_addrs = '0x037C48511BFCF94c18089c6Ca036c6C3947C6976'
nft_module = sdk.get_nft_module(module_addrs)


w3 = Web3(Web3.HTTPProvider('https://rpc-mumbai.maticvigil.com'))
res = w3.eth.get_transaction_receipt('0x28a9910832d5efd43e1bc09605d306e4ad6d3e9a0e0d4b4ad20a62667c1f4a60')
print(((res['status'])))








properties={
    "test": "test"
}
mint_arg = MintArg(
    name= "test",
    description="test",
    properties=properties,
    )
eth_addrs = '0x3cb2e8b6Da8b37e2b1eA55c6e54a3A0eA3270519'
        
def _mint(to_address, arg: MintArg):

    final_properties: Dict
    if arg.properties is None:
        final_properties = {}
    else:
        final_properties = copy.copy(arg.properties)

    if arg.image == "":
        arg.image = arg.image_uri

    meta = {
        'name': arg.name,
        'description': arg.description,
        'image': arg.image,
        'properties': final_properties
    }

    uri = nft_module.upload_metadata(meta)
    tx = nft_module.get_abi_module().mint_to.build_transaction(
        to_address, uri, nft_module.get_transact_opts()
    )

    receipt = nft_module.execute_tx(tx)

    txn_hash = receipt.transactionHash.hex()
    return txn_hash

# tx = _mint('0x3cb2e8b6Da8b37e2b1eA55c6e54a3A0eA3270519', mint_arg)
# print(tx)

# def check_token_minted(txn_hash: str) -> int:
#      result = nft_module.get_abi_module().get_transfer_event(
#             txn_hash
#             ) 
#      print(result)

# check_token_minted(tx)
