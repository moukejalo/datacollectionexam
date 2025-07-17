import streamlit as st
import pandas as pd
from scrapbs import fetchData

st.markdown("""
    <style>
    .custom-container {
        background-color: #f8f9fa;
        padding: 20px;
        border: 2px solid #ddd;
        border-radius: 10px;
        margin-top: 20px;
    }
    .cont {
        padding: 20px;
    }
    .container {
        display: flex;
        height: 100vh;
        font-family: sans-serif;
    }
    .sidebar {
        width: 250px;
        background-color: #2c3e50;
        color: white;
        padding: 20px;
    }
    .sidebar h2 {
        margin-bottom: 20px;
    }
    .sidebar ul {
        list-style: none;
        padding-left: 0;
    }
    .sidebar ul li {
        margin-bottom: 15px;
    }
    .sidebar ul li a {
        color: white;
        text-decoration: none;
        font-weight: bold;
    }
    .sidebar ul li a:hover {
        text-decoration: underline;
    }
    .content {
        flex: 1;
        padding: 40px;
        background-color: #ecf0f1;
        color: #2c3e50;
    }
    .st-emotion-cache-1w723zb {
        width: 100%;
        padding: 6rem 1rem 10rem;
        max-width: 100%;
    }
    .st-emotion-cache-1w723zb {
        width: 100%;
        padding: 20px 150px;
        max-width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>DATA VISUALISATION APP</h1>", unsafe_allow_html=True)

st.markdown("""
This app allows you to download scraped data on motocycles from expat-dakar 
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
""")

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

# Sidebar dropdowns
st.sidebar.title("Sidebar with Dropdowns")

# First dropdown
app_feature = st.sidebar.selectbox(
    "Choose the app feature",
    ["Scrape data", "Download scraped data", "View dashboard", "Fill form"],
    index=0
)

# Second dropdown
page_count = st.sidebar.selectbox(
    "Choose the number of pages",
    [1, 2, 3, 4],
    index=0
)

# Fonction de loading des données
def load_(url, title, pageCount, appFeature, key, csvfile) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
        st.write(appFeature)
        st.write(pageCount)
        if appFeature == "Scrape data":
            mydf = fetchData(url, pageCount)
        elif appFeature == "Download scraped data":
            mydf = pd.read_csv(csvfile)

        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(mydf.shape[0]) + ' rows and ' + str(mydf.shape[1]) + ' columns.')
        st.dataframe(mydf)



if app_feature != "Fill form":
    load_("https://sn.coinafrique.com/categorie/chiens?page=", "chiens", page_count, app_feature,  '1', "data/chiens_clean.csv")
    load_("https://sn.coinafrique.com/categorie/moutons?page=", "moutons", page_count, app_feature, '2', "data/moutons_clean.csv")
    load_("https://sn.coinafrique.com/categorie/poules-lapins-et-pigeons?page=", "volaile", page_count, app_feature, '3', "data/moutons_clean.csv")
    load_("https://sn.coinafrique.com/categorie/autres-animaux?page=", "autres", page_count, app_feature, '4', "data/autres_clean.csv")
else:
    st.markdown("<iframe src=https://ee.kobotoolbox.org/i/ra2zcCxm width='800' height='600'></iframe>", unsafe_allow_html=True)


 


