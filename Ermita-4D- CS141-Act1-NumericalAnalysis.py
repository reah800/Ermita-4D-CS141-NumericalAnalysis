"""
REAHLYN S. ERMITA - CS4D NUMERICAL ANALYSIS ACT1    

"""

import math
import numpy as np
import matplotlib.pyplot as plt


# Core Bisection Method function (used for every sub-problem below)
def bisection_method(f, a, b, decimal_places, label="", max_iter=200):

    fa = f(a)
    fb = f(b)

    print(f"\n===== {label} =====")
    print(f"Initial interval: [a, b] = [{a}, {b}]")
    print(f"f(a) = {fa:.6f},  f(b) = {fb:.6f},  f(a)*f(b) = {fa*fb:.6f}")

    #Sign-change check (Intermediate Value Theorem) If f(a) and f(b) have the SAME sign, there is no guarantee of a root, inside [a, b], so the Bisection Method cannot be started safely.
    if fa * fb >= 0:
        raise ValueError(
            f"f(a) and f(b) do not have opposite signs for {label}. "
            "Choose a different starting interval."
        )
    print("Sign-change condition f(a)*f(b) < 0 is satisfied -> a root exists in [a,b].\n")

    
    tol = 0.5 * 10 ** (-decimal_places)

    print(f"{'Iter':>4} | {'a':>12} | {'b':>12} | {'c (midpoint)':>14} | "
          f"{'f(c)':>12} | {'error = (b-a)/2':>16}")
    print("-" * 82)

    c = a  
    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0          # midpoint of current interval
        fc = f(c)                  # function value at midpoint
        error = (b - a) / 2.0      # current guaranteed error bound

        
        print(f"{i:>4} | {a:>12.8f} | {b:>12.8f} | {c:>14.8f} | "
              f"{fc:>12.3e} | {error:>16.3e}")

        
        if error < tol or fc == 0:
            break

       
        if fa * fc < 0:
          
            b = c
            fb = fc
        else:
          
            a = c
            fa = fc

    print("-" * 82)
    print(f"Result: root ~ {c:.{decimal_places}f}   (found in {i} iterations)")
    return c, i

#Small helper explanation.
def print_explanation(label, root, decimal_places, equation_text):
    print(f"\nWhy this is the correct root for {label}:")
    print(f"  The Bisection Method keeps halving an interval [a,b] on which the")
    print(f"  continuous function f changes sign (f(a)*f(b) < 0). By the")
    print(f"  Intermediate Value Theorem, a root of f must lie inside every one")
    print(f"  of those shrinking sub-intervals. Once the interval width is below")
    print(f"  the tolerance 0.5x10^-{decimal_places}, the midpoint c = {root:.{decimal_places}f}")
    print(f"  is guaranteed to be within {0.5*10**(-decimal_places):.1e} of the true root of")
    print(f"  {equation_text}, i.e. correct to {decimal_places} decimal places.")


#PROBLEM 1 : Bisection Method, roots correct to SIX decimal places
print("\n" + "-" * 82)
print("--- PROBLEM 1  (accuracy: 6 correct decimal places)")
print("-" * 82)

# Problem 1(a): x^3 = 9  -->  f(x) = x^3 - 9
f1a = lambda x: x**3 - 9
root_1a, _ = bisection_method(f1a, 2, 3, 6, label="Problem 1(a): x^3 = 9")
print_explanation("1(a)", root_1a, 6, "x^3 - 9 = 0")

# Problem 1(b): 3x^3 + x^2 = x + 5  -->  f(x) = 3x^3+x^2-x-5 
f1b = lambda x: 3*x**3 + x**2 - x - 5
root_1b, _ = bisection_method(f1b, 1, 1.5, 6, label="Problem 1(b): 3x^3+x^2 = x+5")
print_explanation("1(b)", root_1b, 6, "3x^3+x^2-x-5 = 0")

# Problem 1(c): cos^2(x) + 6 = x  -->  f(x)=cos^2x+6-x
f1c = lambda x: math.cos(x)**2 + 6 - x
root_1c, _ = bisection_method(f1c, 6, 7, 6, label="Problem 1(c): cos^2(x)+6 = x")
print_explanation("1(c)", root_1c, 6, "cos^2(x)+6-x = 0")


#PROBLEM 2 : Bisection Method, roots correct to EIGHT decimal places
print("\n" + "-" * 82)
print("--- PROBLEM 2  (accuracy: 8 correct decimal places)")
print("-" * 82)

# Problem 2(a): x^5 + x = 1  -->  f(x)=x^5+x-1
f2a = lambda x: x**5 + x - 1
root_2a, _ = bisection_method(f2a, 0, 1, 8, label="Problem 2(a): x^5 + x = 1")
print_explanation("2(a)", root_2a, 8, "x^5+x-1 = 0")

