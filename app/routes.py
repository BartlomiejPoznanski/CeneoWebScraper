from app import app
from flask import render_template, request, url_for

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/extraction', methods=["POST",'GET'])
def extraction():
    if request.method=="POST":
        product_code=request.form.get("product_code")
        return redirect(url_for("product",product_code=product_code))
    return render_template("extraction.html")

@app.route('/products_list/<product_code>')
def products_list(product_code):
    return render_template("product_list.html", product_code=product_code)

@app.route('/product_site')
def product_site():
    return render_template("product_site.html")

@app.route('/charts')
def charts():
    return render_template("charts.html")