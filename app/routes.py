from flask import render_template, redirect, url_for
from app import app
from app.forms import SelfPriceForm, ShotForm
from app.calculations import calculate_self_price, soul_shot, blessed_spirit_shot, display_result

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/self_price', methods=['GET', 'POST'])
def self_price():
    form = SelfPriceForm()
    if form.validate_on_submit():
        result = calculate_self_price(form.grade.data, form.item_price.data, form.cry_amount.data)
        if result:
            return render_template('self_price.html', form=form, result=result)
    return render_template('self_price.html', form=form)

@app.route('/soul_shot', methods=['GET', 'POST'])
def soul_shot_route():
    form = ShotForm()
    if form.validate_on_submit():
        result = soul_shot(form.grade.data, form.cry.data)
        display_result(form.cry.data, form.grade.data, result, 'SoulShot')
        return render_template('soul_shot.html', form=form, result=result)
    return render_template('soul_shot.html', form=form)

@app.route('/blessed_spirit_shot', methods=['GET', 'POST'])
def blessed_spirit_shot_route():
    form = ShotForm()
    if form.validate_on_submit():
        result = blessed_spirit_shot(form.grade.data, form.cry.data)
        display_result(form.cry.data, form.grade.data, result, 'BlessedSpiritShot')
        return render_template('blessed_spirit_shot.html', form=form, result=result)
    return render_template('blessed_spirit_shot.html', form=form)
