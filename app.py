from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Define the absolute path to the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'asset_management.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('log_In.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/assets')
def list_assets():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM overview")
    assets = cursor.fetchall()
    conn.close()
    return render_template('assets.html', assets=assets)

@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'POST':
        name = request.form['name']
        category_id = request.form['category_id']
        department_id = request.form['department_id']
        location_id = request.form['location_id']
        purchase_date = request.form['purchase_date']
        purchase_price = request.form['purchase_price']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO assets (name, category_id, department_id, location_id, purchase_date, purchase_price)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, category_id, department_id, location_id, purchase_date, purchase_price))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('list_assets'))
    else:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()
        cursor.execute("SELECT * FROM departments")
        departments = cursor.fetchall()
        cursor.execute("SELECT * FROM locations")
        locations = cursor.fetchall()
        conn.close()
        return render_template('add_asset.html', categories=categories, departments=departments, locations=locations)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
