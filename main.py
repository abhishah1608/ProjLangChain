import streamlit as st
from langchain_helper import getRestaurantandMenuDetails
import os
from dotenv import load_dotenv

st.title("Restaurant and Menu Generator")
load_dotenv()
os.environ["OPENAI_API_KEY"]= os.getenv("chatgpt_key")

cuisine_name = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Mexican", "Gujarati", "Italian", "Arabic", "Pakistani"))



if cuisine_name:
    output = getRestaurantandMenuDetails(cuisine_name)
    st.header("Restaurant and Menu Generator")
    if output and output['results']:
        restaurant_lists = output['results']
        for r in restaurant_lists:
            st.subheader(r['restaurant'])
            st.write("**Menu Items:**")
            menu_list = r['menu_items']
            for menu in menu_list:
                st.write(f"• {menu['menu_item']} ⭐ {menu['rating']}")
             

