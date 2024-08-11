import streamlit as st
import pandas as pd
from PIL import Image
import datetime
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv("Sample_DataSet_Assessment.csv")

# Set page configuration
st.set_page_config(
    page_title="Interactive Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://example.com/help',
        'Report a bug': 'https://example.com/bug',
        'About': 'This is an interactive dashboard created by Oko Abigail using Streamlit.'
    }
)

# Custom CSS styles
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
        }
        .block-container {
            padding-top: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
            padding-bottom: 1rem;
        }
        .title-container {
            background-color: #4CAF50;
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            font-size: 36px;
            font-weight: bold;
        }
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 10px 0;
        }
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: pointer;
        }
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 120px;
            background-color: black;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px 0;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -60px;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
""", unsafe_allow_html=True)

# Load and display the image
image = Image.open('ingryd-academy-logo.jpg')

# Create a sidebar
st.sidebar.image(image, width=180)
st.sidebar.markdown("Last updated by:")
box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
st.sidebar.write(f"{box_date}")

st.sidebar.title("E-Commerce Analytics")
st.sidebar.markdown("Select options below:")
selected_chart = st.sidebar.selectbox("Select Chart Type", 
                                      ["Total Sales by Date", 
                                       "Total Sales by Sales Team", 
                                       "Total Profit by Date", 
                                       "Total Profit by Sales Team", 
                                       "Total Sales by State", 
                                       "Total Profit by State", 
                                       "Most Sold Product by State", 
                                       "Most Profitable Product", 
                                       "Sales Distribution (Donut Chart)"])

# Define the HTML for the title
html_title = """
<div class="title-container">
    E-COMMERCE ANALYTICS DASHBOARD
