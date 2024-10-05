from flask import Flask, render_template, request

app = Flask(__name__)


def convert_feet(feet, unit):
    conversions = {'inches': 12, 'yards': 1 / 3, 'miles': 1 / 5280}
    print(f"[DEBUG] Converting {feet} feet to {unit}.")
    result = conversions.get(unit)

    if result is None:
        print(f"[DEBUG] Invalid unit '{unit}' provided.")
        return None

    conversion_result = feet * result
    print(f"[DEBUG] Conversion result: {conversion_result} {unit}.")
    return conversion_result


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        feet_input = request.form['feet']
        unit = request.form['unit']

        print(f"[DEBUG] Received form data: {feet_input} feet, {unit}.")
        try:
            feet = float(feet_input)
            result = convert_feet(feet, unit)
            if result is None:
                print(f"[DEBUG] Conversion failed due to invalid unit.")
            else:
                print(f"[DEBUG] Conversion successful, result: {result}.")
        except ValueError:
            print(f"[DEBUG] Invalid input for feet: '{feet_input}' (not a float).")
            result = "Invalid input for feet."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    print("[DEBUG] Starting Flask app...")
    app.run(debug=True)

