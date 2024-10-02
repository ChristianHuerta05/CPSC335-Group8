from flask import Flask, render_template, request
from run import run

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_algorithms():
    selected_algorithms = {
        "Merge_Sort": 'merge' in request.form,
        "Bubble_Sort": 'bubble' in request.form,
        "Quick_Sort": 'quick' in request.form,
        "Radix_Sort": 'radix' in request.form
    }
    times = run(selected_algorithms)
    return render_template('index.html', times=times)


if __name__ == '__main__':
    app.run(debug=False)