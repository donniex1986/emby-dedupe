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

环境变量
	•	 EMBY_URL ：Emby 地址，例如  http://192.168.1.10:8096 
	•	 EMBY_API_KEY ：Emby API Key
	•	 EMBY_USER_ID ：可选，留空时直接使用  /emby/Items 
运行方式
Docker Compose
docker compose up -d --build
启动后访问：
http://你的服务器IP:5055
Emby API Key 获取
在 Emby 管理后台中创建 API Key，然后填入  docker-compose.yml 。
注意
当前查重规则是：
	•	片名相同
	•	年份相同
这只是“疑似重复”判断，不会自动删除文件。 后续可继续增强：
	•	按 IMDb / TMDb ID 分组
	•	排除 4K、Remux、Director’s Cut
	•	导出 CSV
	•	定时扫描
