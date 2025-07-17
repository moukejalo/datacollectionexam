import streamlit as st

# Inject custom CSS for layout
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
        padding: 0;
        max-width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# # Render the HTML layout
# st.markdown("""
# <div class="container">
#     <div class="content">
#         <h1>Welcome to the Content Page</h1>
#         <p>This is your main content area. You can put text, images, or anything else here.</p>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# Render styled container using HTML
st.markdown('<div class="custom-container">', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>DATA VISUALISATION APP</h1>", unsafe_allow_html=True)

st.markdown("""
This app allows you to download scraped data on motocycles from expat-dakar 
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
""")

# with st.container():
#     st.title("My content")


# # Fonction de loading des données
# def load_(url, title, page_count, key) :
    
#         # st.title("Main Content Area")

#         st.markdown("""
#         <style>
#         div.stButton {text-align:center}
#         </style>""", unsafe_allow_html=True)

#         if st.button(title,key):
#             st.subheader('Display data dimension')
#             st.write('Data dimension: ' + str(url) + ' rows and ' + str(page_count) + ' columns.')
#             # st.dataframe(dataframe)

# load_("https://sn.coinafrique.com/categorie/chiens?page=", "chiens", 1, '1')
# load_("https://sn.coinafrique.com/categorie/moutons?page=", "moutons", 1, '2')
# load_("https://sn.coinafrique.com/categorie/poules-lapins-et-pigeons?page=", "volaile", 1, '3')
# load_("https://sn.coinafrique.com/categorie/autres-animaux?page=", "autres", 1, '4')

# Close the styled div
st.markdown('</div>', unsafe_allow_html=True)


# Sidebar dropdowns
st.sidebar.title("Sidebar with Dropdowns")

# First dropdown
category = st.sidebar.selectbox(
    "Choose Category",
    ["All", "Technology", "Finance", "Education"],
    index=0
)

# Second dropdown
status = st.sidebar.selectbox(
    "Choose Status",
    ["All", "Active", "Inactive", "Pending"],
    index=0
)

# Use values in Python
st.title("Main Content Area")
st.write(f"Selected Category: **{category}**")
st.write(f"Selected Status: **{status}**")

# Example logic based on selections
if category != "All" and status != "All":
    st.success(f"Filtering for **{category}** items with **{status}** status.")
elif category != "All":
    st.info(f"Filtering by category: **{category}**.")
elif status != "All":
    st.info(f"Filtering by status: **{status}**.")
else:
    st.warning("No filters applied.")
