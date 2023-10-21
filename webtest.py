try:
    import os
    import sys
    import streamlit as st 
    import pandas as pd
    from io import BytesIO, StringIO
    print("All Modules Loaded ")
except Exception as e:
    print("Some Modules are missing: {} ").format(e)
    
STYLE = """
<style>
img {
    max-width: 100%
}
</style>
"""
    
def main():
    st.info(__doc__)
    st.markdown(STYLE, unsafe_allow_html= True)
    file = st.file_uploader("Upload file", type = ["csv", "png", "jpg"])
    show_file = st.empty()
    
    if not file:
        show_file.info("Please Upload a file: {} ".format(' '.join(["csv", "png", "jpg"])))
        return
    content = file.getvalue()
    
    if isinstance(file, BytesIO):
        show_file.image(file)
    else:
        df = pd.read_csv(file)
        st.dataframe(df.head(2))
    file.close()

main()
    
    