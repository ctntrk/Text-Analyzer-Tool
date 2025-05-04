import streamlit as st
import requests

API_URL = "http://localhost:5000/count"

def main():
    st.title("📝 Text Analysis Tool")
    
    with st.expander("📘 About the Project", expanded=False):
        st.markdown("""
                    **📊 Text Analysis Tool** is a web application that analyzes statistical features of your texts.

                    ✨ Key Features
                    - Real-time text analysis
                    - 5 different metric displays:
                      - Character count
                      - Word count
                      - Sentence count
                      - Unique words
                      - Paragraph count
                    - One-click clear functionality

                    🛠️ Technical Structure
                    - **Frontend:** Streamlit (Python)
                    - **Backend:** Flask (Python REST API)
                    - **Communication:** HTTP JSON-based

                    📌 How to Use?
                    1. Paste your text into the input box
                    2. Click "Analyze" button
                    3. View results in metric format
                    4. Use "Clear" button for new analysis
        """)
        
    st.write("Paste your text below and view statistics!")

    if 'text_input' not in st.session_state:
        st.session_state.text_input = ""

    def update_text():
        st.session_state.text_input = st.session_state.widget_text

    text_input = st.text_area(
        "Text Input", 
        height=200, 
        value=st.session_state.text_input, 
        key="widget_text",
        on_change=update_text
    )

    col1, col2 = st.columns(2)
    with col1:
        analyze_button = st.button("Analyze")
    with col2:
        clear_button = st.button("Clear")

    if clear_button:
        st.session_state.text_input = ""
        st.rerun()

    if analyze_button:
        if st.session_state.text_input.strip():
            try:
                response = requests.post(API_URL, json={"text": st.session_state.text_input})
                
                if response.status_code == 200:
                    results = response.json()
                    col1, col2, col3, col4, col5 = st.columns(5)
                    col1.metric("Characters", results['characters'])
                    col2.metric("Words", results['words'])
                    col3.metric("Sentences", results['sentences'])
                    col4.metric("Unique", results['unique_words'])
                    col5.metric("Paragraphs", results['paragraphs'])
                else:
                    st.error(f"API Error ({response.status_code}): {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to server. Please ensure Flask server is running.")
        else:
            st.warning("Please enter text for analysis!")

if __name__ == "__main__":
    main()
