# E-Commerce Analytics Dashboard

Overview

This repository contains an interactive E-Commerce Analytics Dashboard built with Streamlit, Pandas, and Plotly. 
The dashboard allows users to visualize and analyze e-commerce sales data across various metrics such as total sales, total profit, most sold products, and more.

## Features

- **Interactive Visualizations**: Multiple types of charts and graphs, including bar charts, line charts, scatter plots, and donut charts.
- **Customizable Dashboard**: Users can select different metrics to visualize from the sidebar.
- **Downloadable Data**: Users can download the data used in each visualization as a CSV file.
- **Responsive Design**: The dashboard is designed to work across different screen sizes.
- **Real-Time Updates**: Displays the current date and time in the sidebar, indicating the last time the dashboard was updated.

## Technology Stack

- **Python**: Programming language used for data manipulation and backend.
- **Streamlit**: Framework used to create the interactive web application.
- **Pandas**: Library used for data manipulation and analysis.
- **Plotly**: Library used to create interactive visualizations.
- **Pillow**: Library used to handle image processing.

## How to Run the Project

1. **Clone the repository**:

    ```bash
    git clone https://github.com/DataWizardryy/E-Commerce_Dashboard.git
    cd ecommerce-analytics-dashboard
    ```

2. **Install the required dependencies**:

    You can install the required Python libraries using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Add your dataset**:

    Place your dataset (e.g., `Sample_DataSet_Assessment.csv`) in the project directory.

4. **Run the Streamlit app**:

    Use the following command to start the Streamlit server:

    ```bash
    streamlit run app.py
    ```

5. **Access the dashboard**:

    Once the server is running, you can access the dashboard by navigating to `http://localhost:8501` in your web browser.

## Project Structure

- `app.py`: Main application file containing the Streamlit code.
- `Sample_DataSet_Assessment.csv`: Sample dataset used in the dashboard.
- `ingryd-academy-logo.jpg`: Image used in the sidebar.
- `README.md`: This file.

## Customization

To customize the dashboard, you can modify the following:

- **CSS Styles**: Custom styles can be adjusted in the `st.markdown()` block containing the CSS code.
- **Visualizations**: You can add, remove, or modify the visualizations by editing the relevant sections of `app.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Streamlit](https://www.streamlit.io/) for providing an excellent framework for building data applications.
- Special thanks to INGRYD Academy for inspiring the creation of this dashboard.

---

<p align="center">&copy; 2024 E-Commerce Analytics Dashboard. All rights reserved.</p>
