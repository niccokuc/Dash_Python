import dash
import dash_table
import pandas as pd

df = pd.read_csv('port_scan.csv')

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('reccords'),)

if __name__ == '__main__':
    app.run_server(debug=True)