# Earths-Rising-Temperature
Interactive dashboard where users can filter by year and month to see how temperature has changed overtime in different countries.

## Project 1: Global Temperature Trends (1950-2025)
<h3><b>Overview:</b></h3>
An interactive Tableau dashboard visualizing global temperature shifts. This project focuses on the intersection of data engineering and climate storytelling.

<h3>The Problem (Data Transformation):</h3> The raw climate data was provided in a Panel (Wide) format, with monthly averages spread across 12 separate columns. This structure made it impossible to create a dynamic "Month Selection" tool in Tableau.

<h3>The Solution (Python/Pandas):</h3> I developed a Python script to transform the data into a Long format. By using the .melt() function, I consolidated the monthly columns into a single Month dimension and a single Temperature measure. 
This allowed for:
<ol>
<li>Dynamic filtering by month and year.</li>
<li>Cleaner Level of Detail (LOD) expressions in Tableau.</li>
<li>A more responsive user interface.</li>
</ol>
<hr>
Key Features:

Interactive Map: Color-coded by temperature with country-level granularity.

Custom Navigation: Month-selection buttons built using a secondary data source and Parameter Actions.
<hr>
Technologies Used:

Python (Pandas): Data cleaning and reshaping.

Tableau: Geospatial visualization and dashboarding.
