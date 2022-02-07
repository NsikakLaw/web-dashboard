from create_database import Database
from reports import Reports
from dash import Dash, dash_table, html
from create_details import create_db_details
import os

if not os.path.isfile('./test.db'):
    create_db_details()

db = Database("test.db")
report = Reports(db)
popular_df = report.most_popular_item()
app = Dash(__name__)

app.layout = html.Div(children=[
        html.H1(children='Hello User!'),

        html.H3(children='The most purchased product is ' + popular_df['product_name'][0] +
                         ' with ' + str(popular_df['Number_of_Purchases'][0]) + ' purchases'),

        html.H2(children='''
            Insights on Members and Ranking
        '''),
        dash_table.DataTable(report.member_ranking_details().to_dict('records'),
                             [{"name": i, "id": i} for i in report.member_ranking_details().columns])

    ])

if __name__ == '__main__':

    app.run_server(debug=True)
