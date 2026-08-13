# 🌱 Smart Crop Recommendation & Waste-to-Wealth System

## 1. Project Overview

The Smart Crop Recommendation System is a small web application that recommends a suitable crop based on soil and environmental inputs.

The application accepts:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

After the user submits the values, the application recommends a crop and displays related waste-to-wealth options.

The application also provides:

- Input validation
- Negative-value rejection
- Prediction history
- Reset functionality
- Circular waste-to-wealth visualization
- Automated browser testing using Playwright and pytest

---

## 2. Main Features

### Crop Recommendation

The application processes the supplied agricultural parameters and recommends a crop such as:

- Rice
- Wheat
- Sugarcane
- Maize

### Input Validation

The application prevents invalid submissions.

It validates:

- Required fields
- Numeric values
- Non-negative values

Invalid input displays an `Invalid Input` message instead of producing a crop recommendation.

### Prediction History

Successful predictions are added to a prediction history list.

For example:

```text
1. Rice
2. Sugarcane
3. Maize