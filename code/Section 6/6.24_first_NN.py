import numpy as np

np.random.seed(1)

# Setze alle nicht positiven Zahlen auf 0
def relu(x):
    return (x > 0) * x


# Gebe 1 zurueck, wenn output groesse 0, ansonsten 0
def relu2deriv(output):
    return output > 0


streetlights = np.array([[1, 0, 1], [0, 1, 1], [0, 0, 1], [1, 1, 1]])

walk_vs_stop = np.array([[1, 1, 0, 0]]).T

# Bias
alpha = 0.2
# size of hidden_layer
hidden_size = 4

weights_0_1 = 2 * np.random.random((3, hidden_size)) - 1
weights_1_2 = 2 * np.random.random((hidden_size, 1)) - 1

for iteration in range(20):
    layer_2_error = 0
    for i in range(len(streetlights)):
        layer_0 = streetlights[i : i + 1]
        # gewichtete Summe zwischen layer_0 und Gewichten, mit negativen Werte auf 0 gesetzt
        layer_1 = relu(np.dot(layer_0, weights_0_1))
        # gewichtet Summe
        layer_2 = np.dot(layer_1, weights_1_2)
        # Fehlerberechnung, wie weit entfernt von richtigem Wert
        layer_2_error = layer_2_error + np.sum((layer_2 - walk_vs_stop[i : i + 1]) ** 2)
        # Abstand zwischen korrektem Wert und berechneten Wert fuer layer 2
        layer_2_delta = layer_2 - walk_vs_stop[i : i + 1]
        # Abstand zwischen korrektem Wert und berechneten Wert fuer layer 1
        layer_1_delta = layer_2_delta.dot(weights_1_2.T) * relu2deriv(layer_1)
        # anpassen der gewichte anhand des berechneten Abstands
        weights_1_2 = weights_1_2 - alpha * layer_1.T.dot(layer_2_delta)
        weights_0_1 = weights_0_1 - alpha * layer_0.T.dot(layer_1_delta)

    if iteration % 10 == 9:
        print(f"Fehler: {str(layer_2_error)}")
        print(f"layer_1: {layer_1}")
        print(f"Abstand layer_1: {layer_1_delta}")
        print(f"layer_2: {layer_2}")
        print(f"Abstand layer_2: {layer_2_delta}")
        print(f"layer_0: {layer_0}")
        print()
