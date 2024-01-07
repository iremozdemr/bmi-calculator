# BMI Calculator using Streamlit

This is a simple Body Mass Index (BMI) calculator built with Streamlit, allowing users to input their height, weight, gender, and age to determine their BMI status.

## Features

- **Input Options:**
  - Gender: Choose between male and female.
  - Age: Select your age using a slider within the range of 18 to 65.
  - Height: Enter your height in meters.
  - Weight: Input your weight in kilograms.

- **BMI Calculation:**
  - Based on the provided inputs, the application calculates the BMI using the formula: `weight / (height * height)`.
  - Determines BMI status as underweight, normal weight, overweight, or obesity according to standard BMI categories.

- **Result Display:**
  - Upon clicking the 'Calculate' button, the application displays the BMI status.
  - If the BMI indicates normal weight, it shows a success message; otherwise, it indicates an error.

## Usage

To run the application:

1. Make sure you have Streamlit installed. If not, install it using:
    ```
    pip install streamlit
    ```

2. Clone the repository:
    ```
    git clone https://github.com/your-username/bmi-calculator.git
    ```

3. Navigate to the project directory:
    ```
    cd bmi-calculator
    ```

4. Run the Streamlit app:
    ```
    streamlit run bmi_calculator.py
    ```

## Contributing

Contributions are welcome! Here's how you can contribute:
- Fork the repository.
- Create a new branch (`git checkout -b feature/new-feature`).
- Make modifications and commit changes (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature/new-feature`).
- Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
