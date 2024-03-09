from taipy.gui import Gui, notify
from math import cos, exp

value = 10
compute_range = 100

page = """
# Taipy *Getting Started*

## Values: 

- <|{value}|text|>
  <|{value}|slider|on_change=on_slider|>

- <|{compute_range}|text|>
  <|{compute_range}|slider|on_change=on_slider|>

<|{data}|chart|>
"""

xyz = 42

def on_slider(state):
    state.data = compute_data(state.value, state.compute_range)
    print (f'state.value changed to {state.value}')
    extra(state)
    if state.value > 50:
        notify(state, message='exceeding 50', duration=500)
        notify(state, message=f'global xyz={xyz}', duration=500)

def extra(state):
    state.compute_range += 1

def compute_data(decay:int, compute_range:int)->list:
    return [cos(i/6) * exp(-i*decay/900) for i in range(compute_range)]

data = compute_data(value, compute_range)

if __name__ == "__main__":
    Gui(page).run(title="Dynamic chart", use_reloader=False)
    # Note: The reloader doesn't appear to work as advertised. The
    # app starts crashing after you make a change.
