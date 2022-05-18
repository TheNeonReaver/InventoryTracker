from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired


class AddItemForm(FlaskForm):
    name = StringField(label='Item Name:', validators=[Length(max=40), DataRequired()])
    price = StringField(label='Price', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired()])
    submit = SubmitField(label='Add Item to Database')


class DeleteForm(FlaskForm):
    submit = SubmitField(label='Delete Item')


class UpdateForm(FlaskForm):
    name = StringField(label='Item Name:', validators=[Length(max=40), DataRequired()])
    price = StringField(label='Price', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired()])
    submit = SubmitField(label='Edit Item')


class ShipForm(FlaskForm):
    submit = SubmitField(label='Add Item to Shipment')


class DockForm(FlaskForm):
    submit = SubmitField(label='Return Item to Inventory')
