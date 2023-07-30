import streamlit as st

def main():
    # Title
    st.title("Logginator by Audiato")

    # Markdown
    st.markdown("Capturing log data and analyzing with a live model")

    # Writing area with streaming text
    text_input = st.text_area("Output from model predictions here", height=200)

    st.markdown("""### Upload a file ###
                Schema == """)
    
    # File Upload
    uploaded_file = st.file_uploader("Upload a file", type=["csv", "tsv", "json"])

    # Submit Button
    if st.button("Submit"):
        # Action when the Submit button is clicked
        if text_input:
            st.write("Text you entered:")
            st.write(text_input)

        if uploaded_file:
            st.write("Uploaded file details:")
            st.write("Filename:", uploaded_file.name)
            st.write("File type:", uploaded_file.type)
            st.write("File size:", uploaded_file.size)