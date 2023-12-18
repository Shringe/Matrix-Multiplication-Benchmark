# Matrix-Multiplication-Benchmark
Performs Hadamard, Kronecker, and matrix multiplication, then plots on bar graph.

# Installation
```
git clone https://github.com/Shringe/Matrix-Multiplication-Benchmark
cd Matrix-Multiplication-Benchmark

source venv/bin/activate # replace activate for corresponding shell e.x. activate.fish for fish
pip install -r requirements.txt
```
Make sure to compile the Java benchmark as well.

# Usage
```
python plot.py
```

# Java benchmark compilation
In order to compile the Java benchmark:
```
cd JavaBenchmark/ && ./mvnw clean package && cd -
```
