import hash, transaction, json

#genesis block creation
#initial state
state = {'Alice': 50, 'Bob': 50}

genesisBlockTxns = [state]
genesisBlockContents = {'blockNumber': 0, 'parentHash': None, 
                        'txnCount': 1, 'txns': genesisBlockTxns}
genesisHash = hash.hashMe(genesisBlockContents)
genesisBlock = {'hash': genesisHash, 'contents': genesisBlockContents}
genesisBlockStr = json.dumps(genesisBlock, sort_keys=True)

chain = [genesisBlock]

def makeBlock(txns, chain):
    parentBlock = chain[-1]
    parentHash = parentBlock['hash']
    blockNumber = parentBlock['contents']['blockNumber'] + 1
    
    txnCount = len(txns)
    
    blockContents = {'blockNumber': blockNumber, 'parentHash': parentHash,
                     'txnCount': len(txns), 'txns': txns}
    blockHash = hash.hashMe(blockContents)
    block = {'hash': blockHash, 'contents': blockContents}
    
    return block

#arbitrary number of tranactions per block
blockSizeLimit = 5

while len(transaction.txnBuffer) > 0:
    bufferStartSize = len(transaction.txnBuffer)
    
    