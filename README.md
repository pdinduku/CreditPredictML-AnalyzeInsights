# Credit Prediction

This repository contains different phases of the **Project**, which involves building a machine learning-based loan approval system.

## Project Phases
- **Phase 1**: Initial development and data preprocessing.
- **Phase 2**: Model training and evaluation.
- **Phase 3**: Deployment using Flask and a web interface.

## Project Structure
- `Phase1/` - Contains Phase 1 Jupyter Notebook.
- `Phase2/` - Contains Phase 2 Jupyter Notebook.
- `Phase3/`:
  - `templates/` - Contains HTML files for the website.
  - `static/` - Contains the CSS file for styling.
  - `app.py` - Flask application for deployment.
  - `model.py` - Machine learning model training script.
  - `model_rfc.pkl` - Trained RandomForest model.
  - `scaling.pickle` - Data scaler object.
  - `preprocessed_dataset.csv` - Processed dataset used for training.

## Dataset
The dataset used in this project is **Credit Score Classification**, available on Kaggle:
[Credit Score Classification - Kaggle](https://www.kaggle.com/datasets/parisrohan/credit-score-classification)

## How to Run
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd CreditPredictML-AnalyzeInsights
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python Phase3/app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

## Future Updates
Further improvements and additional deployment options will be explored.
