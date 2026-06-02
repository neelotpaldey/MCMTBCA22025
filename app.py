import streamlit as st
import pandas as pd

SHEET_ID = "1jCi5Z4Heyy21fCPwQZcKzfImQ6VK4oJ9v_FEAV_VCPk"

url = "https://docs.google.com/spreadsheets/d/" + SHEET_ID + "/export?format=csv&gid=0"

df = pd.read_csv(url, header=1)

st.title("Student Marks Portal")

name_list = ["Select Name"] + sorted(df["Name"].dropna().unique())

selected_name = st.selectbox(
    "Select Student",
    name_list
)

if selected_name != "Select Name":

    student = df[df["Name"] == selected_name].iloc[0]

    sessional = pd.DataFrame({
        "Subject": ["OB", "DE", "C", "FA", "DM"],
        "Marks (25)": [
            student.iloc[2],
            student.iloc[3],
            student.iloc[4],
            student.iloc[5],
            student.iloc[6]
        ]
    })

    put = pd.DataFrame({
        "Subject": ["OB", "DE", "C", "FA", "DM"],
        "Marks (75)": [
            student.iloc[13],
            student.iloc[9],
            student.iloc[11],
            student.iloc[12],
            student.iloc[10]
        ]
    })

    # Replace blanks and NaN with "Result Soon"
    sessional = sessional.fillna("Result Soon")
    put = put.fillna("Result Soon")

    sessional = sessional.replace("", "Result Soon")
    put = put.replace("", "Result Soon")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sessional Marks (Out of 25)")
        st.dataframe(
            sessional,
            hide_index=True,
            use_container_width=True
        )

    with col2:
        st.subheader("PUT Marks (Out of 75)")
        st.dataframe(
            put,
            hide_index=True,
            use_container_width=True
        )
