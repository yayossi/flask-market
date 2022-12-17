from flask_wtf import form

from market import app
from flask import render_template, redirect, url_for, request
from market.models import Item
from market.forms import RegisterForm
from market import db

# market_page with all the parameter that will appear in the python page.
@app.route('/')
@app.route('/market', methods=['GET', 'POST'])
def market_page():
    form = RegisterForm()
    if form.validate_on_submit():
        item_to_create = Item(id=form.id.data, name=form.name.data, price=form.price.data)
        db.session.add(item_to_create)
        db.session.commit()
        return redirect(url_for("market_page"))
    return render_template('market.html', form=form)

#search page in python
@app.route('/search')
def search_page():
#the 5 next line is for the read the db and choose the search parameter and appear on the display
    q = request.args.get('q')
    if q:
        items = Item.query.filter(Item.name.contains(q))
    else:
        items = Item.query.order_by(Item.id).all()
    return render_template('search.html', items=items, form=form,)
