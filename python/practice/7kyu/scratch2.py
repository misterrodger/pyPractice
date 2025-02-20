def wrapper(value):
    def pipeline(func):
        def next_pipeline(next_func):
            return wrapper(func(value))(next_func)
        next_pipeline.get_value = lambda: func(value)
        return next_pipeline
    return pipeline(lambda x: x)


# Example functions
add_one = lambda x: x + 1
square = lambda x: x * x

# Chain pipeline
result = (
    wrapper(3)               # Start with 3
    (add_one)                # Add 1: 3 + 1 = 4
    (square)                 # Square: 4 * 4 = 16
    (lambda x: x * 2)        # Double: 16 * 2 = 32
    .get_value()             # Retrieve the final value
)

print(result)  # Output: 32
