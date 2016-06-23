import random
import json
import os

def c_at_one(answers):
    '''Given an answers file, computes the c@1 measure

    # Arguments
        answers: file containing the probabilities for each problem

    # Returns
        c@1: the c@1 measure
    '''
    with open(answers) as f:
        lines = f.readlines()
    n = float(len(lines))
    probs = [float(line.split()[1]) for line in lines]
    n_c = sum(p < 0.5 for p in probs)
    n_u = 0  # glad does not support this feature
    return (1.0 / n) * (n_c + (n_u * n_c / n))

def sample(problems, num_obfuscations=2):
    result = []
    for _, dirs, _ in os.walk(problems):
        for dir in dirs:
            problem = os.path.join(problems, dir)
            obfuscation_file = problem + '/obfuscation.json'
            with open(obfuscation_file) as data_file:
                obfuscations = json.load(data_file)
                indices = random.sample(range(1, len(obfuscations)-1),
                                        num_obfuscations)
                selected_obfuscations = [obfuscations[i] for i in indices]
                for obs in selected_obfuscations:
                    obs['soundness'] = {'A': '', 'B': ''}
                    obs['sensibility'] = {'A': '', 'B': ''}
                    result.append(obs)
    filename = problems + 'result.json'
    json.dump(result, open(filename, 'wb'))
