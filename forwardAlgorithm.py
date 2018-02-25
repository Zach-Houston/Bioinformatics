# This file is an example of getting the forward algorithm score in a FSM consisting of a loaded die and a fair die.
import random
# State class: Takes in two dictionaries containing transition and emission probabilities.
class State:
    def __init__(self, transitions, emissions):
        self.tran = transitions
        self.emis = emissions
# probabilities: Takes in a dictionary of probabilities and outputs a random result based on the dict.
def probabilities(prob_dict):
    random_value = random.random()
    total = 0
    for k,v in prob_dict.items():
        total += v
        if random_value <= total:
            return k
# forwardProbability: Use the Forward Algo to calculate probability of the sequence.  matrix[0] is fair and matrix[1] is loaded.  Also I'm really proud of how compact this code turned out to be!
def forwardProbability(seq, fair, loaded, begin):
    matrix = [[1],[0]]
    for i in range(len(seq)):
        matrix[0].append(fair.tran["fair"] * fair.emis[int(seq[i])] * matrix[0][i] + loaded.tran["fair"] * fair.emis[int(seq[i])] * matrix[1][i])
        matrix[1].append(loaded.tran["loaded"] * loaded.emis[int(seq[i])] * matrix[1][i] + fair.tran["loaded"] * loaded.emis[int(seq[i])] * matrix[0][i])
    return(matrix[0][-1] + matrix[1][-1])

#Initialize states
fair = State({"fair": 0.95, "loaded": 0.05}, {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6})
loaded = State({"fair": 0.1, "loaded": 0.9}, {1: 1/10, 2: 1/10, 3: 1/10, 4: 1/10, 5: 1/10, 6: 1/2})
begin = State({"fair": 1, "loaded": 0}, None)

# Forward Probability
file1 = open("file1.txt", 'r').read().strip()
print("File 1 Answer: ", forwardProbability(file1, fair, loaded, begin))
