from flask import Flask, render_template, request, jsonify

from main import load_provinces, load_years, load_by_year, load_all_year

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index2.html')


@app.route("/load")
def do_load():
    year = request.args.get('year', 0, type=str)
    return jsonify({"Code": 0, "Result": load_by_year(year)})


@app.route("/loadall")
def do_load_all():
    return jsonify({"Code": 0, "Result": load_all_year()})


@app.route("/load_province")
def do_load_province():
    return jsonify({"Code": 0, "Result": load_provinces()})


@app.route("/load_year")
def do_load_years():
    return jsonify({"Code": 0, "Result": load_years()})


if __name__ == "__main__":
    app.run()
