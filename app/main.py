from flask import Flask, render_template, request, redirect, url_for
from models.expense import Expense
from models.category import Category
from database import db_session, init_db

app = Flask(__name__)

@app.route('/')
def index():
    expenses = Expense.query.all()
    categories = Category.query.all()
    return render_template('index.html', expenses=expenses, categories=categories)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category_id = request.form['category_id']
    comment = request.form['comment']
    date = request.form['date']
    expense = Expense(amount=amount, category_id=category_id, comment=comment, date=date)
    db_session.add(expense)
    db_session.commit()
    return redirect(url_for('index'))

@app.route('/add_category', methods=['POST'])
def add_category():
    name = request.form['name']
    category = Category(name=name)
    db_session.add(category)
    db_session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)