import pandas as pd
from pandas_profiling import ProfileReport

import streamlit as st
from streamlit_pandas_profiling import st_profile_report

st.header("`streamlit_pandas_profiling`")

df = pd.read_csv(
    "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
)

pr = ProfileReport(df)
st_profile_report(pr)
