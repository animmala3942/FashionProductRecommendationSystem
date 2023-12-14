def generate_bar_chart(filtered_data):
    fig = px.bar(filtered_data, x='Master Category', y='Total Count',
                 labels={'Master Category': 'Master Category', 'Total Count': 'Total Count'},
                 title="Total Count of Items in Each Master Category",
                 hover_data={'Total Count': True},
                 width=600)
    return fig


# Function to generate the line chart based on the filtered data
def generate_line_chart(filtered_data):
    fig = px.line(filtered_data, x="year", y="Growth Rate", color='Category',
                  title="Growth Rates of Apparel, Accessories, and Footwear",
                  template="gridon")
    return fig


st.sidebar.header("Filter By:")
category = st.sidebar.multiselect("Filter By Category:",
                                  options=df["masterCategory"].unique(),
                                  default=df["masterCategory"].unique())

filtered_data = df[df["masterCategory"].isin(category)]

# Display filtered data
st.write(filtered_data)

col1, col2, col3 = st.columns([0.1, 0.45, 0.45])
with col1:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last updated by:\n {box_date}")

with col2:
    filtered_category_counts = category_counts_df[category_counts_df['Master Category'].isin(category)]
    fig = generate_bar_chart(filtered_category_counts)
    st.plotly_chart(fig, use_container_width=True)

_, view1, dwn1, view2, dwn2 = st.columns([0.15, 0.20, 0.20, 0.20, 0.20])
with view1:
    expander = st.expander("Master Category Wise Sales")
    expander.write(filtered_category_counts)

with dwn1:
    st.download_button("Get Data", data=filtered_category_counts.to_csv().encode("utf-8"),
                       file_name="MasterCategoryElementsCount.csv", mime="text/csv")

with col3:
    filtered_result_df = result_df_melted[result_df_melted['Category'].isin(category)]
    fig1 = generate_line_chart(filtered_result_df)
    st.plotly_chart(fig1, use_container_width=True)

with view2:
    expander = st.expander("Growth Rate of each Category")
    expander.write(filtered_result_df)

with dwn2:
    st.download_button("Get Data", data=filtered_result_df.to_csv().encode("utf-8"),
                       file_name="GrowthRatesOfEachCategory.csv", mime="text/csv")

st.divider()
