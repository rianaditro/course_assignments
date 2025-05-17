"""
Objective: Use the pdb module to step through code for debugging purposes.
"""
def buggy_function(x):
    result = x * 10
    # TODO: Set a breakpoint here using pdb.set_trace() and inspect the value of 'result'
    import pdb; pdb.set_trace()  # Debugger breakpoint
    result += 5
    return result

# Call the function to start debugging
print("Buggy function result:", buggy_function(3))

print()
# TODO: After stepping through, remove the pdb breakpoint and ensure the function runs correctly.
def buggy_function(x):
    result = x * 10
    result += 5
    return result

# Call the function to see the result
print("Buggy function result:", buggy_function(3))