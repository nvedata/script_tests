def step_f(x, f_steps, x_breaks):
    n = 0
    for right in x_breaks:
        if x < right:
            break
        n += 1
    return f_steps[n]
