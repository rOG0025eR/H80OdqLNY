# 代码生成时间: 2025-09-10 11:31:30
import requests
from flask import Flask, jsonify, request, abort

# 创建 Flask 应用
app = Flask(__name__)

# 定义一个简单的数据存储
data = {
    "1": {"name": "John", "age": 20},
    "2": {"name": "Jane", "age": 22}
}


# 定义一个获取所有用户的路由
@app.route('/users', methods=['GET'])
def get_users():
    """
    Get a JSON representation of all users.
    """
    return jsonify(data)


# 定义一个获取单个用户的路由
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a JSON representation of a single user.
    """
    if user_id not in data:
        abort(404)  # 如果用户不存在，返回404错误
    return jsonify(data[user_id])


# 定义一个创建新用户的路由
@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.
    """
    if not request.json or not 'name' in request.json:
        abort(400)  # 如果请求数据不完整，返回400错误
    user = {
        'id': len(data) + 1,
        'name': request.json['name'],
        'age': request.json.get('age', 0)  # 可选参数，如果没有提供，默认为0
    }
data[user['id']] = user
    return jsonify(user), 201


# 定义一个更新用户的路由
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user.
    """
    if user_id not in data:
        abort(404)  # 如果用户不存在，返回404错误
    if not request.json:
        abort(400)  # 如果请求数据不完整，返回400错误
    user = data[user_id]
    user['name'] = request.json.get('name', user['name'])
    user['age'] = request.json.get('age', user['age'])
    return jsonify(user)


# 定义一个删除用户的路由
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user.
    """
    if user_id not in data:
        abort(404)  # 如果用户不存在，返回404错误
    del data[user_id]
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)