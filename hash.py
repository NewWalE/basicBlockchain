import hashlib, json, sys

def hashMe(msg=""):
    # Helper function wrapping our hashing algorithm
    if type(msg) != str:
        msg = json.dumps(msg, sort_keys=True)
        # Sorting keys ensures repeatability
    
    if sys.version_info.major == 2:
        return hashlib.sha256(msg).hexdigest().decode('utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()
