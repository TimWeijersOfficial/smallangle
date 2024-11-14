import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def angle_group():
    pass

@angle_group.command()
@click.option(
"-n",
"--steps",
default=10,
)
def sin(steps):
    x = np.linspace(0, 2 * pi, steps)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@angle_group.command()
@click.option(
"-n",
"--steps",
default=10
)
def tan(steps):
    x = np.linspace(0, 2 * pi, steps)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    sin(10)