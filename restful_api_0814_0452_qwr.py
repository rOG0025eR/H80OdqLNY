# 代码生成时间: 2025-08-14 04:52:09
import requests
from flask import Flask, jsonify, request

# 创建 Flask 应用
app = Flask(__name__)

# 定义一个简单的资源，例如用户资源
users = {
    "1": {"name": "John", "age": 30},
    "2": {"name": "Lily", "age": 25},
    "3": {"name": "Mike", "age": 28}
}

# 用户路由 - 列出所有用户
@app.route("/users", methods=["GET"])
def get_users():
    # 错误处理：如果请求方法不是 GET
    if request.method != "GET":
        return jsonify({"error": "Only GET method is allowed"}), 405
    # 返回所有用户信息
    return jsonify(list(users.values()))

# 用户路由 - 添加新用户
@app.route("/users", methods=["POST"])
def create_user():
    # 错误处理：如果请求方法不是 POST
    if request.method != "POST":
        return jsonify({"error": "Only POST method is allowed"}), 405
    # 从请求中获取新用户数据
    new_user = request.json
    user_id = max(users.keys()) + 1
    users[str(user_id)] = new_user
    # 返回新用户信息
    return jsonify(new_user), 201

# 用户路由 - 获取单个用户
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    # 错误处理：如果用户不存在
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    # 返回单个用户信息
    return jsonify(user)

# 用户路由 - 更新用户信息
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    # 错误处理：如果用户不存在或请求方法不是 PUT
    user = users.get(user_id)
    if not user or request.method != "PUT":
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"error": "Only PUT method is allowed"}), 405
    # 更新用户信息
    users[user_id] = request.json
    # 返回更新后的用户信息
    return jsonify(users[user_id])

# 用户路由 - 删除用户
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    # 错误处理：如果用户不存在
    if users.get(user_id) is None:
        return jsonify({"error": "User not found"}), 404
    # 删除用户
    del users[user_id]
    # 返回成功消息
    return jsonify({"message": "User deleted"}), 200

# 启动应用
if __name__ == "__main__":
    app.run(debug=True)