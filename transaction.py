import random
random.seed(0)

#creating valid transactions in the range of 1 to maxValue
def makeTransaction(maxValue=3):
    
    #randomly choose -1 or 1
    sign = int(random.getrandbits(1)) * 2 - 1
    
    amount = random.randint(1, maxValue)
    alicePays = sign * amount
    bobPays = -1 * alicePays
    
    return {'Alice': alicePays, 'Bob': bobPays}

txnBuffer = [makeTransaction() for i in range(30)]

def updateState(txn, state):
    ''' 
    The inputs are dictionaries with the transfer amount (txn)
    or account balance (state).
    
    The returns are updated state with additional
    users if needed
    
    This does not validate the transaction, only
    updates the state. We validate in a
    separate function below
    '''
    
    # copy of state since dictionaries are mutable
    state = state.copy()
    
    for key in txn:
        # for exsisting users
        if key in state.keys():
            state[key] += txn[key]
        else:
            # adding new user to dictionary
            state[key] = txn[key]
    
    return state

def isValidTxn(txn, state):
    
    # checks that sum of deposits and withdralws is 0
    if sum(txn.values()) is not 0:
        return False
    
    # checks that transation does not create overdraft
    for key in txn.keys():
        if key in state.keys():
            acctBalance = state[key]
        else:
            # if new user, assume 0 balance
            acctBalance = 0
        
        if (acctBalance + txn[key] < 0):
            return False
        
    return True

