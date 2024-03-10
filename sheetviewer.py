import pandas as pd
from taipy.gui import Gui, notify

### Data page

sheet_path = ""
dataframe = pd.DataFrame({
        "ID": [1],
        "Name": ["Monty Pi"],
        "Value 1": [42.1234],
        "Value 2": [3.141],
        })
selected = set()
columns = list(dataframe.columns)
selected_columns = columns[:]

data_page = """
## Load sheet data
<|{sheet_path}|file_selector|extensions=.csv|label=Upload .csv file|on_action=show_sheet|>

## Sheet <|{sheet_path}|text|>
<|{selected_columns}|selector|lov={columns}|on_change=column_selector|multiple|dropdown|class_name=wide-selector|>
<|{dataframe}|table|columns={selected_columns}|on_action=row_select|filter|editable|height=500px|rebuild|style=row_style|page_size=10|>

"""

def show_sheet(state):
    new_data = pd.read_csv(state.sheet_path)
    print (new_data.head(10))
    state.dataframe = new_data
    state.columns = list(new_data.columns)
    state.selected_columns = state.columns[:]
    state.chart_dataframe = new_data
    state.x_axis = state.columns[:1]
    state.y_axis = state.columns[1:3]

## Column selector
def column_selector(state, var_name, data):
    return

## Row selection logic

def row_select(state, var_name, data):
    #print (f'on_select - var: {var_name}, data: {data!r}')
    index = data['index']
    if index in state.selected:
        # select row
        state.selected.remove(index)
    else:
        # deselect row
        state.selected.add(index)
    #print (f' - selected: {selected}')
    # Let Taipy know that it has to rerender the table with new CSS
    state.dataframe = state.dataframe

def row_style(state, row_index, row_data):
    #print (f'row_style - row_index: {row_index}')
    if row_index in selected:
        #print (f' - selected: {row_index}')
        return 'selected-row'

### Chart page

chart_dataframe = pd.DataFrame({
        "ID": [1],
        "Name": ["Monty Pi"],
        "Value 1": [42.1234],
        "Value 2": [3.141],
        })

x_axis = [columns[0]]
y_axis = [columns[2], columns[3]]

chart_page = """
## Chart

X axis: <|{x_axis}|selector|lov={columns}|dropdown|>
Y axis: <|{y_axis}|selector|lov={columns}|multiple|dropdown|>


<|{chart_dataframe}|chart|type=bar|x={x_axis}|y={y_axis}|rebuild|height=800px|>
"""

### Combine pages

pages = {"/":"<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
         "Data":data_page,
         "Chart":chart_page,
         }

if __name__ == "__main__":
    Gui(pages=pages).run()
