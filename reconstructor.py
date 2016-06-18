import json


def reconstruct(problem):
    '''Given a problem folder, concatenates all obfuscations insides the
    obfuscation.json file and returns the obfuscated document.

    # Arguments
        problem: folder containing the obfuscation.json file

    # Returns
        x: obfuscated document as string
    '''
    obfuscation_file = problem + '/obfuscation.json'
    with open(obfuscation_file) as data_file:
        obfuscations = json.load(data_file)
    docs = [o['obfuscation'] for o in obfuscations]
    return "".join(docs)
