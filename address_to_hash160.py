# Install bech32 if you don't have it: pip install bech32
from bit import base58
from bech32 import bech32_decode, convertbits

def convert_to_hash160(address):
    try:
        if address.startswith('tb1'):
            hrp, data = bech32_decode(address)
            if not data:
                raise ValueError("Invalid Bech32 address")
            print("hrp:", hrp)  # Debugging
            print("data:", data)  # Debugging
            converted = convertbits(data, 5, 8, True)
            print("converted:", converted)  # Debugging
            decoded = bytes(converted)
        else:
            decoded = base58.b58decode_check(address)

        hash160 = decoded[1:]
        return hash160.hex()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    testnet_address = input("Enter your testnet Bitcoin address: ")
    hash160_address = convert_to_hash160(testnet_address)
    print("Hash160 format:", hash160_address)
