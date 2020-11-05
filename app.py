from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>\nHello World..'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius=""):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    fahrenheit_shortened = f"{fahrenheit:.2f}"
    # return fahrenheit
    return f"Result: {fahrenheit_shortened} F"


# celsius = float(input("Celsius: "))
# fahrenheit = celsius * 9.0 / 5 + 32
# print("Result: {:.2f} F".format(fahrenheit))

if __name__ == '__main__':
    app.run()
