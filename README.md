
# Generative AI Python Coding Benchmark

## Objective
The aim of this project is to evaluate the coding capabilities of Generative AI models using a diverse set of mathematical problems. The generated problems range from sequences like Fibonacci to prime numbers, factorial calculations, arithmetic, and geometric progressions.

## What's Interesting?

This project offers a fresh perspective on benchmarking Generative AI models in coding tasks. Here's why this approach stands out:

1. **Diverse Mathematical Models**: Instead of standard coding problems, this benchmark focuses on a variety of mathematical models. From sequences like Fibonacci to prime number calculations, the problems offer a blend of computational and mathematical challenges.
  
2. **Automated Testing Harness**: With a prime focus on automation, the testing harness allows for seamless evaluation. Whether you have 10 or 10,000 problems, the script can evaluate solutions without manual intervention.

3. **Flexibility for Expansion**: The structured format of problems makes it easy to add new challenges. Whether you want to introduce new mathematical concepts or increase the complexity of existing ones, the framework supports it.

4. **Granular Feedback**: Instead of just a pass/fail status, the harness provides detailed feedback on each problem. This can be instrumental in understanding the strengths and weaknesses of a Generative AI model in coding tasks.

5. **Open-Source and Collaborative**: The project is open-sourced, allowing for community-driven enhancements, extensions, and improvements.

## Problem Structure
Each problem in the dataset is represented as a JSON object with the following attributes:
- `problem_id`: A unique identifier for the problem.
- `problem_statement`: The textual description of the coding problem.
- `sample_test_cases`: A list of sample test cases where each test case has:
  - `input`: The input parameters for the problem.
  - `expected_output`: The expected output for the given input.

## Running the Testing Harness
To evaluate the solutions against the generated problems:
1. Ensure you have the `diverse_math_problems.json` file in the same directory as the script or adjust the path in the script.
2. Run the `testing_harness_script.py` Python script.
3. The script will automatically test the mock solutions against the problems and print the results.

## Results
The script will output:
- A list of results with the number of passed tests for each problem.
- Any errors encountered during the testing process, like missing solutions or runtime errors.

## Potential Errors and Troubleshooting
If a problem doesn't have a corresponding mock solution, the script will log an error message indicating the missing solution for the specific problem ID. Additionally, runtime errors during solution testing will be logged with the problem ID and the error message.

## Future Work
The testing harness can be extended to include more diverse problems, refine existing mock solutions, and enhance the evaluation metrics for a comprehensive benchmarking of Generative AI models in coding tasks.

## License
This project is open source and available under the MIT License.

