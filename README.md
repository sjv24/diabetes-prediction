# Diabetes Prediction

## Overview

Diabetes is a widespread global health issue that requires early detection for effective management. This project presents a beginner-friendly machine learning model designed to predict the likelihood of diabetes based on key features such as age, BMI, glucose levels, and insulin. The model includes essential preprocessing, evaluation, and achieves an accuracy of 80%. Additionally, an interactive user interface (UI) allows users to input their details and access a built-in calculator to assist with measurements (such as BMI) for those who are unsure.

## Problem Description

**Diabetes**, medically known as **Diabetes Mellitus**, is a chronic condition where the body cannot properly regulate blood glucose (sugar) levels. This results in excessively high glucose levels in the bloodstream, while the kidneys work to eliminate the excess glucose through urine. Diabetes occurs when the body either fails to produce sufficient insulin or does not use it effectively, disrupting glucose regulation.

## Dataset

The dataset used in this project is publicly available and free to use. It includes the following features, which are critical in diagnosing diabetes:

- **Pregnancies**: The number of pregnancies the individual has had. This is especially relevant for predicting gestational diabetes and type 2 diabetes risk later in life.
  
- **Glucose**: The concentration of glucose in the blood after fasting. High glucose levels indicate insulin resistance or diabetes.
  
- **Blood Pressure**: The blood pressure (in mm Hg). High blood pressure increases the risk of type 2 diabetes and its complications.
  
- **Skin Thickness**: The thickness of the skin fold (measured in mm) at the triceps. This is an indicator of body fat, which correlates with increased diabetes risk.
  
- **Insulin**: The level of insulin in the blood. Insulin resistance is a key feature of type 2 diabetes and reflects how well the body processes insulin.
  
- **BMI (Body Mass Index)**: A measure of body fat based on weight and height. A higher BMI is associated with a higher risk of diabetes.
  
- **Diabetes Pedigree Function**: A score indicating the likelihood of diabetes based on family history. A higher score suggests a stronger genetic predisposition.
  
- **Age**: The age of the individual in years. Older age is a known risk factor for type 2 diabetes.
  
- **Outcome**: The target variable where **1** indicates the individual has diabetes and **0** means they do not. This is the value the model predicts.