# Problem 2(b): sin(x) = 6x + 5  -->  f(x)=sinx-6x-5
f2b = lambda x: math.sin(x) - 6*x - 5
root_2b, _ = bisection_method(f2b, -1, -0.9, 8, label="Problem 2(b): sin(x) = 6x+5")
print_explanation("2(b)", root_2b, 8, "sin(x)-6x-5 = 0")

# Problem 2(c): ln(x) + x^2 = 3  -->  f(x)=lnx+x^2-3
f2c = lambda x: math.log(x) + x**2 - 3
root_2c, _ = bisection_method(f2c, 1, 2, 8, label="Problem 2(c): ln(x)+x^2 = 3")
print_explanation("2(c)", root_2c, 8, "ln(x)+x^2-3 = 0")


#PROBLEM 3 : Locate ALL solutions, then find each root to 6 decimal places
print("\n" + "-" * 82)
print("--- PROBLEM 3  (locate all roots, accuracy: 6 correct decimal places)")
print("-" * 82)


def scan_for_sign_changes(f, lo, hi, step):
    intervals = []
    x = lo
    f_prev = f(x)
    while x < hi:
        x_next = round(x + step, 10)
        f_next = f(x_next)
        if f_prev == 0 or f_next == 0 or f_prev * f_next < 0:
            intervals.append((x, x_next))
        f_prev = f_next
        x = x_next
    return intervals


# Problem 3(a): 2x^3 - 6x - 1 = 0
f3a = lambda x: 2*x**3 - 6*x - 1
print("\n--- Problem 3(a): 2x^3 - 6x - 1 = 0 ---")
print("Scanning x in [-3, 3] in steps of 0.5 to locate sign changes:")
found_3a = scan_for_sign_changes(f3a, -3, 3, 0.5)
print("Sub-intervals with a sign change:", found_3a)
intervals_3a = [(-2, -1), (-1, 0), (1, 2)]
roots_3a = []
for k, (a, b) in enumerate(intervals_3a, start=1):
    r, _ = bisection_method(f3a, a, b, 6, label=f"Problem 3(a) - root #{k}")
    roots_3a.append(r)
print(f"\nAll three roots of 2x^3-6x-1=0 (each from a length-1 interval): "
      f"{[f'{r:.6f}' for r in roots_3a]}")
print_explanation("3(a) roots", roots_3a[-1], 6, "2x^3-6x-1 = 0 (each interval)")

# Problem 3(b): e^(x-2) + x^3 - x = 0 
f3b = lambda x: math.exp(x - 2) + x**3 - x
print("\n--- Problem 3(b): e^(x-2) + x^3 - x = 0 ---")
print("Scanning x in [-3, 3] in steps of 0.1 to locate sign changes:")
found_3b = scan_for_sign_changes(f3b, -3, 3, 0.1)
print("Sub-intervals with a sign change:", found_3b)
intervals_3b = [(-2, -1), (-0.5, 0.5), (0.5, 1.5)]
roots_3b = []
for k, (a, b) in enumerate(intervals_3b, start=1):
    r, _ = bisection_method(f3b, a, b, 6, label=f"Problem 3(b) - root #{k}")
    roots_3b.append(r)
print(f"\nAll three roots of e^(x-2)+x^3-x=0 (each from a length-1 interval): "
      f"{[f'{r:.6f}' for r in roots_3b]}")
print_explanation("3(b) roots", roots_3b[-1], 6, "e^(x-2)+x^3-x = 0 (each interval)")

# Problem 3(c): 1 + 5x - 6x^3 - e^(2x) = 0 
f3c = lambda x: 1 + 5*x - 6*x**3 - math.exp(2*x)
print("\n--- Problem 3(c): 1 + 5x - 6x^3 - e^(2x) = 0 ---")
print("Scanning x in [-3, 3] in steps of 0.1 to locate sign changes:")
found_3c = scan_for_sign_changes(f3c, -3, 3, 0.1)
print("Sub-intervals with a sign change:", found_3c)
intervals_3c = [(-1.5, -0.5), (-0.5, 0.5), (0.3, 1.3)]
roots_3c = []
for k, (a, b) in enumerate(intervals_3c, start=1):
    r, _ = bisection_method(f3c, a, b, 6, label=f"Problem 3(c) - root #{k}")
    roots_3c.append(r)
print(f"\nAll three roots of 1+5x-6x^3-e^(2x)=0 (each from a length-1 interval): "
      f"{[f'{r:.6f}' for r in roots_3c]}")
