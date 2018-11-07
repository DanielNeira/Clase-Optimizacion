# Orienteering problem (OP)

Greedy aproximation to solve the OP

Recall the MIP formulation:

In the OP, a set of $N$ vertices $i$ is given, each with a score S_{i}. The starting point (vertex 1) and the end point (vertex N) are fixed. The time tij needed to travel from vertex i to j is known for all vertices. Not all vertices can be visited since the available time is limited to a given time budget Tmax. The goal of the OP is to determine a path, limited by Tmax, that visits some of the vertices, in order to maxi- mise the total collected score. The scores are assumed to be en- tirely additive and each vertex can be visited at most once.
The OP can also be defined with the aid of a graph G=(V,A) where V={v_{1}, . . . , v_{N}} is the vertex set and A is the arc set. In this def- inition the nonnegative score Si is associated with each vertex vi 2 V and the travel time tij is associated with each arc a_{ij} A. The OP consists of determining a Hamiltonian path G’ ( G) over a sub- set of V, including preset start (v1) and end (vN) vertex, and having a length not exceeding Tmax, in order to maximise the total col- lected score. In most cases, the OP is defined as a path to be found between distinct vertices, rather than a circuit or tour (v1   vN). In many applications, however, v1 does coincide with vN. The differ- ence between both formulations is small. It is always possible to add a dummy arc between end and start vertex to turn a path problem into a circuit problem. Mansini et al. (2006) explicitly define the ‘‘tour orienteering problem” as an OP where the start and end vertex coincide.
Making use of the notation introduced above, the OP can be for- mulated as an integer problem. The following decision variables are used: xij = 1 if a visit to vertex i is followed by a visit to vertex j – 0 otherwise; ui = the position of vertex i in the path.

<img src="http://bit.ly/2PkRnCU" align="center" border="0" alt="Max \sum_{i=2}^{N-1}\sum_{j=2}^{N}S_i x_{ij} \\ \sum_{j=2}^{N}x_{1j} = \sum_{i=1}^{N-1} x_{iN} = 1\\\sum_{i=1}^{N-1}x_{ik}=\sum_{j=2}^{N}x_{kj} \leq 1,\forall k=2,...,N-1\\\sum_{i=1}^{N-1}\sum_{j=2}^{N}t_{ij}x_{ij} \leq T_{max}\\ 2 \leq u_{i} \leq N,\forall i=2,...,N\\u_{i}-u_{j}+ 1 \leq (N-1)(1-x_{ij}),\forall i,j=2,...,N\\x_{ij} \in {0,1},\forall i,j=1,...,N" width="300" height="296" />

The objective function (0) is to maximise the total collected score. Constraints (1) guarantee that the path starts in vertex 1 and ends in vertex N. Constraints (2) ensure the connectivity of the path and guarantee that every vertex is visited at most once. Constraint (3) ensures the limited time budget. Constraints (4) and (5) are nec- essary to prevent subtours. These subtour elimination constraints are formulated according to the Miller–Tucker–Zemlin (MTZ) for- mulation of the TSP (Miller et al., 1960).

(Pagina para instancias de OP)[https://www.mech.kuleuven.be/en/cib/op#section-2]
