from collections import OrderedDict
import random
import codecs
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
    n_u = sum(p == 0.5 for p in probs)
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
                    obs['sensibleness'] = {'A': '', 'B': ''}
                    obs['problem'] = problem[-11:]
                    result.append(obs)
    filename = problems + '/sensiblenes_team_a.json'
    json.dump(result, open(filename, 'wb'))

# DIRTY CODE! CLEAN IT
def guidline(submissions=[
                          #'results/author-masking-participantA-2016-05-24-04-49-53/output'
                          #'results/author-masking-participantB-2016-05-24-16-57-58/output',
                          'results/author-masking-participantC-2016-06-02-11-02-18/output'
                         ],
             num_problems=20,
             num_obfuscations=3,
             seed=123):
    result = []
    random.seed(seed)
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
                        obs['1_obfuscation'] = obs['obfuscation']
                        obs['2_sensibleness'] = ''
                        obs['3_obfuscation-id'] = obs['obfuscation-id']
                        obs['4_original-end-charpos'] = obs['original-end-charpos']
                        obs['5_original-start-charpos'] = obs['original-start-charpos']
                        obs.pop('original', None)
                        obs.pop('original-end-charpos', None)
                        obs.pop('original-start-charpos', None)
                        obs.pop('original', None)
                        obs.pop('obfuscation-id', None)
                        obs.pop('obfuscation', None)
                        obs['problem'] = problem[-11:]
                        obs['submission'] = submission[23:-27]
                        result.append(obs)
    filename = 'results/sensibleness_team_c.json'
    json.dump(result, open(filename, 'wb'), sort_keys=False, indent=4)

def clean(text):
    return text.replace('\n', ' ').replace('\r', '').replace('\t', ' ').strip()

def create_pairs(submission):
    pairs = []
    for _, dirs, _ in os.walk(submission):
        for dir in dirs:
            problem = os.path.join(submission, dir)
            obfuscation_file = problem + '/obfuscation.json'
            with open(obfuscation_file) as data_file:
                obfuscations = json.load(data_file)
            for obfuscation in obfuscations:
                pair = (clean(obfuscation['obfuscation']), clean(obfuscation['original']))
                pairs.append(pair)
    the_file = codecs.open("pairs.txt", "w", "utf-8")
    for pair in pairs:
        the_file.write(pair[0])
        the_file.write('\t')
        the_file.write(pair[1])
        the_file.write('\n')
    the_file.close()


def merge(file1, file2):
    merged = []
    with open(file1) as f1:
         eval1= json.load(f1, object_pairs_hook=OrderedDict)
    with open(file2) as f2:
         eval2= json.load(f2, object_pairs_hook=OrderedDict)
    for i in range(0, len(eval1)):
        new_dic = {}
        new_dic['obfuscation'] = eval1[i]['1_obfuscation']
        new_dic['sensibleness'] = {'A': eval1[i]['2_sensibleness'], 'B': eval2[i]['2_sensibleness']}
        new_dic['obfuscation-id'] = eval1[i]['3_obfuscation-id']
        new_dic['original-end-charpos'] = eval1[i]['4_original-end-charpos']
        new_dic['original-start-charpos'] = eval1[i]['5_original-start-charpos']
        new_dic['problem'] = eval1[i]['problem']
        new_dic['submission'] = eval1[i]['submission']
        merged.append(new_dic)
    filename = 'results/sensibleness_team_a.json'
    json.dump(merged, open(filename, 'wb'), sort_keys=False, indent=4)


def ia(file):
    values = []
    with open(file) as f:
         evaluations= json.load(f, object_pairs_hook=OrderedDict)
    for evaluation in evaluations:
        a = evaluation['sensibleness']['A']
        b = evaluation['sensibleness']['B']
        values.append((a, b))
    the_file = codecs.open("sensibleness_team_c.csv", "w", "utf-8")
    for value in values:
        the_file.write(value[0])
        the_file.write(',')
        the_file.write(value[1])
        the_file.write('\n')
    the_file.close()




