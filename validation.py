import hash

def checkBlockHash(block):
    # checkes to ensure the hash matches the block contents
    expectedHash = hash.hashMe(block['contents'])
    
    if block['hash'] != expectedHash:
        raise Exception('Hash does not match contents of block {}'.format(block['contents']['blockNumber']))
    
    return
    
def checkBlockValidty(block, parent, state):
    return

def checkChain(chain):
    return