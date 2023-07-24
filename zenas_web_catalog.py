import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')

# Connect to Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# Run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# Put the data into a dataframe
df = pandas.DataFrame(my_catalog)

# Temp
# streamlit.write(df)

# Put the first column into a list
color_list = df[0].values.tolist()

# Put a pick list for users to pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', color_list)
