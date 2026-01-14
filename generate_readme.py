import pandas as pd
import os

def generate_table(csv_path):
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        # 确保链接列显示为 Markdown 链接
        df['Link'] = df['Link'].apply(lambda x: f"[Repo]({x})" if str(x).startswith('http') else "-")
        return df.to_markdown(index=False)
    return "Coming soon..."

# 定义赛区及其对应的 CSV 文件
regions = {
    "🇺🇸 USA": "data/usa.csv",
    "🇬🇧 UK": "data/uk.csv",
    "🇻🇳 Vietnam": "data/vietnam.csv",
    "🇷🇺 Russia": "data/russia.csv",
    "🇰🇷 South Korea": "data/south_korea.csv"
}

# 组装 Showcase 部分
showcase_content = ""
for name, path in regions.items():
    showcase_content += f"### {name}\n\n{generate_table(path)}\n\n"

# 读取 README 模版并替换 (假设你在 README 中留下了 这样的占位符)
# 或者直接在这里定义完整的 README 模版
full_readme = f"""# 📝 SpoonCommunity: Global AI Agent Ecosystem

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![SpoonOS](https://img.shields.io/badge/Powered%20by-SpoonOS-orange)](https://github.com/XSpoonAi)

... (此处省略之前的 README 固定部分) ...

## 🤖 Global Hackathon Project Showcase

{showcase_content}

... (此处省略 Education 等固定部分) ...
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(full_readme)
