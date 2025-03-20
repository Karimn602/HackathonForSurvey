from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

history = []  # Stores previous computations

###############################################################################
#                           Number Theory Functions                           #
###############################################################################

def prime_factorization(n):
    """Returns the prime factorization of n as a dict {prime: exponent}."""
    factors = {}
    if n < 2:
        return factors
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def euler_totient(n):
    """Computes the Euler Totient function φ(n)."""
    if n < 2:
        return 0 if n == 0 else 1
    factors = prime_factorization(n)
    result = n
    for p in factors:
        result -= result // p
    return result

def miller_rabin(n, k=5):
    """Miller-Rabin Primality Test. Returns True if likely prime, False otherwise."""
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for sp in small_primes:
        if n == sp:
            return True
        if n % sp == 0 and n != sp:
            return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False
    
    for _ in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, r, d, n):
            return False
    return True

def fast_exp(base, exponent, modulus=None):
    """Computes (base^exponent) % modulus if modulus is given, else base^exponent."""
    return pow(base, exponent, modulus) if modulus else base ** exponent

###############################################################################
#                               Flask Routes                                  #
###############################################################################

@app.route("/")
def home():
    return render_template("index.html", history=history)

@app.route("/compute", methods=["POST"])
def compute():
    """Handles computation requests from the frontend."""
    try:
        data = request.get_json(force=True)  # ✅ Ensure JSON parsing
        operation = data.get("operation")
        result = None

        if operation == "prime_factor":
            n = int(data["n"])
            factors = prime_factorization(n)
            result = f"Prime factors of {n}: {factors}"

        elif operation == "totient":
            n = int(data["n"])
            result = f"φ({n}) = {euler_totient(n)}"

        elif operation == "miller_rabin":
            n = int(data["n"])
            k = int(data["k"])
            result = f"{n} is PRIME" if miller_rabin(n, k) else f"{n} is COMPOSITE"

        elif operation == "fast_exp":
            base = int(data["base"])
            exponent = int(data["exponent"])
            modulus = int(data["modulus"]) if data["modulus"] else None
            result = f"Result: {fast_exp(base, exponent, modulus)}"

        if result:
            history.append(f"{operation.upper()}: {result}")
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400  # ✅ Return proper error response

if __name__ == "__main__":
    app.run(debug=True)

