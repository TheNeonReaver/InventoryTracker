from trackingapp import app, db
from flask import render_template, redirect, url_for, flash, request
from trackingapp.models import Item
from trackingapp.forms import AddItemForm, ShipForm, DockForm, DeleteForm, UpdateForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/inventory', methods=['GET', 'POST'])
def inventory_page():
    ship_form = ShipForm()
    dock_form = DockForm()
    delete_form = DeleteForm()
    update_form = UpdateForm()

    if update_form.validate_on_submit():
        return redirect(url_for('inventory_page'))

    if request.method == "POST":
        # adding item to shipment logic
        shipping_item = request.form.get('shipping_item')
        s_item_object = Item.query.filter_by(name=shipping_item).first()
        s_item_ship = Item.query.filter_by(shipping=shipping_item).first()
        if s_item_object:
            s_item_ship = 1
            flash(f"You have assigned {s_item_object.name} for shipment!", category='success')

        # delete item logic
        if delete_form.validate_on_submit():
            item_to_delete = request.form.get('item_to_delete')
            print("It's being pressed")
            flash(f"You have deleted this item!", category='success')
            db.session.delete(item_to_delete)
            db.session.commit()

        # sell item logic
        preshipped_item = request.form.get('preshipped_item')
        p_item_object = Item.query.filter_by(name=preshipped_item).first()
        p_item_ship = Item.query.filter_by(shipping=preshipped_item).first()
        if p_item_object:
            p_item_ship = 0
            flash(f"You have shelved {p_item_object.name}!", category='success')

        return redirect(url_for('inventory_page'))

    if request.method == "GET":
        items = Item.query.filter_by(shipping=0)
        preshipped_items = Item.query.filter_by(shipping=1)
        return render_template('market.html', items=items, preshipped_items=preshipped_items, ship_form=ship_form,
                               dock_form=dock_form, delete_form=delete_form, update_form=update_form)


@app.route('/add_item', methods=['GET', 'POST'])
def add_page():
    add_form = AddItemForm()
    if add_form.validate_on_submit():
        item_to_add = Item(name=add_form.name.data,
                           price=add_form.price.data,
                           description=add_form.description.data)
        db.session.add(item_to_add)
        db.session.commit()
        flash(f'You have successfully added {item_to_add.name}!', category='success')
        return redirect(url_for('inventory_page'))
    if add_form.errors != {}:  # if there are no errors from validations
        for err_msg in add_form.errors.values():
            flash(f'There was an error with adding this item: {err_msg}', category='danger')

    return render_template('add.html', add_form=add_form)


@app.route('/edit_item', methods=['GET', 'POST'])
def edit_page():
    update_form = UpdateForm()
    if update_form.validate_on_submit():
        item_to_edit = Item(name=update_form.name.data,
                            price=update_form.price.data,
                            description=update_form.description.data)
        db.session.update(item_to_edit)
        db.session.commit()
        flash(f'You have successfully edited {item_to_edit.name}!', category='success')
        return redirect(url_for('inventory_page'))
    if update_form.errors != {}:  # if there are no errors from validations
        for err_msg in update_form.errors.values():
            flash(f'There was an error with editing this item: {err_msg}', category='danger')

    return render_template('update.html', update_form=update_form)
