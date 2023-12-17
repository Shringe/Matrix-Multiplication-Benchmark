import numpy as np
from jax import numpy as jnp
import time
import sys


# measures total execution time
def totalTime(func):
    def totalTime_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time_milis = (end_time - start_time)*1000
        print("::"+str(total_time_milis))
        return result
    return totalTime_wrapper


# Numpy
@totalTime
def numpyMult(m1, m2):
    return np.matmul(m1, m2)

@totalTime
def numpyKronecker(m1, m2):
    return np.kron(m1, m2)
    
@totalTime
def numpyHadamard(m1, m2):
    return np.multiply(m1, m2)

# Jax
@totalTime
def jaxMult(m1, m2):
    return jnp.matmul(m1, m2)

@totalTime
def jaxKronecker(m1, m2):
    return jnp.kron(m1, m2)
    
@totalTime
def jaxHadamard(m1, m2):
    return jnp.multiply(m1, m2)


# matrices
kronDepth: int = int(sys.argv[1])
depth: int = kronDepth**2
print(f"kronecker matrix depth={kronDepth} regular matrix depth will be {depth}.")

m1 = np.random.random((depth, depth))
m2 = np.random.random((depth, depth))

m1k = np.random.random((kronDepth, kronDepth))
m2k = np.random.random((kronDepth, kronDepth))


# benchmarks
print("Numpy benchmarks =============")

numpyMult(m1, m2)
numpyKronecker(m1k, m2k)
numpyHadamard(m1, m2)

print("Jax benchmarks ===============")

jaxMult(m1, m2)
jaxKronecker(m1k, m2k)
jaxHadamard(m1, m2)
