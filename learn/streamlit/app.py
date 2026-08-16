# import streamlit as st

# st.title("My First Streamlit App")

# st.write("Hello Bala!")

# st.write("Welcome to Streamlit")

# st.title()
# st.header()
# st.subheader()
# st.write()

# st.text_input()
# st.number_input()
# st.text_area()

# st.button()
# st.checkbox()
# st.radio()
# st.selectbox()
# st.multiselect()
# st.slider()

# st.success()
# st.error()
# st.warning()
# st.info()

import streamlit as st

st.title("Employee Salary Calculator")

name = st.text_input("Employee Name")

salary = st.number_input(
    "Current Salary",
    min_value=0
)

hike = st.slider(
    "Hike Percentage",
    0,
    100,
    10
)

if st.button("Calculate"):

    hike_amount = salary * hike / 100
    new_salary = salary + hike_amount

    st.write("Employee:", name)
    st.write("Current Salary:", salary)
    st.write("Hike:", hike, "%")
    st.success(f"New Salary: ₹{new_salary}")