from sklearn.metrics import auc


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


def auc(answers):
    '''Returns the AUC based on the probabilities given in answers

    # Arguments:
        answers: file containing the probabilities for each problem

    # Returns
        auc: aread under the curve
    '''
    with open(answers) as f:
        lines = f.readlines()
    probs = [float(line.split()[1]) for line in lines]
    y = [0] * len(probs)
    return auc(probs, y)
