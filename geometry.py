import typer
import math

app = typer.Typer()

# to run in terminal: python3 geometry.py --help

# 2D Geometry Formulas:
@app.command()
def square_perimeter(side: float, show_work: bool = False):
    if show_work:
        answer = side * 4
        print(f"Side * 4 = {side} * 4 = {answer:.2f}")
    else:
        print(f"{side * 4:.2f}")

@app.command()
def rectangle_perimeter(length: float, width: float, show_work: bool = False):
    if show_work:
        answer = 2 * (length + width)
        print(f"2 * (Length + Width) = 2 * ({length} + {width}) = {answer:.2f}")
    else:
        print(f"{2 * (length + width):.2f}")
    
@app.command()
def square_area(side: float, show_work: bool = False):
    if show_work:
        answer = side ** 2
        print(f"(Side)² = ({side})² = {answer:.2f}")
    else:
        print(f"{side ** 2:.2f}")

@app.command()
def rectangle_area(length: float, width: float, show_work: bool = False):
    if show_work:
        answer = length * width
        print(f"Length * Width = {length} * {width} = {answer:.2f}")
    else:
        print(f"{length * width:.2f}")

@app.command()
def triangle_area(base: float, height: float, show_work: bool = False):
    if show_work:
        answer = base * height * 0.5
        print(f"Base * Height * 0.5 = {base} * {height} * 0.5 = {answer:.2f}")
    else:
        print(f"{base * height * 0.5:.2f}")

@app.command()
def trapezoid_area(base1: float, base2: float, height: float, show_work: bool = False):
    if show_work:
        answer = (base1 + base2) * 0.5 * height
        print(f"(Base1 + Base2) * 0.5 * Height = ({base1} + {base2}) * 0.5 * {height} = {answer:.2f}")
    else:
        print(f"{(base1 + base2) * 0.5 * height:.2f}")

@app.command()
def circle_area(radius: float, show_work: bool = False):
    if show_work:
        answer = math.pi * (radius ** 2)
        print(f"π * (Radius)² = π * ({radius})² = {answer:.2f}")
    else:
        print(f"{math.pi * (radius ** 2):.2f}")

@app.command()
def circle_circumference(radius: float, show_work: bool = False):
    if show_work:
        answer = 2 * math.pi * radius
        print(f"2 * π * Radius = 2 * π * {radius} = {answer:.2f}")
    else:
        print(f"{2 * math.pi * radius:.2f}")

# 3D Geometry Formulas:
@app.command()
def cylinder_curved_surface_area(radius: float, height: float, show_work: bool = False):
    if show_work:
        answer = 2 * math.pi * radius * height
        print(f"2 * π * Radius * Height = 2 * π * {radius} * {height} = {answer:.2f}")
    else:
        print(f"{2 * math.pi * radius * height:.2f}")

@app.command()
def cylinder_total_surface_area(radius: float, height: float, show_work: bool = False):
    if show_work:
        answer = 2 * math.pi * radius * (radius + height)
        print(f"2 * π * Radius * (Radius + Height) = 2 * π * {radius} * ({radius} + {height}) = {answer:.2f}")
    else:
        print(f"{2 * math.pi * radius * (radius + height):.2f}")

@app.command()
def cylinder_volume(radius: float, height: float, show_work: bool = False):
    if show_work:
        answer = math.pi * (radius **2) * height
        print(f"π * (Radius)² * Height = π * ({radius})² * {height} = {answer:.2f}")
    else:
        print(f"{math.pi * (radius **2) * height:.2f}")

@app.command()
def cone_curved_surface_area(radius: float, slant_height: float, show_work: bool = False):
    if show_work:
        answer = math.pi * radius * slant_height
        print(f"π * Radius * Slant Height = π * {radius} * {slant_height} = {answer:.2f}")
    else:
        print(f"{math.pi * radius * slant_height:.2f}")

@app.command()
def cone_total_surface_area(radius: float, slant_height: float, show_work: bool = False):
    if show_work:
        answer = math.pi * radius * (radius + slant_height)
        print(f"π * Radius * (Radius + Slant Height) = π * {radius} * ({radius} + {slant_height}) = {answer:.2f}")
    else:
        print(f"{math.pi * radius * (radius + slant_height):.2f}")

@app.command()
def cone_volume(radius: float, height: float, show_work: bool = False):
    if show_work:
        answer = (1/3) * math.pi * (radius ** 2) * height
        print(f"(1/3) * π * (Radius)² * Height = (1/3) * π * ({radius})² * {height} = {answer:.2f}")
    else:
        print(f"{(1/3) * math.pi * (radius ** 2) * height:.2f}")

@app.command()
def sphere_surface_area(radius: float, show_work: bool = False):
    if show_work:
        answer = 4 * math.pi * (radius ** 2)
        print(f"4 * π * (Radius)² = 4 * π * ({radius})² = {answer:.2f}")
    else:
        print(f"{4 * math.pi * (radius ** 2):.2f}")

@app.command()
def sphere_volume(radius: float, show_work: bool = False):
    if show_work:
        answer = (4/3) * math.pi * (radius ** 3)
        print(f"(4/3) * π * (Radius)³ = (4/3) * π * ({radius})³ = {answer:.2f}")
    else:
        print(f"{(4/3) * math.pi * (radius ** 3):.2f}")

# can't have @app.command()'s under this:
if __name__ == "__main__":
    app()

# formulas: https://www.cuemath.com/geometry-formulas/
# to-do: install autocomplete and install a GUI (use turtle?)