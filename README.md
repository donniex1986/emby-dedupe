# emby-dedupe-app

一个自己实现的 Emby 媒体查重 Docker 服务。

它会通过 Emby API 读取电影库数据，按 **片名 + 年份** 分组，找出疑似重复的电影条目，并以网页和 JSON 接口的方式展示结果。

> 当前版本默认 **只查不删**，不会自动删除任何媒体文件。

---

## 功能特性

- 使用 Emby API Key 连接 Emby
- 读取电影库条目
- 按 **片名 + 年份** 进行疑似重复分组
- 提供 Web 页面查看结果
- 提供 `/api/duplicates` JSON 接口
- 默认只读，不执行删除操作
- 使用 Docker / Docker Compose 快速部署

---

## 项目截图说明

当前版本页面会显示：

- 总电影数
- 重复组数
- 每组重复项目的 Emby ID
- 每个项目的物理路径
- 每个项目的 ProviderIds 信息

后续你可以继续扩展为：

- 按 IMDb / TMDb ID 分组
- 排除 4K / Remux / Director's Cut
- 导出 CSV
- 定时扫描
- 邮件或消息通知
- 隔离目录移动，而不是直接删除

---

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
