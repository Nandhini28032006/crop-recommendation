# 🌱 Smart Crop Recommendation & Waste-to-Wealth System

A smart agriculture web application that recommends suitable crops based on soil and environmental conditions and provides **waste-to-wealth ideas** related to the recommended crop.

The project combines **crop recommendation, input validation, prediction history, circular waste-to-wealth visualization, and automated browser testing** into a single web application.

---

## 📌 Project Overview

Agriculture depends heavily on soil nutrients and environmental conditions. Choosing an appropriate crop for a particular combination of soil and weather parameters can help farmers make better cultivation decisions.

The **Smart Crop Recommendation & Waste-to-Wealth System** provides a simple web-based interface where users enter agricultural parameters and receive a suitable crop recommendation.

The application accepts the following inputs:

* 🌱 Nitrogen (N)
* 🌱 Phosphorus (P)
* 🌱 Potassium (K)
* 🌡️ Temperature
* 💧 Humidity
* 🧪 Soil pH
* 🌧️ Rainfall

After processing the inputs, the application displays:

1. Recommended crop
2. Prediction history
3. Related waste-to-wealth opportunities
4. Circular visualization of agricultural waste utilization

---

## 🎯 Objectives

The main objectives of this project are:

* Provide a simple interface for crop recommendation.
* Use agricultural and environmental parameters to generate recommendations.
* Validate user input before processing predictions.
* Prevent negative and invalid values.
* Maintain a history of successful predictions.
* Connect crop recommendations with waste-to-wealth opportunities.
* Demonstrate automated web application testing.
* Provide a practical example of an AI-assisted software development workflow.

---

## 🚀 Key Features

### 🌾 1. Crop Recommendation

The system processes the supplied agricultural parameters and recommends a suitable crop.

Example recommendations include:

* Rice
* Wheat
* Sugarcane
* Maize

The recommendation is generated based on the application's prediction logic/model.

---

### ✅ 2. Input Validation

The application validates user input before generating a prediction.

Validation includes:

* Required-field validation
* Numeric-value validation
* Non-negative-value validation
* Prevention of invalid submissions

If invalid information is entered, the application displays an:

```text
Invalid Input
```

message instead of generating a crop recommendation.

This prevents incorrect data from being processed by the application.

---

### 📜 3. Prediction History

Every successful prediction can be added to a prediction history list.

Example:

```text
Prediction History

1. Rice
2. Sugarcane
3. Maize
```

This allows users to view previously generated recommendations during their session.

---

### 🔄 4. Reset Functionality

The application provides a reset option that clears the entered values and restores the interface to its initial state.

The reset functionality helps users quickly perform a new prediction without manually clearing every field.

---

### ♻️ 5. Waste-to-Wealth Recommendations

The project extends beyond simple crop prediction by connecting the recommended crop with possible agricultural waste utilization.

Examples of waste-to-wealth opportunities include:

* Composting
* Animal feed
* Biofertilizer
* Biogas
* Biomass-based products
* Other value-added agricultural applications

This feature demonstrates the idea of converting agricultural waste into useful resources instead of treating it only as waste.

---

### 📊 6. Circular Waste-to-Wealth Visualization

The application presents waste-to-wealth information using a circular visualization.

The visualization helps users understand the relationship between:

```text
Crop
  ↓
Agricultural Waste
  ↓
Processing / Reuse
  ↓
Useful Product
  ↓
Economic / Environmental Value
```

This provides an easy-to-understand representation of the circular economy concept.

---

### 🧪 7. Automated Testing

The application includes automated browser testing using:

* **pytest**
* **Playwright**

The automated tests verify important application workflows such as:

* Application loading
* Valid input submission
* Crop recommendation
* Invalid input handling
* Negative-value rejection
* Prediction history
* Reset functionality
* Waste-to-wealth display

Automated testing helps ensure that important features continue to work after changes are made to the application.

---

## 🏗️ System Architecture

The application follows a simple web application architecture.

```text
                ┌─────────────────────┐
                │       User          │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Frontend UI       │
                │ HTML / CSS / JS     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      Flask          │
                │ Application Layer   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Input Validation    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Prediction Logic    │
                └──────────┬──────────┘
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
       ┌─────────────────┐   ┌────────────────────┐
       │ Prediction      │   │ Waste-to-Wealth    │
       │ History         │   │ Recommendations    │
       └─────────────────┘   └────────────────────┘
                │                     │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │    Result Display   │
                └─────────────────────┘
```

---

## 🔄 Application Workflow

The complete workflow is:

```text
User enters agricultural parameters
              ↓
       Input validation
              ↓
      Is input valid?
         ↙          ↘
       No            Yes
       ↓              ↓
Invalid Input     Prediction Logic
                      ↓
               Crop Recommendation
                      ↓
              Update Prediction History
                      ↓
             Waste-to-Wealth Mapping
                      ↓
                Display Results
```

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Testing

* pytest
* Playwright

### Development

* Git
* GitHub
* Python Virtual Environment

---

## 📂 Project Structure

A typical project structure is:

```text
Crop-recommendation/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── tests/
│   └── test_*.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

> The exact files and folders may vary depending on the final project implementation.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd Crop-recommendation
```

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

The application will start on the local Flask development server.

Open the displayed local URL in a browser.

For example:

```text
http://127.0.0.1:5000
```

---

## 🧪 Running Automated Tests

Make sure the virtual environment is activated.

Run:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

Playwright tests can be used to verify the application's browser-based workflows.

