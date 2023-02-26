import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(page_title ='Loan Amount')
st.header('Distribution of loans across the states')


'''We have a dataset consists of loans distribution across the states based on Due Dates and Date of birth'''

data = pd.read_csv('Portfolio_data.csv')
st.write(data)


st.write("## Slider to the Streamlit app where the user can select a range of loan amounts")

min_loan_amount = int(data['Loan Amount'].min())
max_loan_amount = int(data['Loan Amount'].max())
selected_loan_amount = st.slider('Filter by Loan Amount', min_loan_amount, max_loan_amount, (min_loan_amount, max_loan_amount))
filtered_data = data[(data['Loan Amount'] >= selected_loan_amount[0]) & (data['Loan Amount'] <= selected_loan_amount[1])]
st.write(filtered_data)



st.write("## Scatter Plot of Loan Amount vs Due Date")
scatter_plot = alt.Chart(data).mark_circle(size=60).encode(
    x="Due Date:T",
    y="Loan Amount:Q",
    color="State:N",
    tooltip=["Loan Number", "Due Date", "State", "DOB", "Loan Amount"],).properties(width=800, height=400)
st.altair_chart(scatter_plot, use_container_width=True)


st.write("## Pie Chart of Loan Amount by State")
pie_data = data.groupby("State")["Loan Amount"].sum().reset_index()
pie_chart = alt.Chart(pie_data).mark_arc().encode(
    x=alt.value(0),
    y=alt.value(0),
    color="State:N",
    tooltip=["State", "Loan Amount"], theta="Loan Amount:Q",).properties(width=400, height=400)
st.altair_chart(pie_chart, use_container_width=True)

st.write("## Line Chart of Loan Amount by Loan Number")
line_data = data[["Loan Number", "Loan Amount"]]
line_chart = alt.Chart(line_data).mark_line().encode(
    x=alt.X("Loan Number:Q", title="Loan Number"),
    y=alt.Y("Loan Amount:Q", title="Loan Amount ($USD)"),
    tooltip=["Loan Number", "Loan Amount"],).properties(width=800, height=400)
st.altair_chart(line_chart, use_container_width=True)

st.write("## Histograms shows the Loan Amount count based on the Amount range")

plt.hist(data['Loan Amount'], bins=20)
st.pyplot()

st.write("## Bar chart shows the relationship between States and Loan Amount")

loan_amount_by_state = data.groupby('State').sum()['Loan Amount']
plt.bar(loan_amount_by_state.index, loan_amount_by_state.values)
plt.xticks(rotation=45)
st.pyplot()
