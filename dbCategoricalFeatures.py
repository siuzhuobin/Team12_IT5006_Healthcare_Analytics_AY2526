# categorical feature page 
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from dbShared import load_data


@st.cache_data
# wrapper function to be decorated by st.cache_data for static content 
def categorical_feature_static_items():
    X, y, df = load_data()
    st.header("Categorical Feature Distribution and Unique Value Analysis")

    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    print(f"Categorical features: {len(categorical_cols)}")
    
    # Unique value statistics
    unique_counts = {col: df[col].nunique() for col in categorical_cols}
    unique_df = pd.DataFrame(list(unique_counts.items()), 
                           columns=['Feature', 'Unique Count']).sort_values('Unique Count')
    
    st.subheader("Unique Value Statistics")
    st.dataframe(unique_df)
    
    # identify low cardinality features as those with unique counts of less than 10
    low_cardinality = unique_df[unique_df['Unique Count'] <= 10]
    return X, y, df, low_cardinality



X, y, df, low_cardinality = categorical_feature_static_items()

st.subheader('Visualization of Low-cardinality Features (<= 10)')
cbX = st.selectbox(label='Categorical feature', options=sorted(low_cardinality["Feature"]), index=0, key='cbX')



plt.clf()
plt.figure()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))


col = cbX
ax = df[col].value_counts().plot(kind='bar', color='lightcoral', ax = ax1)
ax1.set_title(f'{col} distribution')
ax1.tick_params(axis='x', rotation=45)



crosstab = pd.crosstab(df[col], df['readmitted'], normalize='index') * 100

# Draw stacked bar chart
crosstab.plot(kind='bar', stacked=True, ax=ax2,
                color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
ax2.set_title(f'{col} vs Readmission Status')
ax2.set_ylabel('Percentage (%)')
ax2.legend(title='Readmission Status')
ax2.tick_params(axis='x', rotation=45)
st.pyplot(fig)






    
