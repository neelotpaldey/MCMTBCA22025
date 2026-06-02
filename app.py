import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Student Marks", page_icon="📊")

# Google Sheet Connection
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "service_account.json",
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1jCi5Z4Heyy21fCPwQZcKzfImQ6VK4oJ9v_FEAV_VCPk"
).sheet1

data = sheet.get_all_values()

# Header row is row 2 in your sheet
headers = data[1]
rows = data[2:]

df = pd.DataFrame(rows, columns=headers)

st.title("Student Marks Portal")

name_list = sorted(df["Name"].dropna().unique())

selected_name = st.selectbox(
    "Select Student",
    name_list
)

if selected_name:

    student = df[df["Name"] == selected_name].iloc[0]

    sessional_df = pd.DataFrame({
        "Subject": ["OB", "DE", "C", "FA", "DM"],
        "Marks (25)": [
            student.iloc[2],   # C
            student.iloc[3],   # D
            student.iloc[4],   # E
            student.iloc[5],   # F
            student.iloc[6]    # G
        ]
    })

    put_df = pd.DataFrame({
        "Subject": ["OB", "DE", "C", "FA", "DM"],
        "Marks (75)": [
            student.iloc[13],  # N
            student.iloc[9],   # J
            student.iloc[11],  # L
            student.iloc[12],  # M
            student.iloc[10]   # K
        ]
    })

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sessional Marks (Out of 25)")
        st.dataframe(
            sessional_df,
            use_container_width=True,
            hide_index=True
        )

    with col2:
        st.subheader("PUT Marks (Out of 75)")
        st.dataframe(
            put_df,
            use_container_width=True,
            hide_index=True
        )
