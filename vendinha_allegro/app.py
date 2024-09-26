from flask import render_template, request, redirect, url_for

from __init__ import create_app
from models import db, Sale

app = create_app()


@app.route('/')
def index():
    sales = Sale.query.all()
    return (render_template('index.html', sales=sales)

            @ app.route('/register_sale', methods=['GET', 'POST']))


def register_sale():
    if request.method == 'POST':
        item = request.form['item']
        quantity = request.form['quantity']
        price = request.form['price']

        new_sale = Sale(item=item, quantity=quantity, price=price)
        db.session.add(new_sale)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('register_sale.html')


if __name__ == '__main__':
    app.run(debug=True)
