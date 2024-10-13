import pandas as pd
import plotly.graph_objects as go

# 读取CSV文件 / Read CSV file
df = pd.read_csv('chinese_small_car_sales_rankings_2019_2024.csv')

# 将月份转换为日期类型，然后立即转换为字符串
# Convert month to date type, then immediately convert to string
df['月份'] = pd.to_datetime(df['月份'], format='%Y%m').dt.strftime('%Y年%m月')

# 选择2021年8月之后的数据 / Select data after August 2021
df = df[df['月份'] >= '2021年08月']

# 获取所有车型 / Get all car models
models = df['车型'].unique()

# 计算每个车型的最高单月销量
# Calculate the highest monthly sales for each car model
model_max_sales = df.groupby('车型')['销量'].max().sort_values(ascending=False)

# 创建图表 / Create chart
fig = go.Figure()

# 为每个车型添加一条线，保持原有顺序
# Add a line for each car model, maintaining the original order
for model in models:
    model_data = df[df['车型'] == model]
    fig.add_trace(go.Scatter(
        x=model_data['月份'],
        y=model_data['销量'],
        mode='lines+markers',
        name=model,
        text=[f"{model}<br>{month}<br>销量: {sales:,}<br>排名: {rank}" 
              for month, sales, rank in zip(model_data['月份'], model_data['销量'], model_data['排名'])],
        hoverinfo='text'
    ))

# 更新布局 / Update layout
fig.update_layout(
    font={"size": 12},
    title={"text": "中国小型车TOP车型销量走势 (2021年8月 - 2024年8月)"},
    xaxis={
        "title": {"text": "月份"},
        "tickangle": 45,
        "tickmode": "array",
        "tickvals": ["2021年08月", "2021年11月", "2022年02月", "2022年05月", "2022年08月", "2022年11月", 
                     "2023年02月", "2023年05月", "2023年08月", "2023年11月", "2024年02月", "2024年05月", "2024年08月"]
    },
    yaxis={"title": {"text": "销量"}},
    hovermode="closest",
    legend={
        "title": {"text": "车型"},
        "traceorder": "normal"
    },
    plot_bgcolor="#E5ECF6",  # 设置绘图区背景色 / Set plot area background color
    paper_bgcolor="#F9F9F9",  # 设置整个图表的背景色 / Set overall chart background color
    autosize=True  # 确保图表是响应式的 / Ensure the chart is responsive
)

# 更新x轴和y轴的网格线颜色
# Update grid line colors for x-axis and y-axis
fig.update_xaxes(gridcolor='white')
fig.update_yaxes(gridcolor='white')

# 调整图例顺序，同时保持交互功能
# Adjust legend order while maintaining interactive functionality
legend_order = model_max_sales.index.tolist()
for i, trace in enumerate(fig.data):
    trace.legendrank = legend_order.index(trace.name)

# 保存为HTML文件 / Save as HTML file
config = {'responsive': True}
fig.write_html("small-car-topsales-cn.html", config=config)

# 在浏览器中显示图表 / Display chart in browser
fig.show(config=config)