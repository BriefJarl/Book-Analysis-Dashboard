 📊 Book Analysis Dashboard

A full-stack data application that analyzes book data with an interactive dashboard and a live backend API.

---

## 🚀 Features

- 🔍 Search books by title  
- 🎯 Filter by price & rating  
- 📊 Visual insights (ratings & price distribution)  
- 📈 Top 10 most expensive books  
- 🌙 Dark/Light mode toggle  
- 📥 Export filtered data as CSV  
- 🔗 Integrated Flask API backend  

---

## 🧠 What This Project Demonstrates

- End-to-end data pipeline (scraping → cleaning → visualization)  
- Frontend + backend integration  
- REST API development  
- Real-time data filtering & UI interaction  
- Deployment-ready architecture  

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Flask  
- **Data**: Pandas  
- **Visualization**: Seaborn, Matplotlib  
- **API Integration**: Requests  
- **Deployment**: Streamlit Cloud, Render  

---

## 🌐 Live Demo

- 🔗 Frontend: https://book-dashboard-analysis-96.streamlit.app  
- 🔗 Backend API: https://book-analysis-dashboard.onrender.com/books  

---

## 🔐 Demo Login

Username: `admin`  
Password: `1234`  

> Note: This is a demo login system to simulate access control.

---

## 📂 Project Structure


.
├── app.py # Streamlit frontend
├── api.py # Flask backend API
├── data/ # Dataset
├── requirements.txt
└── README.md


---

## 📊 Data Source

🔗 https://books.toscrape.com  

---

## ⚙️ How to Run Locally

```bash
# Run backend
python api.py

# Run frontend
streamlit run app.py
🎯 Future Improvements
Proper user authentication (JWT/OAuth)
Database integration (MongoDB/PostgreSQL)
Docker containerization
CI/CD pipeline
👤 Author

Bhumika Shaw
