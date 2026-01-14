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
    if not os.path.exists(file_path):
        return "| Project Name | Description | Key Tech | Link |\n| :--- | :--- | :--- | :--- |\n| - | Coming Soon | - | - |"
    
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.readlines()
            if len(content) <= 1: # 只有表头或为空
                return "No projects listed yet."
            
            # 生成 Markdown 表格头
            lines.append("| Project Name | Description | Key Tech | Link |")
            lines.append("| :--- | :--- | :--- | :--- |")
            
            # 跳过第一行表头，处理数据行
            for line in content[1:]:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    name, desc, tech, link = parts[0], parts[1], parts[2], parts[3]
                    link_md = f"[Repo]({link})" if link.startswith('http') else "-"
                    lines.append(f"| {name} | {desc} | {tech} | {link_md} |")
        return "\n".join(lines)
    except Exception as e:
        return f"Error loading CSV: {e}"

# 后面的 README 模版保持不变... (请接上文的模版代码)
