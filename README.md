# chaotic
3D Phase Space Visualization of a Quantum Random Number Generator (work in progress...)

Borrowed from the field of nonlinear dynamical systems analysis (chaos theory), [phase space analysis](https://en.wikipedia.org/wiki/Phase_space) is used to find [attractors](https://en.wikipedia.org/wiki/Attractor) / [limit cycles](https://en.wikipedia.org/wiki/Limit_cycle) within highly entropic datasets. The method of phase space reconstruction currently used by this tool is based on the [Takens' delay embedding theorem](https://en.wikipedia.org/wiki/Takens%27s_theorem), using a default lag length of 2 and embedding dimension of 3. Both variables are configurable for purposes of creating the reconstruction plot. In essense, the stream of RNG-derived values are treated as a time-series sequence which are then used as x/y/z coordinate vectors to create a navigable 3D point cloud / scatter plot that represents all observed states of the dynamical system.

A lot of assumptions are being made about the true randomness of quantum systems without any real testing, so this is the result of a few day quarantine sprint to see if any visual indicators of a pattern (attractors) emerge from repeated sampling of a 15 qubit Hadamard gate quantum Random Number Generator (RNG) circuit running on IBM's quantum computer in Melbourne (ibmq_16_melbourne).

The back-of-the-beverage-napkin theory is, any discernible attractor that shows up from repeated observations of a quantum process could then potentially be predicted with artificial neural network function approximation. Which would break a lot of things such as Einstein's general relativity. And perhaps open the door for superluminal communications via quantum entanglement.

To use this tool, your input dataset should be a simple text file with one value per line, int or float. Requires the Mayavi scientific visualization suite. The resulting 3D cube can be mouse rotated / pan / zoom etc to interactively explore the plotted point cloud.

```
$ sudo apt update && sudo apt -y install mayavi2
$ for n in {1..10}; do python3 qRNG.py ibmq_16_melbourne >> melbourne_15.txt; done
$ python3 chaotic.py melbourne_15.txt -i
```

[May 8, 2020 Update]

After experimenting with a couple of different methods of arranging the results from the H-gate RNG, there are apparent striding patterns that emerge from IBM's 15 qubit quantum computer ibmq_16_melbourne. Doesn't appear to be an issue with phase space representation of the dataset, as using a cryptographically strong PRNG from Python's secrets library does not result in those same patterns, and the patterns seem too uniformly distributed to be attributed to quantum noise.

434176 int8 values in int8 phase space from ibmq_16_melbourne (8 qubit H-gate RNG sampling), lag = 2 embed = 3:

[8 qubit YouTube video](https://www.youtube.com/watch?v=ha3QuNymHPg&list=PLmvtGH47UObJrzqodX92Ts8d4WSn-R4kX)

![ibmq_16_melbourne 8-bit screenshot](https://github.com/GregoryVPerry/chaotic/raw/master/melbourne_8bit.png "chaotic: 8-bit dataset from ibmq_16_melbourne")

1040384 15-bit values in phase space from ibmq_16_melbourne (15 qubit H-gate RNG sampling), lag = 2 embed = 3:

[15 qubit YouTube video](https://youtu.be/TaBDv-PYDeU&list=PLmvtGH47UObJrzqodX92Ts8d4WSn-R4kX)

![ibmq_16_melbourne 15-bit screenshot](https://github.com/GregoryVPerry/chaotic/raw/master/melbourne_15bit.png "chaotic: 15-bit dataset from ibmq_16_melbourne")

1040384 15-bit values from Python's cryptographic secrets library, lag = 2 embed = 3:

[Python secrets lib YouTube video](https://youtu.be/432sV0NgdiU&list=PLmvtGH47UObJrzqodX92Ts8d4WSn-R4kX)

![python secrets library 15-bit screenshot](https://github.com/GregoryVPerry/chaotic/raw/master/python_secrets_prng_15bit.png "chaotic: 15-bit dataset from python secrets library")
