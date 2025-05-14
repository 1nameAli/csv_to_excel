import pandas as pd
import streamlit as st

# Page settings
st.set_page_config(page_title="CSV to Excel Converter", layout="centered")
st.title("📁 CSV to Excel Converter")

st.write("Upload a CSV file and convert it to Excel (.xlsx) format.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV
    try:
        df = pd.read_csv(uploaded_file)
        st.success("CSV file loaded successfully!")
        
        st.subheader("🔍 Preview of CSV:")
        st.dataframe(df.head())

        # Convert to Excel in memory
        from io import BytesIO
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        processed_data = output.getvalue()

        # Download button
        st.download_button(
            label="📥 Download as Excel",
            data=processed_data,
            file_name="converted_file.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"❌ Error reading CSV: {e}")
