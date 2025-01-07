# Rossmann Sales Prediction Project

## Project Overview
This project focuses on predicting sales for Rossmann stores based on historical sales data and various influencing factors. Two primary approaches were employed: Machine Learning (ML) and Deep Learning (DL). The project aims to enhance decision-making by forecasting sales trends, optimizing promotional strategies, and understanding store-specific dynamics.



## Business Objectives
1. **Sales Forecasting**: Predict future sales with high accuracy to support inventory and staffing decisions.
2. **Promotion Impact Analysis**: Evaluate how promotions influence sales trends across different stores.
3. **Seasonal and Holiday Trends**: Identify patterns in sales related to seasons and state holidays.
4. **Store Performance Evaluation**: Assess how store-specific features (e.g., assortment type, competition distance) affect overall sales.
5. **Actionable Insights**: Provide recommendations for improving marketing strategies and operational efficiency.



## Datasets
- **Train Dataset**: Historical sales data (`train.csv`).
- **Test Dataset**: Data for sales prediction (`test.csv`).
- **Store Dataset**: Store-related attributes (`store.csv`).
- **Sample Submission**: Template for submitting predictions (`sample_submission.csv`).



## Key Findings
### 1. State Holiday Sales Analysis
| StateHoliday | Average Sales |
|--------------|---------------|
| 0            | 5733.53       |
| a            | 290.73        |
| b            | 214.31        |
| c            | 168.73        |

### 2. Monthly Sales Trends
| Month | Average Sales |
|-------|---------------|
| 1     | 5465.40       |
| 12    | 6826.61       |

### 3. Sales and Customers Correlation
| Metric    | Sales  | Customers |
|-----------|--------|-----------|
| Sales     | 1.00   | 0.89      |
| Customers | 0.89   | 1.00      |

### 4. Promotional Impact
| Promo | Average Sales |
|-------|---------------|
| 0     | 4406.05       |
| 1     | 7991.15       |



## Tools and Technologies
- **Programming Language**: Python
- **Libraries**:
  - `pandas`, `numpy` for data manipulation.
  - `matplotlib`, `seaborn` for visualization.
  - `scikit-learn` for machine learning.
  - `tensorflow`, `keras` for deep learning.
  - `logging` for maintaining a record of execution.
- **Environment**: Jupyter Notebooks



## Methodologies
### Machine Learning
- **Feature Engineering**: Extracted key features such as month, year, day, and holiday indicators.
- **Modeling**: Employed Random Forest and XGBoost models for predictive analysis.
- **Evaluation**: Used metrics like RMSE and R² to evaluate model performance.

### Deep Learning
- **Neural Network Design**: Built a multi-layer perceptron (MLP) using TensorFlow and Keras.
- **Hyperparameter Tuning**: Optimized layers, activation functions, and learning rates.
- **Evaluation**: Assessed performance using validation accuracy and loss metrics.



## Recommendations
1. **Promotional Strategies**:
   - Focus promotions during high-traffic periods (e.g., holidays, weekends) to maximize sales.
   - Use personalized promotions based on customer segmentation.

2. **Sales Forecasting**:
   - Integrate predictive models into operational planning to better manage inventory and workforce.

3. **Store Optimization**:
   - Analyze competition distance and store characteristics to enhance store layouts and marketing efforts.

4. **Automated Pipelines**:
   - Automate data processing and model retraining to keep predictions up-to-date.



## How to Run the Project
### Prerequisites
1. Clone the repository:
   ```bash
   git clone https://github.com/Azazh/StoreForecast.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Notebooks
1. Execute the ML workflow:
   ```bash
   jupyter notebook rossmann_sales_prediction_ml.ipynb
   ```
2. Execute the ML workflow:
   ```bash
   jupyter notebook customer_behavior_eda.ipynb.ipynb
   ```
3. Execute the DL workflow:
   ```bash
   jupyter notebook rossmann_sales_prediction_dl.ipynb
   ```

### Running Tests
1. Run unit tests:
   ```bash
   python -m unittest discover -s tests
   ```



## References
- **Dataset Source**: Rossmann Store Sales dataset.
- **Documentation**: Standard GitHub templates and best practices.
- **Tools**: Python, TensorFlow, scikit-learn, pandas, matplotlib, seaborn.



## Future Work
1. Explore time series models (e.g., ARIMA, LSTM) for improved sales forecasting.
2. Incorporate external datasets (e.g., weather data) for deeper analysis.
3. Enhance model interpretability using SHAP or LIME.



