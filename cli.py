import argparse

from ipython_commander import process_question

if __name__ == '__main__':
    # Parse question from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('question', type=str, help='Question to ask GPT-3')
    # Optional parameter "max iterations"
    parser.add_argument(
        '--max_iterations',
        type=int,
        default=5,
        help='Maximum number of iterations to ask GPT-3'
    )
    # Optional parameter "openapi token"
    parser.add_argument(
        '--openai_token',
        type=str,
        default=None,
        help='OpenAI API token'
    )
    # Optional parameter "cost per 1000 tokens"
    parser.add_argument(
        '--cost_per_1000_tokens',
        type=float,
        default=None,
        help='Cost per 1000 tokens'
    )

    args = parser.parse_args()
    response = process_question(
        args.question, args.max_iterations,
        args.openai_token, args.cost_per_1000_tokens
    )
    print(response.final_prompt)
    print(f'Answer: {response.answer}')
    print(f'Iterations: {response.iterations}')
    print(f'Execution total cost: ${response.execution_total_cost}')
