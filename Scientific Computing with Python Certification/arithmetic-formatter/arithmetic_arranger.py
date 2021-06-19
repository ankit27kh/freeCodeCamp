def arithmetic_arranger(problems, answer=False):
    top = []
    bottom = []
    lines = []
    answers = []
    if len(problems) > 5:
        return "Error: Too many problems."
    for prob in problems:
        a, sign, b = prob.split()
        if sign not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (a.isdigit() and b.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(a) > 4 or len(b) > 4:
            return "Error: Numbers cannot be more than four digits."
        length = max(len(a), len(b)) + 2
        top.append(a.rjust(length))
        bottom.append(f"{sign} {b.rjust(length - 2)}")
        lines.append('-' * length)
        if sign == '+':
            answers.append(str(int(a) + int(b)).rjust(length))
        else:
            answers.append(str(int(a) - int(b)).rjust(length))
    if answer:
        return f"{'    '.join(top)}\n{'    '.join(bottom)}\n{'    '.join(lines)}\n{'    '.join(answers)}"
    else:
        return f"{'    '.join(top)}\n{'    '.join(bottom)}\n{'    '.join(lines)}"