print_explanation("3(c) roots", roots_3c[-1], 6, "1+5x-6x^3-e^(2x) = 0 (each interval)")


#SUMMARY
print("\n" + "-" * 82)
print("--- SUMMARY OF ALL RESULTS ---")
print("-" * 82)
print(f"1(a) x^3=9                        -> root = {root_1a:.6f}")
print(f"1(b) 3x^3+x^2=x+5                 -> root = {root_1b:.6f}")
print(f"1(c) cos^2x+6=x                   -> root = {root_1c:.6f}")
print(f"2(a) x^5+x=1                      -> root = {root_2a:.8f}")
print(f"2(b) sinx=6x+5                    -> root = {root_2b:.8f}")
print(f"2(c) lnx+x^2=3                    -> root = {root_2c:.8f}")
print(f"3(a) 2x^3-6x-1=0                  -> roots = {[f'{r:.6f}' for r in roots_3a]}")
print(f"3(b) e^(x-2)+x^3-x=0              -> roots = {[f'{r:.6f}' for r in roots_3b]}")
print(f"3(c) 1+5x-6x^3-e^(2x)=0           -> roots = {[f'{r:.6f}' for r in roots_3c]}")
print("-" * 82 + "\n")


#INTERACTIVE MATPLOTLIB SKETCHES 
def show_problem3_plots():
    print("-" * 82)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))
    colors = ['#FFA07A', '#98FB98', '#DDA0DD']

    # Subplot 3(a)
    x_a = np.linspace(-2.5, 2.5, 500)
    y_a = 2 * x_a**3 - 6 * x_a - 1
    ax = axes[0]
    ax.plot(x_a, y_a, 'b-', label=r'$f(x) = 2x^3 - 6x - 1$', linewidth=2)
    ax.axhline(0, color='black', linestyle='--', linewidth=0.8)
    for (a, b), col in zip(intervals_3a, colors):
        ax.axvspan(a, b, alpha=0.25, color=col, label=f'Interval [{a}, {b}] (len 1)')
    for r in roots_3a:
        ax.plot(r, 0, 'ro', markersize=6)
        ax.annotate(f'{r:.4f}', (r, 0), textcoords='offset points',
                    xytext=(0, 10), ha='center', fontsize=9, fontweight='bold', color='darkred')
    ax.set_title('Problem 3(a): $2x^3 - 6x - 1 = 0$', fontsize=12, fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_ylim(-15, 15)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(fontsize=8, loc='upper left')

    # Subplot 3(b)
    x_b = np.linspace(-2.5, 2.0, 500)
    y_b = np.exp(x_b - 2) + x_b**3 - x_b
    ax = axes[1]
    ax.plot(x_b, y_b, 'b-', label=r'$f(x) = e^{x-2} + x^3 - x$', linewidth=2)
    ax.axhline(0, color='black', linestyle='--', linewidth=0.8)
    for (a, b), col in zip(intervals_3b, colors):
        ax.axvspan(a, b, alpha=0.25, color=col, label=f'Interval [{a}, {b}] (len 1)')
    for r in roots_3b:
        ax.plot(r, 0, 'ro', markersize=6)
        ax.annotate(f'{r:.4f}', (r, 0), textcoords='offset points',
                    xytext=(0, 10), ha='center', fontsize=9, fontweight='bold', color='darkred')
    ax.set_title('Problem 3(b): $e^{x-2} + x^3 - x = 0$', fontsize=12, fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_ylim(-10, 10)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(fontsize=8, loc='upper left')

    # Subplot 3(c)
    x_c = np.linspace(-1.8, 1.2, 500)
    y_c = 1 + 5 * x_c - 6 * x_c**3 - np.exp(2 * x_c)
    ax = axes[2]
    ax.plot(x_c, y_c, 'b-', label=r'$f(x) = 1 + 5x - 6x^3 - e^{2x}$', linewidth=2)
    ax.axhline(0, color='black', linestyle='--', linewidth=0.8)
    for (a, b), col in zip(intervals_3c, colors):
        ax.axvspan(a, b, alpha=0.25, color=col, label=f'Interval [{a}, {b}] (len 1)')
    for r in roots_3c:
        ax.plot(r, 0, 'ro', markersize=6)
        ax.annotate(f'{r:.4f}', (r, 0), textcoords='offset points',
                    xytext=(0, 10), ha='center', fontsize=9, fontweight='bold', color='darkred')
    ax.set_title('Problem 3(c): $1 + 5x - 6x^3 - e^{2x} = 0$', fontsize=12, fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_ylim(-15, 15)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(fontsize=8, loc='upper left')

    plt.tight_layout()
    plt.show()

# Show interactive plot window
show_problem3_plots()
