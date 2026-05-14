# 📊 Sales Prediction using Machine Learning

An end-to-end Machine Learning project that predicts sales revenue based on customer and product data. Built using Python with a fully functional Streamlit web application for real-time predictions.

---

## 🚀 Live Demo
Run locally:
streamlit run app.py

text
Open → `http://localhost:8501`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core programming language |
| Pandas & NumPy | Data manipulation |
| Scikit-learn | Machine learning model |
| Matplotlib | Data visualization |
| Streamlit | Frontend web application |
| Joblib | Model saving and loading |
| Jupyter Notebook | Development environment |

---

## 📁 Project Structure
sales-prediction/
├── app.py ← Streamlit frontend UI
├── models/
│ ├── sales_model.pkl ← Trained ML model
│ └── feature_columns.pkl
├── data/
│ ├── sales_data.csv
│ ├── sales_data_cleaned.csv
│ └── *.png (charts)
└── notebooks/
├── 01_data_exploration.ipynb
├── 02_data_preprocessing.ipynb
├── 03_model_training.ipynb
└── 04_model_evaluation.ipynb

text

---

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| R² Score | **0.8454 (84.5%)** |
| MAE | ₹5,077 |
| RMSE | ₹7,051 |
| Dataset Size | 1000 records |

---

## ▶️ How to Run

```bash
# Install dependencies
pip install pandas numpy scikit-learn matplotlib streamlit joblib jupyter

# Launch web app
cd sales-prediction
streamlit run app.py
```

---

## 💡 Key Insights

- **UnitPrice** is the strongest predictor of Sales
- **Quantity** directly drives total revenue
- **Discount** has slight negative impact
- Region and Product have minor influence

---

## 👨‍💻 Author
**Mukesh**
