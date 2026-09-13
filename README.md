# Numerical Analysis Activity 1

This Python program solves numerical equations using the **Bisection Method**. It prints the iteration tables and approximate roots for Problems 1, 2, and 3, then displays interactive Matplotlib plots for the roots found in Problem 3.

## Requirements

- Python 3.10 or newer
- NumPy
- Matplotlib

## Installation on Windows

1. Open PowerShell in this project folder.
2. Optional: create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the required packages:

   ```powershell
   python -m pip install numpy matplotlib
   ```

## Run the program

From the project folder, run:

```powershell
python ".\Ermita-4D- CS141-Act1-NumericalAnalysis.py"
```

If the `python` command is not available, use the Python launcher instead:

```powershell
py ".\Ermita-4D- CS141-Act1-NumericalAnalysis.py"
```

If neither command is recognized, run the file with the full path to your Python executable. For example:

```powershell
& "C:\Users\reah\AppData\Local\Programs\Python\Python314\python.exe" ".\Ermita-4D- CS141-Act1-NumericalAnalysis.py"
```

## What to expect

- The terminal displays the bisection iterations and calculated roots.
- Problem 3 intervals are scanned for sign changes before the roots are calculated.
- A window opens with three plots for the Problem 3 equations.
- Close the plot window after reviewing it so the program can finish.

## Project file

- `Ermita-4D- CS141-Act1-NumericalAnalysis.py` - main Python program
