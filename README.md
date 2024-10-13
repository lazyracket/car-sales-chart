# Chinese Small Car Sales Trend Visualization

This repository contains an interactive visualization of top-selling small car sales trends in China from August 2021 to August 2024.

## Quick View
中国小型车TOP车型销量走势 (2021年8月 - 2024年8月)

You can view the interactive chart directly [here](https://lazyracket.github.io/car-sales-chart/small-car-topsales-cn.html).

## Repository Contents
- `small-car-topsales-cn.html`: The interactive visualization
- `generate_chinese_small_car_sales_chart.py`: Python script to generate the chart
- `chinese_small_car_sales_rankings_2019_2024.csv`: Raw data file

## About the Project
This visualization provides insights into the sales performance of various small car models in the Chinese market. It features an interactive line chart that allows users to explore monthly sales data and compare different car models.

## How to Use
1. To view the chart: Open `small-car-topsales-cn.html` in a web browser.
2. To regenerate the chart:
   - Ensure the CSV file `chinese_small_car_sales_rankings_2019_2024.csv` is in the same directory as the Python script.
   - Run `python generate_chinese_small_car_sales_chart.py`

Note: You'll need Python installed with pandas and plotly libraries.

## Data Source
The car sales data used in this project is sourced from "车主之家" (www.16888.com) auto sales rankings. It provides comprehensive automobile sales data, including brand sales, manufacturer sales, and sales by vehicle category. Please note that this data does not include imported car models and is for reference only. For official sales figures, please refer to the data published by automobile manufacturers.

Data source: [Auto Sales Rankings - 车主之家](https://xl.16888.com/)

## Future Improvements
- Expand the dataset to include other vehicle categories such as SUVs, sedans, etc.
- Implement more interactive analysis features, allowing users to compare across different vehicle types and time periods.
- Add functionality for users to customize the chart based on specific brands or price ranges.
- Integrate real-time data updates to keep the visualization current with the latest market trends.

For any questions or suggestions regarding this project, please open an issue in this repository.
