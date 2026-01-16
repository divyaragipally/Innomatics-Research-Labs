from flask import Flask, request

app = Flask(__name__)

@app.route('/upper')
def upper_name():
    name = request.args.get('name')
    if not name:
        return "Please provide a name using ?name=yourname"

    return f"<h1>{name.upper()}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
