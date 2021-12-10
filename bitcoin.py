from hashlib import sha256
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(block.encode("ascii")).hexdigest()

def mine(block_number, transcation_list, previous_hash, prefex_zeroes):
    prefix_str = "0" * prefex_zeroes
    for nonce in range(MAX_NONCE):
        text = str(block_number) + str(transcation_list) + str(previous_hash) + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Block found with nonce {nonce}")
            return new_hash
    
    raise BaseException(f"Could not find correct hash after {MAX_NONCE} tries")


if __name__ == "__main__":
    transcations = '''
    Dhaval->Bhavin->20,
    Manda->Cara->45
    '''
    difficulty = 5

    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5, transcations, '0000000xa036944e29568d0cff17edbe038f81208fecf9166be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"Total time taken to mine: {total_time}")
    print(f"Hash: {new_hash}")
