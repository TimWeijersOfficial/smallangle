import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def angle_group():
    """prints sine or tangent values (depending on subcommand)
    of values between 0 and pi
    """    
    pass

@angle_group.command()
@click.option(
"-s",
"--steps",
default=10,
)
def sin(steps):
    """prints table of values between 0 and pi
    and their sine values

    Args:
        steps (int): amount of values between 0 and pi
    """    
    x = np.linspace(0, 2 * pi, steps)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@angle_group.command()
@click.option(
"-s",
"--steps",
default=10
)
def tan(steps):
    """prints table of values between 0 and pi 
        and their tangent values

    Args:
        steps (int): amount of values between 0 and pi
    """    
    x = np.linspace(0, 2 * pi, steps)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    sin(10)