import dash
import dash_cytoscape as cyto
from dash import html, dcc, Input, Output

app = dash.Dash(__name__)

# Define the elements of the graph (nodes and edges)
elements = [
    # Nodes
    {'data': {'id': 'A', 'label': 'Node A'}, 'position': {'x': 100, 'y': 150}},
    {'data': {'id': 'B', 'label': 'Node B'}, 'position': {'x': 200, 'y': 250}},
    {'data': {'id': 'C', 'label': 'Node C'}, 'position': {'x': 300, 'y': 100}},
    {'data': {'id': 'D', 'label': 'Node D'}, 'position': {'x': 400, 'y': 200}},
    {'data': {'id': 'E', 'label': 'Node E'}, 'position': {'x': 150, 'y': 350}},
    
    # More Nodes
    {'data': {'id': 'F', 'label': 'Node F'}, 'position': {'x': 500, 'y': 100}},
    {'data': {'id': 'G', 'label': 'Node G'}, 'position': {'x': 550, 'y': 300}},
    
    # Edges
    {'data': {'source': 'A', 'target': 'B', 'label': 'A to B'}},
    {'data': {'source': 'A', 'target': 'C', 'label': 'A to C'}},
    {'data': {'source': 'B', 'target': 'D', 'label': 'B to D'}},
    {'data': {'source': 'C', 'target': 'D', 'label': 'C to D'}},
    {'data': {'source': 'D', 'target': 'E', 'label': 'D to E'}},
    
    # More Edges
    {'data': {'source': 'E', 'target': 'F', 'label': 'E to F'}},
    {'data': {'source': 'F', 'target': 'G', 'label': 'F to G'}}
]

# Define the layout of the app
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown-layout',
        options=[
            {'label': 'Preset', 'value': 'preset'},
            {'label': 'Breadthfirst', 'value': 'breadthfirst'},
            {'label': 'Circle', 'value': 'circle'},
            {'label': 'Concentric', 'value': 'concentric'},
            {'label': 'Grid', 'value': 'grid'},
            {'label': 'Random', 'value': 'random'},
        ],
        value='preset',
        clearable=False
    ),
    cyto.Cytoscape(
        id='cytoscape',
        elements=elements,
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '600px'},
        stylesheet=[
            # Node style
            {
                'selector': 'node',
                'style': {
                    'background-color': '#28a745',
                    'label': 'data(label)',
                    'width': '50px',
                    'height': '50px',
                    'text-valign': 'center',
                    'color': 'white',
                    'text-outline-width': 2,
                    'text-outline-color': '#28a745'
                }
            },
            # Edge style
            {
                'selector': 'edge',
                'style': {
                    'curve-style': 'bezier',
                    'target-arrow-shape': 'triangle',
                    'line-color': '#007bff',
                    'target-arrow-color': '#007bff',
                    'label': 'data(label)',
                    'width': 4,
                    'font-size': 10,
                    'color': '#007bff',
                    'text-outline-width': 1,
                    'text-outline-color': 'white',
                }
            },
            # Style on node hover
            {
                'selector': 'node:hover',
                'style': {
                    'background-color': '#007bff',
                    'text-outline-color': '#007bff',
                    'transition-property': 'background-color, text-outline-color',
                    'transition-duration': '0.5s',
                }
            },
            # Style on edge hover
            {
                'selector': 'edge:hover',
                'style': {
                    'line-color': '#28a745',
                    'target-arrow-color': '#28a745',
                    'transition-property': 'line-color, target-arrow-color',
                    'transition-duration': '0.5s',
                }
            }
        ],
    ),
    html.Div(id='cytoscape-tapNodeData-output')
])

# Define callback to change layout based on dropdown
@app.callback(
    Output('cytoscape', 'layout'),
    Input('dropdown-layout', 'value')
)
def update_layout(layout_value):
    return {'name': layout_value}

# Define callback to display node data on tap
@app.callback(
    Output('cytoscape-tapNodeData-output', 'children'),
    Input('cytoscape', 'tapNodeData')
)
def display_tap_node_data(data):
    if data:
        return f"You clicked on {data['label']}."
    return "Click on a node to see its details."

if __name__ == '__main__':
    app.run_server(debug=True)
