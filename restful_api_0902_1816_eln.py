# 代码生成时间: 2025-09-02 18:16:22
import requests
from flask import Flask, jsonify, request, abort

# 创建Flask应用
app = Flask(__name__)

# 定义一个简单的数据存储
users = [
    {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
    {'id': 2, 'name': 'Jane Doe', 'email': 'jane@example.com'}
]

# 获取所有用户信息
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users}), 200

# 获取单个用户信息
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is not None:
        return jsonify(user), 200
    else:
        abort(404, description='User not found')

# 创建新用户
@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    user = {
        'id': users[-1]['id'] + 1,
        'name': request.json['name'],
        'email': request.json.get('email', '')
    }
    users.append(user)
    return jsonify(user), 201

# 更新用户信息
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404, description='User not found')
    if not request.json:
        abort(400)
    user['name'] = request.json.get('name', user['name'])
    user['email'] = request.json.get('email', user['email'])
    return jsonify(user), 200

# 删除用户
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404, description='User not found')
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'result': True}), 200

# 运行应用
if __name__ == '__main__':
    app.run(debug=True)
