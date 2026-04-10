# emby-dedupe-app

一个自己实现的 Emby 媒体查重 Docker 服务。

当前版本功能：
- 使用 Emby API Key 连接 Emby
- 读取电影库条目
- 按“片名 + 年份”分组查找疑似重复电影
- Web 页面查看结果
- 提供 `/api/duplicates` JSON 接口
- 默认只查不删

## 项目结构

```text
emby-dedupe-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── .dockerignore
├── README.md
└── templates/
    └── index.html
