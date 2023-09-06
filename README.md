
# AI Coding Abilities Assessment

This project aims to assess generative AI's coding capabilities through a set of 100 Python problems that focus on good practices of software engineering. Each problem tests the AI's ability to write code that is not only functional but also adheres to principles such as modularity, readability, and robustness.

## Project Structure

- `problems.json`: A JSON file containing 100 Python coding problems, each with a description, input parameters, output parameters, sample test cases, coding guidelines, and evaluation metrics.
- `automated_testing.py`: A Python script that mocks the generation of solutions by an AI, tests these solutions against the provided sample test cases, and evaluates them based on the metrics defined in `problems.json`.

## Usage Instructions

1. Ensure that both the `problems.json` file and the `automated_testing.py` script are in the same directory.
2. Run the testing script using Python:

```
python automated_testing.py
```

3. The script will simulate the generation of solutions by the AI, test these solutions against the sample test cases, and evaluate them based on "Correctness" and "Robustness". The results will be printed to the console.

## Evaluation Metrics

- **Correctness**: Determines if the generated solution produces the expected output for the given sample test cases.
- **Robustness**: Assesses the solution's ability to handle edge cases and unexpected inputs without crashing or producing errors.

## Future Work

This is a mock version of the project that provides a scaffold for evaluating generative AI's coding abilities. Future work should focus on integrating with real Generative AI platforms and expanding the testing capabilities.
