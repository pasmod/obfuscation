from collections import OrderedDict
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


A = 'results/author-masking-participantA-2016-05-24-04-49-53/output'
B = 'results/author-masking-participantB-2016-05-24-16-57-58/output'
C = 'results/author-masking-participantC-2016-06-02-11-02-18/output'

# DIRTY CODE! CLEAN IT
def sample(problems=A, num_obfuscations=2):
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
                    obs['problem'] = problem[-11:]
                    result.append(obs)
    filename = problems + '/result.json'
    json.dump(result, open(filename, 'wb'))

# DIRTY CODE! CLEAN IT
def guidline(submissions=['results/author-masking-participantA-2016-05-24-04-49-53/output',
                          'results/author-masking-participantB-2016-05-24-16-57-58/output',
                          'results/author-masking-participantC-2016-06-02-11-02-18/output'],
             num_problems=20,
             num_obfuscations=3):
    result = []
    for submission in submissions:
        for _, dirs, _ in os.walk(submission):
            if len(dirs) == 0:
                continue
            indices = random.sample(range(1, len(dirs)-1),
                                    num_problems)
            selected_problems = [dirs[i] for i in indices]
            for dir in selected_problems:
                problem = os.path.join(submission, dir)
                obfuscation_file = problem + '/obfuscation.json'
                with open(obfuscation_file) as data_file:
                    obfuscations = json.load(data_file,
                                             object_pairs_hook=OrderedDict)
                    indices = random.sample(range(1, len(obfuscations)-1),
                                            num_obfuscations)
                    selected_obfuscations = [obfuscations[i] for i in indices]
                    for obs in selected_obfuscations:
                        obs['soundness'] = ''
                        obs['sensibility'] = ''
                        obs['problem'] = problem[-11:]
                        obs['submission'] = submission[23:-27]
                        result.append(obs)
    filename = 'results/guidline.json'
    json.dump(result, open(filename, 'wb'), sort_keys=False)
