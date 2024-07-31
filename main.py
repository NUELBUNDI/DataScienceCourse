import streamlit as st


python     = st.Page("Learn Data Science/python.py",     title="Python",     icon="📟", default=True)
pandas     = st.Page("Learn Data Science/pandas.py",    title="Pandas",      icon="🐼",)
matplotlib = st.Page("Learn Data Science/matplotlib.py", title="Matplotlib", icon="📊")
seaborn    = st.Page("Learn Data Science/seaborn.py", title="Seaborn",       icon="📶")
search     = st.Page("Machine Learning/search.py", title="Search", icon=":material/search:")
history    = st.Page("Machine Learning/history.py", title="History", icon=":material/history:")






pg = st.navigation(
        {
            "Learn Data Science"  : [python, pandas, matplotlib,seaborn],
            "Machine Learning"    : [search, history],
        }
    )
pg.run()