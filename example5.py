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
    temp.loc[len(temp)] = scores
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

# Second page

dataframe2 = dataframe.copy()
path = ""
treatment = 0

page_file = """
<|{path}|file_selector|extensions=.txt|label=Upload .txt file|on_action=analyze_file|> <|Downloading {treatment}%...|>


<|Table|expandable|
<|{dataframe2}|table|on_action=on_select|selected={selected_rows}|editable|>
|>

<|{dataframe2}|chart|type=bar|x=Text|y[1]=Score Pos|y[2]=Score Neu|y[3]=Score Neg|y[4]=Overall|color[1]=green|color[2]=grey|color[3]=red|type[4]=line|height=800px|>
"""

def analyze_file(state):
    state.dataframe2 = dataframe2
    state.treatment = 0
    with open(state.path,"r", encoding="utf-8") as f:
        data = f.read()
        # split lines and eliminates duplicates
        file_list = list(dict.fromkeys(data.replace("\n", " ").split(".")[:-1]))


    for i in range(len(file_list)):
        text = file_list[i]
        state.treatment = int((i+1)*100/len(file_list))
        temp = state.dataframe2.copy()
        scores = analyze_text(text)
        temp.loc[len(temp)] = scores
        state.dataframe2 = temp

    state.path = None

selected_rows = [0]

def on_select(state, var_name, data):
    print (f'table row of {var_name} was selected: {data!r}')
    print (f'selected rows: {state.selected_rows!r}')

# One root page for common content
# The two pages that were created
pages = {"/":"<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
         "line":page,
         "text":page_file}

Gui(pages=pages).run()
