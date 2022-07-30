import streamlit
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast favorites')
streamlit.text('🥗 Omega 3 and blueberry oat meal')
streamlit.text('🥑🍞 kale, spinach and rocket smoothie')
streamlit.text('🐔 Hard boiled free range egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
