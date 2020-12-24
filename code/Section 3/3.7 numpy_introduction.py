import numpy as np


def neural_network(input, weight):
    prediction = input.dot(weight)

    return prediction


if __name__ == "__main__":
    weights = np.array([0.1, 0.2, 0.0])
    number_of_toes = np.array([8.5, 9.5, 9.9, 9.0])
    wlrec = np.array([0.65, 0.8, 0.8, 0.9])
    nfans = np.array([1.2, 1.3, 0.5, 1.0])
    input = np.array([number_of_toes[0], wlrec[0], nfans[0]])
    pred = neural_network(input, weights)
    print(pred)
