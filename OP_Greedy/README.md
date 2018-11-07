# Orienteering problem (OP)

Greedy aproximation to solve the OP

Recall the MIP formulation:

$Max \sum_{p=1}^{P}\sum_{i=2}^{N-1}S_i y_ip$
$\sum_{p=1}^{P}\sum_{j=2}^{N}x_{1jp} = \sum_{p=1}^{P}\sum_{i=1}^{N-1} x_{iNp} = P$
$\sum_{p=1}^{P}y_{kp} \leq 1, \forall k = 2,...,N-1$
$\sum_{i=1}^{N-1}x_{ikp}=\sum_{j=2}^{N}x_{kjp}=y_{kp},~\forall k=2,...,N-1,~\forall p=1,...,1$
$\sum_{i=1}^{N-1}\sum_{j=2}^{N}t_{ij}x_{ijp} \leq T_{max}$
$2 \leq u_{ip} \leq N,~\forall i=2,...,N,~\forall p=1,...,P$
$u_{ip}-u_{jp}+ \leq (N-1)(1-x_{ijp}),~\forall i,j=2,...,N,~\forall p=1,...,P$
$x_{ijp},y_{ip} \in \{0,1\},~\forall i,j=1,...,N,~\forall p =1,...,P$
