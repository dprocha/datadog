from flask import Flask, request, jsonify

app = Flask(__name__)
food_items = {}

@app.route('/food', methods=['POST'])
def add_food():
    data = request.json
    food_items[data['name']] = {'price': data['price'], 'description': data['description']}
    return jsonify({'message': 'Food item added'}), 201

@app.route('/food', methods=['GET'])
def get_food_items():
    return jsonify(food_items)

@app.route('/food/<name>', methods=['PUT'])
def update_food_price(name):
    if name in food_items:
        data = request.json
        food_items[name]['price'] = data['price']
        return jsonify({'message': 'Price updated'}), 200
    return jsonify({'error': 'Food item not found'}), 404

@app.route('/food/<name>', methods=['DELETE'])
def delete_food(name):
    if name in food_items:
        del food_items[name]
        return jsonify({'message': 'Food item deleted'}), 200
    return jsonify({'error': 'Food item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
