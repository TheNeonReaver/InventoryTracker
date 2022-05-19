from trackingapp import app, db
from flask import render_template, redirect, url_for, flash, request
from trackingapp.models import Item, Shipment
from trackingapp.forms import AddItemForm, DockForm, DeleteForm, UpdateForm, EditPageForm, AddShipmentForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/inventory', methods=['GET', 'POST'])
def inventory_page():
    ship_form = AddShipmentForm()
    dock_form = DockForm()
    delete_form = DeleteForm()
    edit_form = EditPageForm()

    if request.method == "POST":
        # adding item to shipment logic
        shipping_item = request.form.get('shipping_item')
        s_item_object = Item.query.filter_by(name=shipping_item).first()
        if s_item_object:
            flash(f"You have assigned {s_item_object.name} for shipment!", category='success')

        # delete item logic
        if delete_form.validate_on_submit():
            deleted_item = request.form.get('deleted_item')
            d_item_object = Item.query.filter_by(name=deleted_item).first()
            flash(f"You have deleted this item!", category='success')
            db.session.delete(d_item_object)
            db.session.commit()

        # return item logic
        preshipped_item = request.form.get('preshipped_item')
        p_item_object = Item.query.filter_by(name=preshipped_item).first()
        if p_item_object:
            flash(f"You have shelved {p_item_object.name}!", category='success')

        return redirect(url_for('inventory_page'))

    if request.method == "GET":
        return render_template('market.html', ship_form=ship_form,
                               dock_form=dock_form, delete_form=delete_form, edit_form=edit_form)


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
    print(request.form)
    update_form = UpdateForm()

    updated_item = request.args.get('updated_item')
    u_item_object = Item.query.filter_by(name=updated_item).first()

    if request.method == "POST":
        print("Just before name change")
        setattr(u_item_object, 'name', update_form.name.data)
        print("Just before price change")
        setattr(u_item_object, 'price', update_form.price.data)
        print("Just before desc. change")
        setattr(u_item_object, 'description', update_form.description.data)
        print("Just before commit")
        db.session.commit()
        print(u_item_object.price)
        flash(f'You have successfully edited {u_item_object.name}!', category='success')
        return redirect(url_for('inventory_page'))

    return render_template('update.html', update_form=update_form)
