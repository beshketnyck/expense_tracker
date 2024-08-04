from flask import Flask, render_template, request, redirect, url_for
from models.expense import Expense
from models.category import Category
from database import db_session, init_db

app = Flask(__name__)

@app.route('/')
def index():
    categories = Category.query.filter(Category.name != 'Без категорії').all()
    expenses = db_session.query(Expense).all()
    return render_template('index.html', categories=categories, expenses=expenses)

@app.route('/add_category', methods=['POST'])
def add_category():
    name = request.form['name'].capitalize()
    category = Category(name=name)
    db_session.add(category)
    db_session.commit()
    return redirect(url_for('index'))

@app.route('/edit_category/<int:id>', methods=['POST'])
def edit_category(id):
    category = Category.query.get(id)
    category.name = request.form['name'].capitalize()
    db_session.commit()
    return redirect(url_for('index'))

@app.route('/delete_category/<int:id>')
def delete_category(id):
    try:
        category = Category.query.get(id)
        default_category = Category.query.filter_by(name='Без категорії').first()

        # Якщо категорія "Без категорії" не знайдена, створимо її
        if not default_category:
            default_category = Category(name='Без категорії')
            db_session.add(default_category)
            db_session.commit()

        # Переназначаємо всі витрати до категорії "Без категорії"
        expenses = Expense.query.filter_by(category_id=id).all()
        for expense in expenses:
            expense.category_id = default_category.id

        db_session.commit()  # Зберігаємо зміни у витратах перед видаленням категорії
        db_session.delete(category)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        print(f"Error deleting category: {e}")
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category_id = request.form['category_id']
    comment = request.form['comment']
    date = request.form['date']
    if not category_id:
        default_category = Category.query.filter_by(name='Без категорії').first()
        if not default_category:
            default_category = Category(name='Без категорії')
            db_session.add(default_category)
            db_session.commit()
        category_id = default_category.id
    expense = Expense(amount=amount, category_id=category_id, comment=comment, date=date)
    db_session.add(expense)
    db_session.commit()
    return redirect(url_for('index'))

@app.route('/edit_expense/<int:id>', methods=['POST'])
def edit_expense(id):
    expense = Expense.query.get(id)
    expense.amount = request.form['amount']
    expense.category_id = request.form['category_id']
    expense.comment = request.form['comment']
    expense.date = request.form['date']
    db_session.commit()
    return redirect(url_for('index'))

@app.route('/delete_expense/<int:id>')
def delete_expense(id):
    expense = Expense.query.get(id)
    db_session.delete(expense)
    db_session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()

    # Створення категорії "Без категорії", якщо ще не існує
    if not Category.query.filter_by(name='Без категорії').first():
        default_category = Category(name='Без категорії')
        db_session.add(default_category)
        db_session.commit()

    app.run(debug=True)