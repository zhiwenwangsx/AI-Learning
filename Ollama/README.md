# Ollama 聊天 Web 应用

这是一个使用 FastAPI 构建的 Web 应用，用于与本地部署的 Ollama 模型进行聊天交互。

## 功能特点

- 与本地部署的 Ollama 模型进行聊天
- 支持选择不同的 Ollama 模型
- 实时显示连接状态
- 美观的聊天界面

## 系统要求

- Python 3.7+
- 已安装并运行的 Ollama（默认在 http://localhost:11434）

## 安装步骤

1. 克隆或下载此仓库

2. 创建并激活虚拟环境（可选但推荐）

```bash
python -m venv venv
source venv/bin/activate  # 在 Windows 上使用 venv\Scripts\activate
```

3. 安装依赖

```bash
pip install -r requirements.txt
```

4. 启动 Ollama 服务（如果尚未运行）

```bash
ollama serve
```

5. 下载并运行模型（如果尚未下载）

```bash
ollama pull llama3
```

6. 启动 Web 应用

```bash
python main.py
```

7. 在浏览器中访问 http://localhost:8000

## 使用说明

1. 在下拉菜单中选择要使用的 Ollama 模型
2. 在文本框中输入您的问题或消息
3. 点击"发送"按钮或按 Enter 键发送消息
4. 等待模型生成回复

## API 端点

- `GET /` - 主页面
- `POST /chat` - 发送消息并获取回复
- `GET /models` - 获取可用模型列表

## 自定义

- 修改 `main.py` 中的 `OLLAMA_API_URL` 变量以连接到不同地址的 Ollama 服务
- 编辑 `static/css/styles.css` 文件自定义界面样式

## 技术栈

- FastAPI - Web 框架
- Jinja2 - 模板引擎
- Ollama API - 大语言模型服务
- HTML/CSS/JavaScript - 前端界面

## 问题排查

- 如果状态指示为"未连接"，请确保 Ollama 服务正在运行
- 如果没有显示模型，请确保您已下载至少一个 Ollama 模型 