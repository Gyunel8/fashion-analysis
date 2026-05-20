import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Fashion Analytics", layout="wide")

# Загрузка данных
file_path = "fashion_boutique_dataset_CLEAN.csv"
try:
    df = pd.read_csv(file_path)
except Exception as e:
    st.error(f"Не удалось загрузить файл: {e}")
    st.stop()

# Навигация
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Dashboard Overview", "Returns Analysis", "Profitability"])
brand = st.sidebar.selectbox("Filter by Brand", ["All Brands"] + list(df["brand"].unique()))
df_f = df if brand == "All Brands" else df[df["brand"] == brand]

# --- СТРАНИЦЫ ---
if page == "Dashboard Overview":
    st.title("👗 Fashion Performance Dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Revenue", f"${df_f['current_price'].sum():,.0f}")
    c2.metric("Discount Loss", f"${(df_f['original_price'] - df_f['current_price']).sum():,.0f}")
    c3.metric("Returns (pcs)", int(df_f['is_returned'].sum()))
    c4.metric("Avg Rating", f"{df_f['customer_rating'].mean():.1f}")
    
    st.subheader("📋 Category Summary")
    summary = df_f.groupby("category").agg({"current_price": "sum", "stock_quantity": "sum"}).reset_index()
    st.dataframe(summary, use_container_width=True)

elif page == "Returns Analysis":
    st.title("⚠️ Returns Deep Dive")
    ret_df = df_f[df_f['is_returned'] == True]
    if not ret_df.empty:
        ret_data = ret_df["return_reason"].value_counts().reset_index()
        fig = px.bar(ret_data, x="count", y="return_reason", orientation='h', color="count")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Нет данных о возвратах для выбранного фильтра.")

elif page == "Profitability":
    st.title("🎯 Profitability Analysis")
    # Используем .sum() для колонки is_returned, так как это True/False
    cat_analysis = df_f.groupby("category").agg({"current_price": "sum", "is_returned": "sum"}).reset_index()
    fig = px.scatter(cat_analysis, x="is_returned", y="current_price", size="is_returned", 
                     color="category", text="category", size_max=60)
    st.plotly_chart(fig, use_container_width=True)