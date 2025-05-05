# 📝 **Text Analyzer Tool** 📊

The **Text Analysis Tool** is a simple web application that allows users to input their text and get various statistical insights in real-time. By pasting a block of text into the interface, users can instantly see key metrics such as character count, word count, sentence count, unique words, and paragraph count.

This project uses **Streamlit** for the frontend and **Flask** for the backend, working together to provide a smooth user experience with instant results.

---

## Text Analyzer Tool Demo Introduction Video

https://github.com/user-attachments/assets/0b8ac185-b215-4f52-b7a4-747e4774a372


---

## 🚀 **Features**

* **Character Count**: Displays the total number of characters in the text.
* **Word Count**: Provides the total number of words.
* **Sentence Count**: Calculates how many sentences the text contains.
* **Unique Words**: Counts the number of distinct words in the text.
* **Paragraph Count**: Shows how many paragraphs are present in the text.

---

## 🛠️ **Technologies Used**

* **Frontend**: Streamlit (Python)
* **Backend**: Flask (Python REST API)
* **Communication**: HTTP JSON-based API

---


## 📄 **Project Overview**

This application is designed to offer quick and accurate text analysis through a simple and interactive web interface. It allows users to gain insights into the structure and complexity of any given text, such as the total number of characters, words, sentences, paragraphs, and distinct words.

* **Streamlit** is used to create a clean and interactive user interface, where users can easily input their text and see results in real time.
* **Flask** serves as the backend to process and analyze the text, returning the statistical data to the frontend.

This project is perfect for anyone who wants to analyze the basic statistics of their text quickly and effortlessly. It can be particularly useful for writers, students, and educators who need to evaluate their content.

## Text-Analyzer-Tool Web Interface

![Alt text](https://github.com/ctntrk/Text-Analyzer-Tool/blob/main/Text-Analyzer-Tool-Web-Interface.jpg)

---

## Result Screen After Analysis

![Alt text](https://github.com/ctntrk/Text-Analyzer-Tool/blob/main/Result-Screen-After-Analysis.jpg)


---

## 💡 **How to Use**

1. **Paste Your Text**: Start by pasting your text into the input area on the Streamlit interface.
2. **Click "Analyze"**: Once your text is entered, click the **"Analyze"** button to view the statistical breakdown.
3. **Click "Clear"**: You can reset the input and start fresh by clicking the **"Clear"** button.

---

## 🔧 **Technical Setup**

### **Frontend: Streamlit**

The frontend of this application is built using **Streamlit**, a Python library that allows for the rapid creation of interactive web applications. The interface allows users to enter text, click the "Analyze" button to view results, and interact with the application.

* **Input Text**: Users can paste text into a text area.
* **Analyze Button**: Triggers an HTTP request to the backend Flask API to process the text and retrieve statistics.
* **Clear Button**: Clears the input area for a fresh start.

### **Backend: Flask**

The backend is built with **Flask**, a micro web framework for Python. Flask handles HTTP POST requests and performs the text analysis, returning a JSON response with the statistics to the frontend.

* **Text Processing**: The backend processes the input text to calculate metrics such as character count, word count, sentence count, unique words, and paragraph count.
* **API**: The backend exposes a POST API at `/count` that receives the text and returns the computed statistics.

---

## 📦 **Installation and Setup**

To run this project locally, follow these steps:

1. **Install Dependencies**:

   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask Backend**:

   Navigate to the `app.py` file and start the Flask API:

   ```bash
   python app.py
   ```

   This will start the Flask API on `http://localhost:5000`.

3. **Run the Streamlit Frontend**:

   Open a new terminal and navigate to the folder containing `streamlit-app.py`. Start the Streamlit app:

   ```bash
   streamlit run streamlit-app.py
   ```

   The Streamlit app will open in your browser, and you can start using the text analysis tool.

---

## ⚙️ **Endpoints**

### **POST /count**

* **Request Body** (JSON format):

  ```json
  {
    "text": "Your text goes here"
  }
  ```

* **Response Body** (JSON format):

  ```json
  {
    "characters": 1500,
    "words": 250,
    "sentences": 15,
    "unique_words": 150,
    "paragraphs": 5
  }
  ```


## 📝 **Conclusion**

In summary, this **Text Analysis Tool** offers a user-friendly platform for performing text analysis, built with **Streamlit** for the frontend and **Flask** for the backend. The application provides immediate feedback on important text metrics, allowing users to quickly understand the structure and content of their written material.

---

## 📚 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
