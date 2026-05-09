# Titanic Survival Predictor

This is a Streamlit application that uses a Machine Learning model to predict whether a passenger would have survived the Titanic disaster.

## Features
- **Ticket Class (Pclass)**: Socio-economic status (1st, 2nd, 3rd).
- **Sex**: Male or Female.
- **Port of Embarkation**: Southampton, Cherbourg, or Queenstown.
- **SibSp**: Number of siblings or spouses aboard.
- **Parch**: Number of parents or children aboard.
- **Fare**: Passenger fare.

## Project Structure
```
advanced-assignments-4-5/
├── assets/                                # Images/logos (Optional)
├── data/                                   # Dataset files (train.csv, etc.)
├── app.py                                 # Streamlit application
├── model.joblib                           # Trained ML model
├── notebook.ipynb                         # Original training notebook
├── requirements.txt                       # Dependency list
└── README.md                              # Project documentation
```

## How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dnnuuyzzo/advanced-assignments-4-5.git
   cd advanced-assignments-4-5
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # Mac/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## Deployment
This app is designed to be deployed on **Streamlit Community Cloud**.
