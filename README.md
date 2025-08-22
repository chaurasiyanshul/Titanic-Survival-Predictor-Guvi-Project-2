# Titanic-Survival-Predictor-Guvi-Project-2
# Titanic Survival Predictor Dashboard

This project is an interactive web dashboard built with [Streamlit](https://streamlit.io/) that predicts the survival of a Titanic passenger based on user-input features. The model is trained on Titanic dataset features and uses a pre-trained machine learning model (`titanic3.pkl`) to make predictions.

## Features

- User-friendly interface to input passenger details:
  - Passenger class (1st, 2nd, 3rd)
  - Sex (male/female)
  - Age
  - Fare (ticket price)
- Real-time prediction of survival outcome
- Visual feedback on prediction (success/error message)

## How to Run the Project

1. **Clone or Download the Repository**

   Download the project files to your local machine.

2. **Install Dependencies**

   Make sure you have Python 3.9+ installed. Install required packages using pip:

   ```sh
   pip install streamlit numpy
   ```

3. **Ensure Model File is Present**

   Make sure the `titanic3.pkl` file (the trained model) is in the same directory as `dashboard.py`.

4. **Run the Streamlit App**

   In your terminal, navigate to the project directory and run:

   ```sh
   streamlit run dashboard.py
   ```

5. **Access the Dashboard**

   After running the above command, a new tab will open in your browser at `http://localhost:8501/` where you can use the dashboard.

## Project Structure

```
dashboard.py
titanic3.pkl
```

- `dashboard.py`: Main Streamlit app file.
- `titanic2.pkl`: Pre-trained machine learning model.

## License

This project is for educational purposes.

---

For any questions or issues, please open an issue
