
# Generative AI Coding Benchmark

This project focuses on assessing the coding abilities of Generative AI models. The primary aim is to evaluate if these models can generate Python code solutions for diverse mathematical problems.

## Overview

- **Problems**: 100 diverse math model problems encompassing Fibonacci sequences, prime number checking, and factorial calculations.
- **Automated Testing**: A Python script designed to evaluate AI-generated solutions against provided test cases for each problem.
- **Objective**: Assess the capacity of Generative AI to understand and solve coding challenges, with a particular emphasis on diverse mathematical models.

## Getting Started

1. **Setup**:
   - Clone this repository.
   - Ensure you have Python 3.x installed.

2. **Running the Automated Test Script**:
   - Execute the script using the command: 
     ```
     python automated_test_script.py
     ```
   - The script will load the problems, generate solutions (placeholder currently), and evaluate them.

## Project Structure

- **math_model_problems.json**: Contains the 100 coding problems in a structured format.
- **automated_test_script.py**: The main script that evaluates AI-generated solutions.

## Customizing the AI Solution Generator

The current testing script contains a placeholder function for generating AI solutions. To integrate a real Generative AI model:

1. Replace the `generate_solution` function in `automated_test_script.py`.
2. Ensure the function returns valid Python code as a solution to the loaded problem.
3. The returned code should be executable and return expected outputs for the given test cases.

## Results

After executing the script, you will receive results indicating how many test cases each problem passed.

## Contributing

Feel free to fork this project and integrate it with actual Generative AI models. Enhancements, especially in the area of solution evaluation and diverse problem generation, are welcome!

## License

This project is open-source and available to everyone for research and development purposes.
