import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

# Notion API 密钥和数据库 ID
NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
DATABASE_ID = os.environ.get("DATABASE_ID")

# 检查是否成功获取到环境变量
if not NOTION_API_KEY or not DATABASE_ID:
    raise ValueError("未能获取到必要的环境变量 NOTION_API_KEY 或 DATABASE_ID")

# 获取网页内容
url = "https://xl.16888.com/level-2.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 提取月份信息
month_input = soup.find('input', class_='xl-date-input')
if month_input and 'value' in month_input.attrs:
    month_str = month_input['value']
    month_value = int(month_str.replace('-', ''))
else:
    raise ValueError("无法找到月份信息")

# 找到数据表格
table = soup.find('table')

# 提取数据
data = []
for row in table.find_all('tr')[1:]:  # 跳过表头，获取所有数据行
    cols = row.find_all('td')
    if len(cols) >= 5:
        rank = cols[0].text.strip()
        model = cols[1].text.strip()
        sales = cols[2].text.strip()
        manufacturer = cols[3].text.strip()
        price = cols[4].text.strip()
        data.append([month_value, rank, model, sales, manufacturer, price])

# 创建 DataFrame
df = pd.DataFrame(data, columns=['月份', '排名', '车型', '销量', '厂商', '售价'])

# 定义写入 Notion 数据库的函数
def write_to_notion_database(df):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    for _, row in df.iterrows():
        data = {
            "parent": {"database_id": DATABASE_ID},
            "properties": {
                "月份": {"number": row['月份']},
                "排名": {"number": int(row['排名'])},
                "车型": {"title": [{"text": {"content": row['车型']}}]},
                "销量": {"number": int(row['销量'].replace(',', ''))},
                "厂商": {"select": {"name": row['厂商']}},
                "售价": {"select": {"name": row['售价']}}
            }
        }
        
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            print(f"Error adding row {row['排名']}: {response.text}")
        else:
            print(f"Successfully added row {row['排名']}")

# 调用函数将数据写入Notion数据库
write_to_notion_database(df)
