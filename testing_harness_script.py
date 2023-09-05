
import json
from math import log

# Mock Solutions

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

def nth_prime(n):
    def sieve_of_eratosthenes(limit):
        sieve = [True] * (limit + 1)
        sieve[0:2] = [False, False]
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                sieve[i*i::i] = [False] * len(sieve[i*i::i])
        return [i for i, is_prime in enumerate(sieve) if is_prime]
    
    upper_bound = int(n * (log(n) + log(log(n))))
    primes = sieve_of_eratosthenes(upper_bound)
    return primes[n-1]

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def arithmetic_progression(a, d, n):
    return a + (n - 1) * d

def geometric_progression(a, r, n):
    return a * (r ** (n - 1))

# Testing Harness

def run_tests(problems_path):
    with open(problems_path, 'r') as file:
        problems = json.load(file)
    
    results = []
    errors = []
    
    for problem in problems:
        statement = problem["problem_statement"]
        solution_func = None
        
        if "Fibonacci" in statement:
            solution_func = fibonacci
        elif "Prime" in statement:
            solution_func = nth_prime
        elif "factorial" in statement:
            solution_func = factorial
        elif "arithmetic progression" in statement:
            solution_func = arithmetic_progression
        elif "geometric progression" in statement:
            solution_func = geometric_progression
        
        if not solution_func:
            errors.append(f"No solution found for problem {problem['problem_id']}.")
            continue
        
        passed_tests = 0
        total_tests = len(problem.get("sample_test_cases", []))
        
        for test_case in problem.get("sample_test_cases", []):
            try:
                input_params = test_case["input"]
                expected_output = test_case["expected_output"][0]
                if solution_func(*input_params) == expected_output:
                    passed_tests += 1
            except Exception as e:
                errors.append(f"Error testing problem {problem['problem_id']}: {str(e)}")
        
        result = {
            "problem_id": problem["problem_id"],
            "passed_tests": passed_tests,
            "total_tests": total_tests
        }
        results.append(result)
    
    return results, errors

# Main Execution

if __name__ == "__main__":
    problems_path = "diverse_math_problems.json"  # Adjust path as needed
    test_results, test_errors = run_tests(problems_path)
    print(test_results)
    print(test_errors)

