st.sidebar.header("Filter By:")
category=st.sidebar.multiselect("Filter By Category:",
                                options=df["masterCategory"].unique(),
                                default=df["masterCategory"].unique()
                                )
filtered_data = df[df["masterCategory"].isin(category)]
st.write(filtered_data)
col1, col2,col3 = st.columns([0.1,0.45,0.45])
with col1:
    box_date=str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last updated by:\n {box_date}")
with col2:
    fig = px.bar(category_counts_df, x='Master Category', y='Total Count',
                 labels={'Master Category': 'Master Category', 'Total Count': 'Total Count'},
                 title="Total Count of Items in Each Master Category",
                 hover_data={'Total Count': True},
             width=600)  # Set the gap between bar groups)  # Include 'Total Count' in hover data
    st.plotly_chart(fig, user_container_width=True)

_, view1, dwn1,view2,dwn2=st.columns([0.15,0.20,0.20,0.20,0.20])
with view1:
    expander=st.expander("Master Category Wise Sales")
    expander.write(category_counts_df)
with dwn1:
    st.download_button("Get Data",data=category_counts_df.to_csv().encode("utf-8"),
                       file_name="MasterCategoryElementsCount.csv",mime="text/csv")
with col3:
    fig1=px.line(result_df_melted,x="year",y="Growth Rate",color='Category',title="Growth Rates of Apparel, Accessories, and Footwear",
                 template="gridon")
    st.plotly_chart(fig1,use_container_width=True)
with view2:
    expander=st.expander("Growth Rate of each Category")
    expander.write(result_df_melted)
with dwn2:
    st.download_button("Get Data", data=result_df_melted.to_csv().encode("utf-8"),
                       file_name="GrowthRatesOfEachCategory.csv",mime="text/csv")
st.divider()
