📊 Interactive Survey Data Visualization GUI
This project is a Python GUI application that provides interactive visualizations based on Stack Overflow Developer Survey data. It allows users to explore insights from the dataset using various chart types via an easy-to-use interface.

🚀 Features
Cleaned and filtered real-world developer survey data

Interactive Tkinter-based GUI

Dropdown to select from 9 different types of visualizations:

Histogram

Box Plot

Scatter Plot

Donut Chart

Bar Chart

Heatmap

Pie Chart

Horizontal Bar Chart

Line Chart

Enhanced GUI with modern styling and layout

📂 Dataset Used
File: survey_results_public.csv

Source: Stack Overflow Developer Survey

📊 Graph Descriptions
Chart Type	Description
Histogram	Distribution of yearly compensation
Box Plot	Salary by employment type
Scatter Plot	Country vs. Salary (Top 5 countries)
Donut Chart	Remote work distribution
Bar Chart	Average salary based on job satisfaction
Heatmap	Correlation between age and compensation
Pie Chart	Distribution of top 5 education levels
Horizontal Bar	Count of job satisfaction responses
Line Chart	Average salary across age groups
🛠️ Tech Stack
Python 3.x

Pandas for data handling

Matplotlib and Seaborn for data visualization

Tkinter for GUI

📸 Screenshots
You can add screenshots here showing the GUI interface and example plots.

▶️ How to Run
Clone this repo or download the .py file.

Ensure the survey_results_public.csv file is in the same folder.

Run the Python file:

bash
Copy
Edit
python your_filename.py
Select a graph type from the dropdown and click Generate Graph.

📌 Requirements
Make sure the following libraries are installed:

bash
Copy
Edit
pip install pandas matplotlib seaborn
✨ Future Enhancements
Add export option for generated plots

Filter by region, role, or experience

Add theme toggle (dark/light)

Responsive GUI improvements
