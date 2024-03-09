import numpy as np
import pandas as pd
from taipy.gui import Gui, notify
from nlp1 import analyze_text

text = "Original text"

dataframe = pd.DataFrame({"Text": [""],
                        "Score Pos": [0.33],
                        "Score Neu": [0.33],
                        "Score Neg": [0.33],
                        "Overall": [0]})


def local_callback(state):
    notify(state, "Info", f"The text is: {state.text}", True)
    temp = state.dataframe.copy()
    scores = analyze_text(state.text)
    temp.loc[-1] = scores
    state.dataframe = temp
    state.text = ""


page = """
<|toggle|theme|>

# Getting started with Taipy GUI

My text: <|{text}|>

Enter a word:
<|{text}|input|>
<|Analyze|button|on_action=local_callback|>

## Positive
<|{np.mean(dataframe["Score Pos"])}|text|format=%.2f|>

## Neutral
<|{np.mean(dataframe["Score Neu"])}|text|format=%.2f|>

## Negative
<|{np.mean(dataframe["Score Neg"])}|text|format=%.2f|>

<|{dataframe}|table|>

<|{dataframe}|chart|type=bar|x=Text|y[1]=Score Pos|y[2]=Score Neu|y[3]=Score Neg|y[4]=Overall|color[1]=green|color[2]=grey|color[3]=red|type[4]=line|>
"""

Gui(page).run(debug=True)
