import streamlit as st
import pandas as pd
from scrapbs import fetchData
import plotly.express as px
import geopandas as gpd
import folium
from streamlit_folium import folium_static

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
    .st-emotion-cache-derjs0 h1 {
        font-size: 1.5rem;
        font-weight: 600;
        padding: 1.25rem 0px 1rem;
        color: white;
    }
    .st-emotion-cache-1e9qngv p {
        word-break: break-word;
        margin: 0px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>DATA VISUALISATION APP</h1>", unsafe_allow_html=True)

st.markdown("""
This app allows you to scraped data using BeautifulSoup, to download scraped data using web scraper, to view some dashboard from downloaded data and at the end to fill an evaluaton form for using the app. 
* **Python libraries:** BeautifulSoup, pandas, streamlit, plotly, geopandas, folium, streamlit_folium, get
* **Data source:** [Coin-Afrique](https://sn.coinafrique.com/).
""")

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

# Sidebar dropdowns
st.sidebar.title("Menu")

# First dropdown
app_feature = st.sidebar.selectbox(
    "Choose the app feature",
    ["Scrape data", "Download scraped data", "View dashboard", "Fill form"],
    index=0
)

# Second dropdown
page_count = st.sidebar.selectbox(
    "Choose the number of pages",
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
    index=0
)

# Fonction de loading des données
def load_(url, title, pageCount, appFeature, key, csvfile) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
        if appFeature == "Scrape data":
            df = fetchData(url, pageCount)

            # Convert prices to numeric (filtering out "Prix sur demande")
            df = df[df['prix'] != 'Prix sur demande'].copy()
            df = df[df['prix'] != ''].copy()

            st.subheader('Display data dimension')
            st.write('Data dimension: ' + str(df.shape[0]) + ' rows and ' + str(df.shape[1]) + ' columns.')
            st.dataframe(df)
        elif appFeature == "Download scraped data":
            df = pd.read_csv(csvfile)
            st.subheader('Display data dimension')
            st.write('Data dimension: ' + str(df.shape[0]) + ' rows and ' + str(df.shape[1]) + ' columns.')
            st.dataframe(df)
        elif appFeature == "View dashboard":    
            df = pd.read_csv(csvfile)

            columns_to_keep = ['nom', 'prix', 'adresse', 'image_lien']
            df = df[columns_to_keep]

            # Clean the 'prix' column: remove spaces, convert to numeric
            df['prix'] = df['prix'].astype(str).str.replace(' ', '').str.replace('CFA', '', regex=False)
            df['prix'] = pd.to_numeric(df['prix'], errors='coerce')

            # Optional: drop rows where price is NaN
            df = df.dropna(subset=['prix'])

            MAX_INT_32 = 2_147_483_647
            df = df[df['prix'] < MAX_INT_32].copy()

            # Dashboard title
            st.title('Senegal Marketplace Analysis')

            # Overview metrics
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Listings", len(df))
            col2.metric("Average Price", f"{df[df['prix'] != 'Prix sur demande']['prix'].mean():,.0f} CFA")
            col3.metric("Most Common", df['nom'].value_counts().index[0])

            st.bar_chart(df['adresse'].value_counts())


            # # Load 
            # # Clean the 'prix' column: remove spaces, convert to numeric
            # df['prix'] = df['prix'].astype(str).str.replace(' ', '').str.replace('CFA', '', regex=False)
            # df['prix'] = pd.to_numeric(df['prix'], errors='coerce')

            # # Optional: drop rows where price is NaN
            # df = df.dropna(subset=['prix'])

            # Price distribution
            st.subheader('Price Distribution')
            fig = px.histogram(df[df['prix'] != 'Prix sur demande'], x='prix', nbins=20)
            st.plotly_chart(fig)

            # popularity
            st.subheader('Top 10')
            top_breeds = df['nom'].value_counts().head(10)
            st.bar_chart(top_breeds)

            # Location analysis
            st.subheader('Listings by Location')
            location_counts = df['adresse'].value_counts().head(10)
            st.table(location_counts)


            st.title('Price Analysis')

            # Convert prices to numeric (filtering out "Prix sur demande")
            price_df = df

            # price_df['prix'] = price_df['prix'].astype(str).str.replace(' ', '').str.replace('CFA', '', regex=False)
            # price_df['prix'] = pd.to_numeric(price_df['prix'], errors='coerce')

            # # Optional: drop rows where price is NaN
            # price_df = price_df.dropna(subset=['prix'])

            # st.write(price_df)

            # Price range selector
            price_range = st.slider(
                'Select price range (CFA)',
                min_value=int(price_df['prix'].min()),
                max_value=int(price_df['prix'].max()),
                value=(int(price_df['prix'].quantile(0.25)), int(price_df['prix'].quantile(0.75)))
            )

            # Filter data
            filtered_df = price_df[(price_df['prix'] >= price_range[0]) & (price_df['prix'] <= price_range[1])]

            # Scatter plot of price vs breed
            st.subheader('Price Distribution')
            fig = px.scatter(filtered_df, x='nom', y='prix', color='adresse')
            st.plotly_chart(fig)

            # Average price by location
            st.subheader('Average Price by Location')
            avg_price = filtered_df.groupby('adresse')['prix'].mean().sort_values(ascending=False).head(10)
            st.bar_chart(avg_price)


            st.title('Dog Listings Geographic Distribution')

            # Simple geocoding (would need proper implementation)
            # This is a simplified version - you'd need actual coordinates
            locations = {
                'Dakar': (14.7167, -17.4677),
                'Thies': (14.7833, -16.9167),
                'Saint Louis': (16.0333, -16.5000),
            }

            # Create a map
            m = folium.Map(location=[14.7167, -17.4677], zoom_start=10)

            # Add markers
            for idx, row in df.iterrows():
                location = row['adresse'].split(',')[0]  # Get primary location
                if location in locations:
                    folium.Marker(
                        location=locations[location],
                        popup=f"{row['nom']} - {row['prix']}",
                    ).add_to(m)

            # Display map
            folium_static(m)




if app_feature == "Fill form":
    st.markdown("<iframe src=https://ee.kobotoolbox.org/i/ra2zcCxm width='1200' height='900'></iframe>", unsafe_allow_html=True)
else:
    load_("https://sn.coinafrique.com/categorie/chiens?page=", "Chiens", page_count, app_feature,  '1', "data/chiens_file.csv")
    load_("https://sn.coinafrique.com/categorie/moutons?page=", "Moutons", page_count, app_feature, '2', "data/moutons_file.csv")
    load_("https://sn.coinafrique.com/categorie/poules-lapins-et-pigeons?page=", "Volailles", page_count, app_feature, '3', "data/moutons_file.csv")
    load_("https://sn.coinafrique.com/categorie/autres-animaux?page=", "Autres", page_count, app_feature, '4', "data/autres_file.csv")
    
