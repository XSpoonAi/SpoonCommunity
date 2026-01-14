import os
import csv

# 配置赛区和对应的文件
REGIONS = {
    "🇺🇸 USA": "data/usa.csv",
    "🇬🇧 UK": "data/uk.csv",
    "🇻🇳 Vietnam": "data/vietnam.csv",
    "🇷🇺 Russia": "data/russia.csv",
    "🇰🇷 South Korea": "data/south_korea.csv"
}

def load_csv_to_md(region_name, file_path):
    if not os.path.exists(file_path):
        # 调试信息：如果文件不存在，直接返回提示
        return f"> ⚠️ Data file for {region_name} not found at `{file_path}`. Please ensure the file exists."
    
    rows = []
    try:
        # 使用 utf-8-sig 处理 Excel 可能导出的 BOM 头
        with open(file_path, mode='r', encoding='utf-8-sig') as f:
            # 自动识别分隔符（防止有的是分号，有的是逗号）
            dialect = csv.Sniffer().sniff(f.read(1024))
            f.seek(0)
            reader = csv.DictReader(f, dialect=dialect)
            
            # 清理表头空格
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            for row in reader:
                # 兼容不同大小写的表头
                name = row.get('Project Name', row.get('project name', '-')).strip()
                desc = row.get('Description', row.get('description', '-')).strip()
                tech = row.get('Key Tech', row.get('key tech', '-')).strip()
                link = row.get('Link', row.get('link', '-')).strip()
                
                link_md = f"[Repo]({link})" if link.startswith('http') else "-"
                rows.append(f"| {name} | {desc} | {tech} | {link_md} |")
        
        if not rows:
            return f"> ℹ️ No projects currently listed for {region_name}."
            
        header = "| Project Name | Description | Key Tech | Link |\n| :--- | :--- | :--- | :--- |"
        return header + "\n" + "\n".join(rows)
    except Exception as e:
        return f"> ❌ Error parsing `{file_path}`: {str(e)}"

# 拼接所有赛区
showcase_sections = ""
for name, path in REGIONS.items():
    showcase_sections += f"### {name}\n\n{load_csv_to_md(name, path)}\n\n"

# 完整的 README 内容
README_CONTENT = f"""# 📝 SpoonCommunity: Global AI Agent Ecosystem

[![SpoonOS](https://img.shields.io/badge/Powered%20by-SpoonOS-orange)](https://github.com/XSpoonAi)
[![Global Reach](https://img.shields.io/badge/Global%20Chapters-5-blue)](#-global-impact)

---

## 🌍 Global Impact
`🇺🇸 USA` | `🇬🇧 UK` | `🇻🇳 Vietnam` | `🇷🇺 Russia` | `🇰🇷 South Korea`

---

## 🤖 Global Hackathon Project Showcase

{showcase_sections}

---

## 📚 Community & Education
| Resource | Link |
| :--- | :--- |
| 🧑‍💻 **Co-learning** | [Explore ↗️](https://xspoonai.github.io/spoon-colearning/) |
| 🎬 **Workshop** | [Watch ↗️](https://www.youtube.com/playlist?list=PLyHm819ed_KA36Ae2Ug1iUeiA8_N0obcB) |
| 📖 **Cookbook** | [Read ↗️](https://xspoonai.github.io/) |

---
*Last updated by Spoon-Bot.*
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(README_CONTENT)

print("Process finished.")
