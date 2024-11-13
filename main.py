from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def root():
    return "Página principal de prueba"

@app.route("/users/<user_id>")
def get_user(user_id):
    user =  {'id': user_id, 'name':'test', 'telefono':"111-222-333"}
    query = request.args.get('query')
    if query:
        user['query'] = query
    return jsonify(user), 200

if __name__=="__main__":
    app.run(debug=True)