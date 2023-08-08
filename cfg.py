from lizard import analyze_file

def calculate_cyclomatic_complexity_per_function(args):
    result = analyze_file(args.path)
    functions = result.function_list
    tot_cfg = sum(function.cyclomatic_complexity for function in functions)
    for function in functions:
        print(f"Function: {function.name}, Cyclomatic Complexity: {function.cyclomatic_complexity}")

    print("Total cyclomatic complexity :", tot_cfg)
    print("Average cyclomatic complexity :", result.average_cyclomatic_complexity)