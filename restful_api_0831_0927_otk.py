# 代码生成时间: 2025-08-31 09:27:18
import requests
from flask import Flask, jsonify, request, abort

# 创建 Flask 应用
app = Flask(__name__)

# 假设我们有一个简单的用户数据存储，使用字典作为示例
users = {"1": {"name": "John"}, "2": {"name": "Jane"}}

# 获取所有用户
@app.route('/users', methods=['GET'])
def get_users():
    # 返回所有用户的 JSON 表示
    return jsonify({'users': list(users.values())})

# 获取单个用户
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # 查找用户，如果不存在，则返回 404 错误
    user = users.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user)

# 创建新用户
@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    user = {
        'id': users[-1]['id'] + 1,
        'name': request.json['name'],
    }
    users[user['id']] = user
    return jsonify(user), 201

# 更新用户信息
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if user is None:
        abort(404)
    if not request.json:
        abort(400)
    user['name'] = request.json.get('name', user['name'])
    return jsonify(user)

# 删除用户
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        abort(404)
    del users[user_id]
    return jsonify({'result': True})

# 错误处理
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

if __name__ == '__main__':
    # 运行 Flask 应用
    app.run(debug=True)
