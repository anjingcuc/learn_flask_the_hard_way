# InstaCUC

实现一个图片站点。

运行方式：

```bash
# 初始化数据库
flask db init

# 生成迁移文件
flask db migrate

# 迁移数据库，即创建database以及各个表
flask db upgrade

# 创建管理员账号
flask user create-admin <username@email.com> <username> <password>

# 运行站点
flask run
```
