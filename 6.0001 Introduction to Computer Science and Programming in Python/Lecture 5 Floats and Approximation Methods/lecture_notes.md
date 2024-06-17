### Summary of Learned Concepts in Computer Science: Newton–Raphson Method

#### Newton–Raphson Method
The Newton–Raphson method, commonly attributed to Isaac Newton, is a widely used approximation algorithm. It is particularly effective for finding the real roots of functions, specifically polynomials with one variable. The method can be extended to polynomials with multiple variables both mathematically and algorithmically.

#### Polynomials and Roots
A polynomial with one variable, typically denoted as \( x \), is defined as either zero or the sum of a finite number of nonzero terms. Each term is composed of a constant coefficient multiplied by the variable raised to a nonnegative integer exponent, which is called the degree of the term. The degree of the polynomial is the highest degree of any of its terms. For example, the polynomial \( 3x^2 + 2x + 3 \) has terms of degrees 2, 1, and 0, respectively, making the polynomial's degree 2.

A root of a polynomial \( p \) is a real number \( r \) such that \( p(r) = 0 \). For instance, finding the square root of 24 can be framed as finding \( x \) such that \( x^2 - 24 \approx 0 \).

#### Newton’s Theorem
Newton's theorem provides that if a value, referred to as \( \text{guess} \), is an approximation of a root of a polynomial, then the value \( \text{guess} - \frac{p(\text{guess})}{p'(\text{guess})} \) is a better approximation. Here, \( p' \) denotes the first derivative of the polynomial \( p \).

#### Derivative Calculation
The first derivative of a function \( f(x) \) represents the rate of change of \( f(x) \) with respect to \( x \). For a constant, the first derivative is zero. For a term \( c \cdot x^p \), the first derivative is \( c \cdot p \cdot x^{p-1} \). Hence, the first derivative of a polynomial of the form \( \sum_{i} c_i \cdot x^i \) is \( \sum_{i} c_i \cdot i \cdot x^{i-1} \).

#### Application to Square Roots
To find the square root of a number \( k \), one needs to find \( x \) such that \( x^2 - k = 0 \). The first derivative of this polynomial is \( 2x \). Therefore, an improved guess for the square root can be obtained using the formula:
\[ \text{next\_guess} = \text{guess} - \frac{\text{guess}^2 - k}{2 \cdot \text{guess}} \]

#### Implementation
The following code demonstrates how to use the Newton–Raphson method to approximate the square root of a number efficiently:
```python
def newton_raphson_sqrt(k, initial_guess=1.0, epsilon=1e-7):
    guess = initial_guess
    while abs(guess**2 - k) > epsilon:
        guess = guess - (guess**2 - k) / (2 * guess)
    return guess

# Example usage:
sqrt_24 = newton_raphson_sqrt(24)
print(f"Approximate square root of 24: {sqrt_24}")
```
This method iteratively improves the guess until the difference between \( \text{guess}^2 \) and \( k \) is less than a small threshold, \( \epsilon \), ensuring a high degree of accuracy.
