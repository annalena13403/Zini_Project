# PE4MOVE – Predicting Physical Activity Intervention Outcomes with Machine Learning

This repository contains the code and data used for a machine learning project investigating whether changes in physical activity after a school-based intervention can be predicted from baseline participant characteristics.

The project is based on data from the **PE4MOVE** study and focuses on predicting individual intervention success using supervised regression models.

---

## Project Aim

School-based physical activity interventions often show large differences in effectiveness between individuals.  
The aim of this project is to:

- predict changes in physical activity outcomes following the intervention using baseline data only, and  
- identify which baseline characteristics are most informative for explaining individual differences in intervention response.

The prediction task is formulated as a regression problem, where changes in physical activity between baseline (T0) and follow-up (T1) are modeled.

---

## Repository Structure


---

## Main Notebooks

### `data_preparation.ipynb`  *(main notebook)*

This notebook contains all preprocessing and feature construction steps used for the final analysis.  
It includes:

- loading and merging intervention-related datasets,
- filtering to the intervention group,
- handling missing values and intentional non-responses,
- encoding categorical variables,
- standardizing continuous variables,
- aggregating questionnaire items into scale scores,
- selecting baseline predictors and precomputed change scores (\(\Delta\)) as targets.

All preprocessing steps are designed to ensure reproducibility and to prevent information leakage.

---

### `Prediction_FeatureRanking.ipynb`  *(main notebook)*

This notebook contains the core machine learning analysis, including:

- train–test split,
- model comparison using five-fold cross-validation,
- hyperparameter tuning with GridSearchCV,
- final evaluation on a held-out test set,
- feature importance analysis using Random Forest models,
- grouping of feature importance results by conceptual categories.

This notebook produces the results reported in the final project report.

---

## Supporting Notebooks

### `initial_exploration.ipynb`
Exploratory data analysis conducted at the beginning of the project to understand the structure, distributions, and completeness of the data.

### `exploring_features.ipynb`
Additional exploratory analyses focused on inspecting individual features, correlations, and potential predictors.  
These notebooks supported feature selection decisions but are not part of the final modeling pipeline.

---

## Prediction Targets

Separate regression models are trained for the following outcomes, defined as changes from baseline (T0) to follow-up (T1):

- Δ MVPA Frequency  
- Δ MVPA during a Usual Week  
- Δ Leisure Exercise  
- Δ Leisure Physical Activity  

---

## Models Used

The following regression models are evaluated:

- Ridge Regression  
- Lasso Regression  
- Elastic Net  
- Random Forest Regression  
- Gradient Boosting Regression  
- Support Vector Regression  
- k-Nearest Neighbors Regression  

Model selection is based on cross-validated \(R^2\) scores on the training set.  
Final performance is evaluated on a held-out test set using:

- \(R^2\),
- Mean Absolute Error (MAE),
- Root Mean Squared Error (RMSE).

---

## Feature Importance

Feature importance is analyzed using Random Forest models to gain insight into which baseline variables contribute most strongly to prediction.

Features are also grouped into conceptual categories:

- Demographic / Anthropometric  
- Baseline Physical Activity  
- Fitness / Motor Competence  
- Psychosocial  
- Contextual / Environmental  

Feature importance results are descriptive and intended for interpretation, not causal inference.

---

## Authors

- **Anna-Lena Klöckner**
- **Jakob Werner**

---


