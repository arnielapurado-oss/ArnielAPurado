"""ITECC04 Laboratory 4, Parts B and C: the converter and the evaluator.

Part B turns infix into postfix using the Shunting Yard algorithm.
Part C evaluates a postfix expression.

Both use your own stack. Import it, do not use a bare Python list. If your
ArrayStack is not finished, these functions cannot work, so finish Part A
first.

TOKENS ARE SEPARATED BY SPACES. "3 + 4" is valid input, "3+4" is not. This
is deliberate: writing a real tokeniser is a different exercise, and mixing
it in here hides the algorithm you are meant to be learning.
"""

from stack_array import ArrayStack

# Written for you. Higher number binds tighter.
PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}

# Written for you. 2 ^ 3 ^ 2 means 2 ^ (3 ^ 2), not (2 ^ 3) ^ 2.
RIGHT_ASSOCIATIVE = {"^"}


def tokenize(expression):
    """Written for you. Splits on whitespace."""
    return expression.split()


def infix_to_postfix(expression):
    output = []
    stack = ArrayStack()

    for token in tokenize(expression):
        if token.isdigit():
            output.append(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            while not stack.is_empty() and stack.peek() != "(":
                output.append(stack.pop())
            if stack.is_empty():
                raise ValueError("Unbalanced parentheses")
            stack.pop()  # Remove the "("
        else:  # It's an operator
            while (not stack.is_empty() and stack.peek() != "(" and
                   PRECEDENCE.get(stack.peek(), 0) >= PRECEDENCE.get(token, 0) and
                   not (token in RIGHT_ASSOCIATIVE and PRECEDENCE.get(stack.peek(), 0) == PRECEDENCE.get(token, 0))):
                output.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        if stack.peek() in "()":
            raise ValueError("Unbalanced parentheses")
        output.append(stack.pop())

    return " ".join(output)


def evaluate_postfix(expression):
    values = ArrayStack()

    for token in tokenize(expression):
        if token.isdigit():
            values.push(float(token))
        else:  # It's an operator
            if values.size() < 2:
                raise ValueError("Invalid postfix expression")
            right = values.pop()
            left = values.pop()
            result = apply_operator(token, left, right)
            values.push(result)

    if values.size() != 1:
        raise ValueError("Invalid postfix expression")

    return values.pop()


def apply_operator(operator, left, right):
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("division by zero in the expression")
        return left/right
    if operator == "%":
        if right == 0:
            raise ZeroDivisionError("modulo by zero in the expression")
        return left % right
    if operator == "^":
        return left ** right
    else:
        raise ValueError(f"Unknown operator: {operator}")

def convert_and_evaluate(expression):
    """Written for you. Used by the test file and by the classwork demo."""
    postfix = infix_to_postfix(expression)
    return postfix, evaluate_postfix(postfix)


if __name__ == "__main__":
    # Once Steps 1 to 3 are written, this prints the worked example from the
    # lecture. Until then it reports which step is still missing.
    try:
        postfix, value = convert_and_evaluate("3 + 4 * 2")
        print("infix   : 3 + 4 * 2")
        print("postfix :", postfix)
        print("value   :", value)
    except NotImplementedError as unfinished:
        print("Not written yet ->", unfinished)
