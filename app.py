import streamlit as st
import pandas as pd
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="E-Commerce Sales Analysis & Demand Prediction",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>

.main{
    background-color:#f6f8fb;
}

.block-container{
    padding-top:1.5rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

h1,h2,h3{
    color:#0F172A;
}

.metric-card{
    background:white;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
    border-left:5px solid #2563EB;
}

.info-card{
    background:white;
    padding:18px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

.sidebar .sidebar-content{
    background:#ffffff;
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# Load Dataset
csv_path = Path("results/demand_forecast.csv")
if not csv_path.exists():
    st.error("❌ demand_forecast.csv not found.")
    st.stop()
forecast_df = pd.read_csv(csv_path)

# Header
st.title("📦 E-Commerce Sales Analysis & Demand Prediction")
st.markdown("""
Analyze historical e-commerce sales data, predict future product demand using
**Machine Learning (Random Forest Regressor)** and generate inventory
recommendations for efficient stock management.
""")
st.divider()

# Sidebar
st.sidebar.image(
    "https://img.icons8.com/fluency/96/shopping-cart-loaded.png",
    width=80
)
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "",
    [
        "🏠 Dashboard",
        "🔍 Product Search",
        "📊 Visualizations"
    ]
)
st.sidebar.divider()
st.sidebar.subheader("Project Information")
st.sidebar.write("**Project**")
st.sidebar.write("E-Commerce Sales Analysis & Demand Prediction")
st.sidebar.write("**Model**")
st.sidebar.success("Random Forest Regressor")
st.sidebar.write("**Dataset**")
st.sidebar.info("DataCo Supply Chain Dataset")
st.sidebar.divider()
st.sidebar.subheader("Developer")
st.sidebar.write("**Kavita Seervi**")
st.sidebar.caption(
"""
B.Tech CSE (Data Science)

Manipal University Jaipur
"""
)

# Useful Statistics
total_products = len(forecast_df)
avg_prediction = round(
    forecast_df["Predicted Demand"].mean(),
    2
)

high_products = (
    forecast_df["Demand Level"]=="High"
).sum()

medium_products = (
    forecast_df["Demand Level"]=="Medium"
).sum()

low_products = (
    forecast_df["Demand Level"]=="Low"
).sum()

# DASHBOARD

if page == "🏠 Dashboard":

    st.header("📊 Dashboard Overview")

    st.markdown(
        """
        Welcome to the **E-Commerce Sales Analysis & Demand Prediction Dashboard**.

        This dashboard presents demand forecasting results generated using the
        **Random Forest Regressor** model. It provides an overview of predicted
        product demand along with inventory recommendations.
        """
    )

    st.write("")

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📦 Total Products",
            value=f"{total_products:,}"
        )

    with col2:
        st.metric(
            label="📈 Average Predicted Demand",
            value=avg_prediction
        )

    with col3:
        st.metric(
            label="🔥 High Demand Products",
            value=f"{high_products:,}"
        )

    with col4:
        st.metric(
            label="📉 Low Demand Products",
            value=f"{low_products:,}"
        )

    st.divider()

    # Project Summary

    left, right = st.columns([2,1])

    with left:

        st.subheader("📌 Project Summary")

        st.markdown(
        """
        This project performs:

        - Sales Data Analysis
        - Demand Forecasting
        - Inventory Recommendation
        - Product-wise Demand Prediction
        - Machine Learning based Decision Support

        The final prediction model uses the **Random Forest Regressor**
        because it achieved better performance compared to Linear Regression.
        """
        )

    with right:

        st.subheader("📋 Model Information")

        st.info(
        f"""
**Algorithm**

Random Forest Regressor

**Dataset**

DataCo Supply Chain Dataset

**Records**

{total_products:,}

**Target Variable**

Order Item Quantity
        """
        )

    st.divider()

    # Demand Distribution Summary

    st.subheader("📦 Demand Distribution")

    d1, d2, d3 = st.columns(3)

    with d1:
        st.success(
            f"""
High Demand Products

**{high_products:,}**
            """
        )

    with d2:
        st.warning(
            f"""
Medium Demand Products

**{medium_products:,}**
            """
        )

    with d3:
        st.error(
            f"""
Low Demand Products

**{low_products:,}**
            """
        )

    st.divider()

    # Dataset Preview
    st.subheader("📄 Forecast Preview")

    preview_columns = [
        "Product Name",
        "Category Name",
        "Department Name",
        "Predicted Demand",
        "Demand Level",
        "Inventory Recommendation"
    ]

    st.dataframe(
        forecast_df[preview_columns].head(15),
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Showing the first 15 predicted products from the demand forecast."
    )

    st.divider()

    # Key Business Insights

    st.subheader("💡 Business Insights")

    insight1, insight2 = st.columns(2)

    with insight1:

        st.info(
        """
### Key Observations

• Random Forest successfully predicts future demand.

• Products are classified into High, Medium and Low demand.

• Inventory recommendations help optimize stock levels.

• Forecasting reduces overstocking and stock shortages.
        """
        )

    with insight2:

        st.success(
        """
### Inventory Recommendations

✅ Increase Stock → High Demand

✅ Maintain Stock → Medium Demand

✅ Reduce Stock → Low Demand
        """
        )

    st.divider()

# PRODUCT SEARCH
elif page == "🔍 Product Search":

    st.header("🔍 Product Search")

    st.markdown(
        """
Search any product to view its predicted demand,
inventory recommendation and product information.
        """
    )

    st.divider()

    # Product Selection

    product = st.selectbox(
        "Select Product",
        sorted(forecast_df["Product Name"].unique())
    )

    result = forecast_df[
        forecast_df["Product Name"] == product
    ]

    if not result.empty:

        row = result.iloc[0]

        # Product Information

        st.subheader("📦 Product Information")

        left, right = st.columns([2,1])

        with left:

            st.markdown(f"### {row['Product Name']}")

            st.write(f"**Category:** {row['Category Name']}")
            st.write(f"**Department:** {row['Department Name']}")
            st.write(f"**Region:** {row['Order Region']}")
            st.write(f"**Shipping Mode:** {row['Shipping Mode']}")

            if "Product Price" in result.columns:
                st.write(
                    f"**Product Price:** ${row['Product Price']:.2f}"
                )

        with right:

            st.info(
f"""
### Prediction

**Predicted Demand**

{row['Predicted Demand']:.2f}

**Demand Level**

{row['Demand Level']}

**Recommendation**

{row['Inventory Recommendation']}
"""
            )

        st.divider()

        # Prediction Summary Cards

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "📈 Predicted Demand",
                round(row["Predicted Demand"],2)
            )

        with c2:

            st.metric(
                "🔥 Demand Level",
                row["Demand Level"]
            )

        with c3:

            st.metric(
                "📦 Inventory Action",
                row["Inventory Recommendation"]
            )

        st.divider()

        # Complete Product Record

        st.subheader("📄 Product Record")

        st.dataframe(
            result,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        # Business Interpretation
        st.subheader("💡 Business Interpretation")

        demand = row["Demand Level"]

        if demand == "High":

            st.success(
                """
### High Demand Product

This product has high predicted demand.

Recommended Action:

- Increase Inventory
- Monitor Stock Frequently
- Avoid Stock-Out Situations
                """
            )

        elif demand == "Medium":

            st.warning(
                """
### Medium Demand Product

This product has stable demand.

Recommended Action:

- Maintain Current Inventory
- Monitor Weekly Sales
                """
            )

        else:

            st.error(
                """
### Low Demand Product

This product has low predicted demand.

Recommended Action:

- Reduce Overstock
- Avoid Excess Inventory
                """
            )

    else:

        st.warning("No product found.")

# VISUALIZATIONS
elif page == "📊 Visualizations":

    st.header("📊 Demand Forecast Visualizations")

    st.markdown(
        """
These visualizations summarize the sales analysis and demand forecasting
results generated by the Machine Learning model.
        """
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Demand Level Distribution")

        st.image(
            "images/demand_level_distribution.png",
            use_container_width=True
        )

        st.caption(
            "Distribution of products classified into High, Medium and Low demand."
        )

    with col2:

        st.subheader("Inventory Recommendation")

        st.image(
            "images/inventory_recommendation.png",
            use_container_width=True
        )

        st.caption(
            "Recommended inventory actions based on predicted demand."
        )

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        st.subheader("Top Predicted Products")

        st.image(
            "images/top_predicted_products.png",
            use_container_width=True
        )

        st.caption(
            "Products with the highest predicted demand."
        )

    with col4:

        st.subheader("Shipping Mode Analysis")

        st.image(
            "images/shipping_mode_prediction.png",
            use_container_width=True
        )

        st.caption(
            "Average predicted demand across different shipping modes."
        )

    st.divider()

    st.subheader("📌 Key Insights")

    insight1, insight2 = st.columns(2)

    with insight1:

        st.success(
        """
### Business Insights

- Machine Learning successfully predicts future demand.

- Demand forecasting helps businesses optimize inventory.

- High-demand products require increased stock.

- Low-demand products should be monitored to avoid overstocking.
        """
        )

    with insight2:

        st.info(
        """
### Dashboard Summary

✔ Sales Analysis

✔ Demand Prediction

✔ Inventory Recommendation

✔ Product Search

✔ Data Visualization
        """
        )

# FOOTER
st.markdown("---")

footer_left, footer_right = st.columns([3,1])

with footer_left:

    st.caption(
    """
**E-Commerce Sales Analysis & Demand Prediction**

Developed as a Machine Learning project for analyzing sales data,
forecasting product demand, and generating inventory recommendations.

**Developer:** Kavita Seervi

B.Tech Computer Science & Engineering (Data Science)

Manipal University Jaipur
    """
    )

with footer_right:

    st.caption(
    """
Version 1.0

Machine Learning Project

Random Forest Regressor
    """
    )