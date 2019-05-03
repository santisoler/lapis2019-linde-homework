import time
import numpy as np


def GPR_forward_matrix(sources, boreholes_distance):
    dh = sources[1] - sources[0]
    receivers = sources.copy()
    n_sources = sources.size
    G = np.matrix(np.zeros((n_sources ** 2, n_sources)))
    for i, source in enumerate(sources):
        for j, receiver in enumerate(receivers):
            height = abs(source - receiver)
            if i == j:
                G[j + 6 * i, i] = boreholes_distance
            else:
                factor = np.sqrt(
                    1 + boreholes_distance ** 2 / height ** 2
                ) * dh
                for k in range(6):
                    kmin, kmax = min(i, j), max(i, j)
                    if k == kmin or k == kmax:
                        G[j + 6 * i, k] = 0.5 * factor
                    elif k > kmin and k < kmax:
                        G[j + 6 * i, k] = factor
    G = np.matrix(G)
    return G


def forward(G, porosity):
    # Convert the four porosities into 6 layers
    porosity_six_layers = np.zeros(6)
    porosity_six_layers[0] = porosity[0]
    porosity_six_layers[1] = porosity[0]
    porosity_six_layers[2] = porosity[1]
    porosity_six_layers[3] = porosity[2]
    porosity_six_layers[4] = porosity[2]
    porosity_six_layers[5] = porosity[3]
    # Convert porosity to slowness
    slowness = _porosity_to_slowness(porosity_six_layers)
    slowness = np.matrix(slowness).T
    times = G * slowness
    return times


def _porosity_to_slowness(porosity, kappa_s=5, kappa_w=81):
    # Convert porosities to slownesses
    c = 0.3  # speed of light in vacumm in m/ns
    kappa_sqrt = (
        (1 - porosity) * np.sqrt(kappa_s)
        + porosity * np.sqrt(kappa_w)
    )
    slowness = kappa_sqrt / c
    return slowness


def likelihood(G, porosity, times, sigma):
    # Get number of data values
    n_times = times.size
    # Calculate the difference between predicted and data
    difference = np.linalg.norm(forward(G, porosity) - times)
    likelihood = (
        (1 / np.sqrt(2 * np.pi) / sigma) ** n_times
        * np.exp(-0.5 * difference ** 2 / sigma ** 2)
    )
    return likelihood


def inverse_problem(G, times, sigma, supremum, iterations):
    n_accepted = 0
    accepted_porosities = np.zeros((iterations, 4))
    likelihoods = np.zeros(iterations)
    for i in range(iterations):
        # Draw a porosity array with uniform distribution between 0.2 and 0.4
        porosity = (0.4 - 0.2) * np.random.rand(4) + 0.2
        # Check if it should be rejected or accepted
        likelihoods[i] = likelihood(G, porosity, times, sigma)
        probability = likelihoods[i] / supremum
        if np.random.rand() < probability:
            accepted_porosities[n_accepted] = porosity
            n_accepted += 1
    accepted_porosities = accepted_porosities[:n_accepted]
    return accepted_porosities, likelihoods


# Define model
boreholes_distance = 4
sources = np.linspace(0.5, 5.5, 6)

# Get G matrix
G = GPR_forward_matrix(sources, boreholes_distance)

# Synthetic model
porosity = [0.2, 0.4, 0.2, 0.2]
times = forward(G, porosity)

# Inverse problem of synthetic
sigma = 1
supremum = 1e-21
iterations = 100000
start = time.time()
porosities, likelihoods = inverse_problem(G, times, sigma, supremum, iterations)
end = time.time()
print("Computation time: {}".format(end - start))
print(porosities.size)