A successful test run should show the tests passing.

Example:

```text
==================== test session starts ====================

tests/test_*.py ........                                  [100%]

===================== 8 passed ==============================
```

> The exact number of tests may vary depending on the final test suite.

---

## 🔍 Testing Strategy

The project follows an end-to-end testing approach.

### Functional Tests

The automated tests verify:

| Test Area           | Expected Result                     |
| ------------------- | ----------------------------------- |
| Application loading | Page loads successfully             |
| Valid inputs        | Crop recommendation is displayed    |
| Required fields     | Missing values are rejected         |
| Non-numeric input   | Invalid input is handled            |
| Negative values     | Invalid input is displayed          |
| Prediction history  | Successful predictions are recorded |
| Reset               | Form is cleared/reset               |
| Waste-to-wealth     | Related options are displayed       |

---

## 🛡️ Input Validation Examples

### Valid Input

```text
N = 90
P = 42
K = 43
Temperature = 25
Humidity = 80
pH = 6.5
Rainfall = 200
```

The application processes the values and displays a recommendation.

### Invalid Input

```text
N = -10
```

The application rejects the input and displays:

```text
Invalid Input
```

This ensures that invalid agricultural parameters are not processed as normal prediction data.

---

## ♻️ Waste-to-Wealth Concept

A key feature of this project is the integration of the **waste-to-wealth** concept.

Instead of considering agricultural residues as unwanted waste, the application presents possible ways to reuse them.

```text
Agricultural Crop
       ↓
   Crop Residue
       ↓
Waste Collection
       ↓
Processing / Conversion
       ↓
Value-Added Product
       ↓
Economic + Environmental Benefits
```

Potential benefits include:

* Reduction of agricultural waste
* Better resource utilization
* Additional income opportunities
* Reduced environmental impact
* Promotion of circular agriculture

---

## 📈 Future Enhancements

The current application can be extended with several advanced features:

### 🤖 Improved Machine Learning

* Train the recommendation system using a larger agricultural dataset.
* Compare multiple ML algorithms.
* Display prediction confidence.
* Improve model accuracy through feature engineering.

### 🌦️ Real-Time Weather Integration

Weather APIs could be integrated to automatically obtain:

* Temperature
* Humidity
* Rainfall
* Weather forecasts

### 🗺️ Location-Based Recommendations

The application could use the user's location and regional agricultural data to provide more localized recommendations.

### 📊 Farmer Dashboard

A dashboard could provide:

* Previous predictions
* Crop statistics
* Soil information
* Waste-to-wealth opportunities
* Recommendation trends

### 💰 Economic Estimation

The system could estimate:

* Expected crop value
* Waste quantity
* Potential waste-to-wealth revenue
* Production costs

### 🌐 Deployment

The application can be deployed to a cloud platform so that users can access it through the internet.

---

## 🔐 Validation & Reliability

The project focuses on reliable user interaction by validating inputs before prediction.

The application follows the principle:

```text
Input
  ↓
Validate
  ↓
Process
  ↓
Predict
  ↓
Display
```

This reduces the possibility of invalid user input affecting the prediction workflow.

---

## 💡 Project Highlights

### What makes this project different?

This project does not stop at crop recommendation.

It combines:

```text
Crop Recommendation
        +
Input Validation
        +
Prediction History
        +
Waste-to-Wealth
        +
Circular Visualization
        +
Automated Testing
```

This creates a more complete agriculture-focused web application rather than a standalone prediction page.

---

## 📸 Screenshots

Add screenshots of the application here.

### Home Page

```text
Add your screenshot here
```

### Crop Recommendation

```text
Add your screenshot here
```

### Invalid Input Validation

```text
Add your screenshot here
```

### Prediction History

```text
Add your screenshot here
```

### Waste-to-Wealth Visualization

```text
Add your screenshot here
```

---

## 🎥 Demo

A short demonstration can show the following workflow:

1. Open the application.
2. Enter valid agricultural parameters.
3. Generate a crop recommendation.
4. Show the prediction history.
5. Demonstrate waste-to-wealth options.
6. Enter an invalid/negative value.
7. Show the validation message.
8. Use the reset functionality.
9. Run the automated tests using pytest.

---

## 🧑‍💻 Development Approach

The project was developed using an iterative workflow:

```text
Existing Application
        ↓
Feature Identification
        ↓
Implementation
        ↓
Automated Testing
        ↓
Bug Detection
        ↓
Fixes / Improvements
        ↓
Regression Testing
        ↓
Final Documentation
```

Automated testing with Playwright and pytest helps verify that changes do not break existing functionality.

---

## 📋 Requirements

The project requires:

* Python 3.x
* Flask
* pytest
* Playwright
* A modern web browser
* Git

Python dependencies are listed in:

```text
requirements.txt
```

---

## 📄 License

This project is intended for educational and demonstration purposes.

---

## 👨‍💻 Author

**Smart Crop Recommendation & Waste-to-Wealth System**

Built as a practical web application demonstrating:

* Web development
* Application logic
* Input validation
* Automated testing
* Agricultural technology
* Circular economy concepts

---

## ⭐ Conclusion

The **Smart Crop Recommendation & Waste-to-Wealth System** demonstrates how a simple agricultural prediction application can be expanded into a more complete solution by combining crop recommendation with validation, history tracking, waste utilization, visualization, and automated testing.

The project provides a foundation that can later be enhanced with real machine-learning models, real-time weather data, location-based recommendations, economic analysis, and cloud deployment.
