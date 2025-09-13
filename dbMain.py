#main streamlit file
import streamlit as st

pg = st.navigation([st.Page("dbOverview.py",title='Basic Information'),
                    st.Page("dbTargetAnalysis.py", title='Target Distribution Analysis'),
                    st.Page("dbNumericalFeatures.py", title='Numerical Feature Analysis'),
                    st.Page("dbCategoricalFeatures.py", title='Categorical Feature Analysis'),
                    st.Page("dbFeatureCorrelation.py", title='Feature Correlation Analysis')
                    ])
pg.run()