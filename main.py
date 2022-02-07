from create_database import Database
from reports import Reports
from flask import Flask, render_template
from create_details import create_db_details
import os

app = Flask(__name__)

if not os.path.isfile('./test.db'):
    create_db_details()

db = Database("test.db")
report = Reports(db)
popular_df = report.most_popular_item()
member_ranking_df = report.member_ranking_details()


@app.route('/', methods=['GET', 'POST'])
def analysis_details():
    return render_template('index.html', tables=[member_ranking_df.to_html(classes='data', header='true', index=False)]
                           , product=popular_df['product_name'][0], count=str(popular_df['Number_of_Purchases'][0]))


if __name__ == '__main__':
    app.run(debug=True)