</div>
"""
st.markdown(html_title, unsafe_allow_html=True)

# Calculations for Total Sales, Total Cost, and Total Profit
df['Total Sales'] = df['Order Quantity'] * df['Unit Price'] * (1 - df['Discount Applied'])
df['Total Cost'] = df['Order Quantity'] * df['Unit Cost']
df['Total Profit'] = df['Total Sales'] - df['Total Cost']

# Helper function to create download buttons
def create_download_button(data, file_name):
    st.download_button(f"Download {file_name}", data=data.to_csv().encode("utf-8"),
                       file_name=file_name, mime="text/csv")

# Function to display the selected metric
def display_metric(df, selected_chart):
    if "Sales" in selected_chart:
        return df['Total Sales'].sum(), "Total Sales"
    elif "Profit" in selected_chart:
        return df['Total Profit'].sum(), "Total Profit"
    elif "Most Sold Product" in selected_chart:
        return df['Order Quantity'].sum(), "Total Sold Product"
    
# Function to create secondary plot for top 10 data
def create_secondary_plot(data, x, y, title, chart_type):
    if chart_type == "bar":
        fig = go.Figure(go.Bar(
            x=data[y],
            y=data[x],
            orientation='h',
            text=data[y],
            textposition='auto',
            marker=dict(color='#4CAF50')
        ))
        fig.update_layout(
            title=title,
            template='plotly_white',
            height=400,
            xaxis=dict(title=y, showgrid=False),
            yaxis=dict(title=x, categoryorder='total ascending', showgrid=False)
        )
    else:
        fig = px.pie(data, names=x, values=y, title=title, template="plotly_white", height=500, hole=0.4)
    return fig

# Data visualizations based on selection
metric_value, metric_label = display_metric(df, selected_chart)
st.metric(label=f"{metric_label}", value=f"${metric_value:,.2f}" if metric_label != "Total Sold Product" else f"{metric_value:,}")

if selected_chart == "Total Sales by Date":
    sales_trend = df.groupby('Transaction Date')['Total Sales'].sum().reset_index()
    fig = px.line(sales_trend, x="Transaction Date", y="Total Sales", labels={"Total Sales": "Total Sales {$}"},
                 title="Total Sales By Transaction Date", template="plotly_white", height=500)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(sales_trend)
    create_download_button(sales_trend, "Sales_by_date.csv")

elif selected_chart == "Total Sales by Sales Team":
    sales_team_summary = df.groupby('SalesTeamID')['Total Sales'].sum().reset_index()
    fig1 = px.bar(sales_team_summary, x="SalesTeamID", y="Total Sales", labels={"Total_Sales": "Total_Sales {$}"},
                  title="Total Sales By Sales Team", template="plotly_white", height=500, color="SalesTeamID")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.dataframe(sales_team_summary)
    create_download_button(sales_team_summary, "Sales_by_SalesTeam.csv")

elif selected_chart == "Total Profit by Date":
    profit_trend = df.groupby('Transaction Date')['Total Profit'].sum().reset_index()
    fig2 = px.scatter(profit_trend, x="Transaction Date", y="Total Profit", labels={"Total Profit": "Total Profit {$}"},
                  title="Total Profit By Transaction Date", template="plotly_white", height=500)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        st.dataframe(profit_trend)
    create_download_button(profit_trend, "Profit_by_date.csv")

elif selected_chart == "Total Profit by Sales Team":
    profit_team_summary = df.groupby('SalesTeamID')['Total Profit'].sum().reset_index()
    fig3 = px.bar(profit_team_summary, x="SalesTeamID", y="Total Profit", labels={"Total Profit": "Total Profit {$}"},
                  title="Total Profit By Sales Team", template="plotly_white", height=500, color="SalesTeamID")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig3, use_container_width=True)
    with col2:
        st.dataframe(profit_team_summary)
    create_download_button(profit_team_summary, "Profit_by_SalesTeam.csv")

elif selected_chart == "Total Sales by State":
    sales_region_summary = df.groupby('state')['Total Sales'].sum().reset_index()
    top_10_states = sales_region_summary.nlargest(10, 'Total Sales')
    fig4 = px.bar(sales_region_summary, x="state", y="Total Sales", labels={"Total Sales": "Total Sales {$}"},
                  title="Total Sales By State", template="plotly_white", height=500, color="state")
    fig_top_10 = create_secondary_plot(top_10_states, "state", "Total Sales", "Top 10 States by Total Sales", "bar")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig4, use_container_width=True)
    with col2:
        st.plotly_chart(fig_top_10, use_container_width=True)
    create_download_button(sales_region_summary, "Sales_by_state.csv")

elif selected_chart == "Total Profit by State":
    profit_region_summary = df.groupby('state')['Total Profit'].sum().reset_index()
    top_10_profit_states = profit_region_summary.nlargest(10, 'Total Profit')
    fig5 = px.bar(profit_region_summary, x="state", y="Total Profit", labels={"Total Profit": "Total Profit {$}"},
                  title="Total Profit By State", template="plotly_white", height=500, color="state")
    fig_top_10 = create_secondary_plot(top_10_profit_states, "state", "Total Profit", "Top 10 States by Total Profit", "bar")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig5, use_container_width=True)
    with col2:
        st.plotly_chart(fig_top_10, use_container_width=True)
    create_download_button(profit_region_summary, "Profit_by_state.csv")

elif selected_chart == "Most Sold Product by State":
    most_sold_product_state = df.groupby(['state', 'Product_id'])['Order Quantity'].sum().reset_index()
    fig6 = px.bar(most_sold_product_state, x="state", y="Order Quantity", color="Product_id", barmode='group',
                  title="Most Sold Product by State", labels={"Order Quantity": "Order Quantity"},
                  template="plotly_white", height=500)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig6, use_container_width=True)
    with col2:
        st.dataframe(most_sold_product_state)
    create_download_button(most_sold_product_state, "Most_Sold_Product_by_State.csv")

elif selected_chart == "Most Profitable Product":
    most_profitable_product = df.groupby('Product_id')['Total Profit'].sum().reset_index()
    fig7 = px.bar(most_profitable_product, x="Product_id", y="Total Profit", color="Product_id",
                  title="Most Profitable Product", labels={"Total Profit": "Total Profit {$}"},
                  template="plotly_white", height=500)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig7, use_container_width=True)
    with col2:
        st.dataframe(most_profitable_product)
    create_download_button(most_profitable_product, "Most_Profitable_Product.csv")

elif selected_chart == "Sales Distribution (Donut Chart)":
    sales_distribution = df.groupby('Product_id')['Total Sales'].sum().reset_index()
    fig8 = px.pie(sales_distribution, names="Product_id", values="Total Sales", title="Sales Distribution",
                  template="plotly_white", height=500, hole=0.5)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig8, use_container_width=True)
    with col2:
        st.dataframe(sales_distribution)
    create_download_button(sales_distribution, "Sales_Distribution.csv")

# Add a footer
footer_html = """
<div class="footer">
    <p>&copy; 2024 E-Commerce Analytics Dashboard. All rights reserved.</p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
