# ModelLab

**ModelLab** is a Streamlit app designed to let you experiment with classical machine learning models directly in your browser. Whether you're new to machine learning or an experienced practitioner, this tool helps you explore how different models work, visualize their decision boundaries, and fine-tune hyperparameters—all in one intuitive interface.


---

## **What Can You Do?**
- **Pick a Dataset**: Choose from pre-defined datasets and configure the number of samples and noise levels.
- **Select a Model**: Experiment with popular algorithms like Logistic Regression, Decision Trees, Random Forests, Neural Networks, and more.
- **Visualize Results**: See decision boundaries, performance metrics (Accuracy, F1 Score), training time, and even a Python script to reproduce the model.
- **Feature Engineering**: Add polynomial features to improve model performance on non-linear problems.

---

## **Why Use ModelLab?**
- **Learn by Doing**: Understand how different models behave by tweaking hyperparameters and observing the results.
- **Fast Feedback**: Get instant visual feedback on decision boundaries and performance metrics.
- **Reproducibility**: Generate Python scripts to replicate experiments outside the app.
- **Experiment Freely**: Test models on noisy data, try feature engineering, and compare training speeds.

---

## **Key Features**
- **Interactive Interface**: A clean and intuitive UI for selecting datasets, models, and hyperparameters.
- **Educational Insights**: Learn about decision boundaries, model robustness, and feature engineering.
- **Customizable Datasets**: Adjust noise levels and sample sizes to simulate real-world scenarios.
- **Wide Range of Models**: From simple Logistic Regression to complex Neural Networks, explore them all.

---

## **How to Run Locally**
1. Clone the repository:
   ```bash
   git clone https://github.com/ehtisham-sadiq/modellab.git
   ```
2. Install dependencies using `pipenv`:
   ```bash
   pip install pipenv
   pipenv install
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## **Code Structure**
- `app.py`: The main script to launch the app.
- `utils/`:
  - `ui.py`: Functions for rendering the user interface.
  - `functions.py`: Data processing, model training, and visualization logic.
- `models/`: Definitions for each model's hyperparameter selector.

---

## **Contributions Welcome!**
We’d love your help to make **ModelLab** even better! Here are some ideas:
- Add new datasets (e.g., non-linear patterns).
- Support additional machine learning models.
- Implement advanced feature engineering techniques.
- Visualize feature importance and other metrics.

Feel free to open an issue or submit a pull request if you have ideas or find bugs!

---

## **Inspiration**
This project was inspired by TensorFlow Playground but focuses on classical machine learning models. It’s designed to be a hands-on tool for learning and experimentation.

---

## **License**
This project is licensed under the MIT License. Feel free to use, modify, and share it as you wish!
