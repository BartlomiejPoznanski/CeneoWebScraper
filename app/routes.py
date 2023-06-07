from app import app
from flask import render_template

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/extraction')
def extraction():
    return render_template("extraction.html")

@app.route('/products_list')
def products_list():
    return render_template("product_list.html")

@app.route('/product_site')
def product_site():
    return render_template("product_site.html")

@app.route('/charts')
def charts():
    return render_template("charts.html")