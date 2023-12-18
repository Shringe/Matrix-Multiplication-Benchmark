import platform
import sys
import psutil
import subprocess
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('QtAgg')


def plotOutput(values: list):
    # color values
    colorMap: dict = {
        "Numpy": "#306998",
        "Jax": "#2c3196",
        "EJML": "#f89820"
    }

    # bar labels
    labels = ["Numpy matmult", "Numpy Kronecker", "Numpy Hadamard",
              "Jax matmult", "Jax Kronecker", "Jax Hadamard",
              "EJML Kronecker", "EJML Hadamard"]

    # set colors
    colors = list(range(len(labels) - 1))

    colors[:3] = [colorMap["Numpy"]] * 3
    colors[3:6] = [colorMap["Jax"]] * 3
    colors[6:8] = [colorMap["EJML"]] * 3

    # order to stack on chart
    order = list(range(1, len(labels) + 1))

    # creating chart
    plt.barh(order, values, tick_label=labels, color=colors, zorder=3)


    # grid formatting
    plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(200))
    plt.gca().xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(100))
    plt.grid(True, "major", 'x', zorder=0)


    plt.xlabel("Time in milliseconds")
    plt.ylabel("Matrix multiplication methods")
    plt.show()


def gatherBenchmark(python: str, java: str, kronMatrixSize: int, jvmWarmUpCycles: int) -> list:
    # default venv verion, python 3.11
    pythonResult: list = subprocess.run([sys.executable, python, str(kronMatrixSize)], stdout=subprocess.PIPE, text=True).stdout.splitlines()

    # default system version, tested with OpenJDK21
    javaVersion: str = "java"
    javaResult: list = subprocess.run([javaVersion, "-jar", java, str(kronMatrixSize), str(jvmWarmUpCycles)], stdout=subprocess.PIPE, text=True).stdout.splitlines()

    # filtering out output prefixed with '::', for benchmark values
    finalResult: list = ([float(r[2:]) for r in pythonResult if r.startswith("::")] +
                         [float(r[2:]) for r in javaResult if r.startswith("::")])
    # print(finalResult)
    return finalResult


if __name__ == "__main__":
    systemInfo: dict = {
        "OS": platform.system(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "memory": str(round(psutil.virtual_memory().total / (1024.0 ** 3)))+"GB" # memory in GB
    }
    print(systemInfo)

    values = gatherBenchmark("pythonBenchmark.py", "JavaBenchmark/target/JavaBenchmark-jar-with-dependencies.jar", 100, 3)
    plotOutput(values)
