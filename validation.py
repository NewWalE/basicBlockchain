import hash, transaction, json

def checkBlockHash(block):
    # checkes to ensure the hash matches the block contents
    expectedHash = hash.hashMe(block['contents'])
    
    if block['hash'] != expectedHash:
        raise Exception('Hash does not match contents of block {}'.format(block['contents']['blockNumber']))
    
    return
    
def checkBlockValidty(block, parent, state):
    parentNumber = parent ['contents']['blockNumber']
    parentHash = parent['hash']
    blockNumber = block['contents']['blockNumber']
    
    for txn in block['contents']['txns']:
        if transaction.isValidTxn(txn, state):
            state = transaction.updateState(txn, state)
        else:
            raise Exception('Invalid transaction in block %s: %s' % (blockNumber, txn))
        
    checkBlockHash(block)
    
    if blockNumber != (parentNumber + 1):
        raise Exception(f'Hash does not match contents of block {blockNumber}')
    
    if block['contents']['parentHash'] != parentHash:
        raise Exception(f'Parent hash not accurate at block {blockNumber}')
    
    return state

def checkChain(chain):
    
    if type(chain) == str:
        try:
            chain = json.loads(chain)
            assert(type(chain) == list)
        except:
            return False
    elif type(chain) != list:
        return False
    
    state = {}
    
    for txn in chain[0]['contents']['txns']:
        state = transaction.updateState(txn, state)
        
    checkBlockHash(chain[0])
    parent = chain[0]
    
    for block in chain[1:]:
        state = checkBlockValidty(block, parent, state)
        parent = block
    
    return state 