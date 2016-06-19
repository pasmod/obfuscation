import json
import os


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


def write_obfuscation(problem):
    """Combines the obfuscations in a problem to a single one and writes
    the result to a text file

    # Arguments
        problem: problem containing the obfuscation.json file
    """
    obfuscation = reconstruct(problem)
    f = open('obfuscation.txt', 'w')
    f.write(obfuscation)
    f.close()

def write_obfuscations(path):
    """For all problems in the path, write the obfuscation file to the folder

    # Arguments
        path: path containing the results of participants
    """
    for _, dirs, _ in os.walk(path):
        for dir in dirs:
            problam_path = os.path.join(path, dir)
            write_obfuscation(problam_path)
