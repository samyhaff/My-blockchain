import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash 
        self.hash = self.get_hach()

    def get_hach(self):
        sha = hasher.sha256()
        sha.update(str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + self.previous_hash.encode('utf-8'))
        return sha.hexdigest()

def next_block(previous_block, data):
    this_timestamp = date.datetime.now()
    this_data = data
    this_hash = previous_block.hash
    return Block(this_timestamp, this_data, this_hash)

def add_block(data):
    print("A new block containing \"" + data + "\" was added to the blockchain")
    previous_block = blockchain[-1]
    next_block(previous_block, data)

init_block = Block(date.datetime.now(), "Hello, ", "0")
blockchain = [init_block]
add_block("World!")

