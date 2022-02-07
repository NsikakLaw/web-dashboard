from sqlite3 import Error
import pandas as pd


class Reports:
    """creates dataframes of different sql queries
    :param Database: Database object

    """

    def __init__(self, Database):

        self.Database = Database

    def most_popular_item(self):
        # returns the dataframe of the most popular item based on the query

        query = '''select sales.product_id, menu.product_name, count(sales.product_id) as Number_of_Purchases
         from sales join menu on sales.product_id = menu.product_id
          group by sales.product_id, menu.product_name order by count(sales.product_id) desc limit 1;'''

        try:
            df = pd.read_sql_query(query, self.Database.db_connection)
            return df

        except Error as e:
            print(e)

    def member_ranking_details(self):
        # returns the sales table showing ranking according
        # to order date and if the customer was a member or not

        query = '''select sales.customer_id, sales.order_date, menu.product_name, menu.price,
               case when sales.order_date < members.join_date then "N"
                when sales.order_date >= members.join_date then "Y"
                 else "N" end as member,
                dense_rank() over(partition by sales.customer_id order by sales.order_date) as ranking
                from sales left join members on sales.customer_id = members.customer_id
                left join menu on sales.product_id = menu.product_id'''

        try:
            df = pd.read_sql_query(query, self.Database.db_connection)
            return df

        except Error as e:
            print(e)
