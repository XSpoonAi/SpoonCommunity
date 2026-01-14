import pandas as pd
import os

# 配置赛区和对应的文件
REGIONS = {
    "🇺🇸 USA": "data/usa.csv",
    "🇬🇧 UK": "data/uk.csv",
    "🇻🇳 Vietnam": "data/vietnam.csv",
    "🇷🇺 Russia": "data/russia.csv",
    "🇰🇷 South Korea": "data/south_korea.csv"
}

def load_csv_to_md(file_path):
    if os.path.exists(file_path):
        try:
            # 自动识别编码并读取
            df = pd.read_csv(file_path, encoding='utf-8')
            
            # 清理列名（去掉可能存在的 Tab 或空格）
            df.columns = [c.strip() for c in df.columns]
            
            # 如果是空的
            if df.empty:
                return "No projects listed yet."
            
            # 处理 Link 列，转为 Markdown 点击链接
            if 'Link' in df.columns:
                df['Link'] = df['Link'].apply(lambda x: f"[Repo]({x})" if str(x).startswith('http') else "-")
            
            # 转换为 Markdown 表格 (不显示索引)
            return df.to_markdown(index=False)
        except Exception as e:
            return f"*Error parsing {file_path}: {e}*"
    return "*Coming soon...*"

# 生成内容
showcase_sections = ""
for region, path in REGIONS.items():
    showcase_sections += f"### {region}\n\n{load_csv_to_md(path)}\n\n"

# 完整的 README 模版
README_TEMPLATE = f"""# 📝 SpoonCommunity: Global AI Agent Ecosystem

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![SpoonOS](https://img.shields.io/badge/Powered%20by-SpoonOS-orange)](https://github.com/XSpoonAi)
[![Global Reach](https://img.shields.io/badge/Global%20Regions-5-blue)](#-global-impact)

Welcome to **SpoonCommunity**! This repository is a curated collection of innovative AI Agent projects developed during the **Spoon Global Hackathon Series**.

---

## 🌍 Global Impact
`🇺🇸 USA` | `🇬🇧 UK` | `🇻🇳 Vietnam` | `🇷🇺 Russia` | `🇰🇷 South Korea`

---

## 🤖 Global Hackathon Project Showcase

{showcase_sections}

---

## 📚 Community & Education
| Resource | Description | Link |
| :--- | :--- | :--- |
| 🧑‍💻 **Co-learning** | Join our community-led sessions. | [Explore ↗️](https://xspoonai.github.io/spoon-colearning/) |
| 🎬 **Workshop** | Watch video tutorials on YouTube. | [Watch ↗️](https://www.youtube.com/playlist?list=PLyHm819ed_KA36Ae2Ug1iUeiA8_N0obcB) |
| 📖 **Cookbook** | Explore practical recipes for SpoonOS. | [Read ↗️](https://xspoonai.github.io/) |

---

## 🚀 How to Contribute
1. **Fork** this repository.
2. Update the corresponding CSV in the `data/` folder.
3. **Submit a Pull Request**.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(README_TEMPLATE)

print("Success: README.md updated.")
