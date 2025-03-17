import sqlite3
from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():
    conn = sqlite3.connect('site.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL UNIQUE,
                 password TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS blog_posts (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT NOT NULL,
                 author TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS blog_entries (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 post_id INTEGER NOT NULL,
                 content TEXT NOT NULL,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                 FOREIGN KEY (post_id) REFERENCES blog_posts (id))''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    conn = sqlite3.connect('site.db')
    c = conn.cursor()
    c.execute("SELECT * FROM blog_posts")
    posts = c.fetchall()
    conn.close()
    return render_template('home.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('site.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists. Please choose a different one.', 'danger')
        conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('site.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'username' not in session:
        flash('You need to be logged in to create a blog post.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        author = session['username']

        conn = sqlite3.connect('site.db')
        c = conn.cursor()
        c.execute("INSERT INTO blog_posts (title, author) VALUES (?, ?)", (title, author))
        conn.commit()
        conn.close()

        flash('Blog post created successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('create.html')

@app.route('/post/<int:post_id>', methods=['GET'])
def view_post(post_id):
    conn = sqlite3.connect('site.db')
    c = conn.cursor()
    c.execute("SELECT * FROM blog_posts WHERE id = ?", (post_id,))
    post = c.fetchone()

    c.execute("SELECT * FROM blog_entries WHERE post_id = ? ORDER BY created_at DESC", (post_id,))
    entries = c.fetchall()
    conn.close()

    return render_template('view_post.html', post=post, entries=entries)

@app.route('/post/<int:post_id>/add_entry', methods=['GET', 'POST'])
def add_entry(post_id):
    if 'username' not in session:
        flash('You need to be logged in to add an entry.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        content = request.form['content']

        conn = sqlite3.connect('site.db')
        c = conn.cursor()
        c.execute("INSERT INTO blog_entries (post_id, content) VALUES (?, ?)", (post_id, content))
        conn.commit()
        conn.close()

        flash('Entry added successfully!', 'success')
        return redirect(url_for('view_post', post_id=post_id))

    return render_template('add_entry.html', post_id=post_id)

@app.route('/edit/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    if 'username' not in session:
        flash('You need to be logged in to edit an entry.', 'danger')
        return redirect(url_for('login'))

    conn = sqlite3.connect('site.db')
    c = conn.cursor()
    c.execute("SELECT * FROM blog_entries WHERE id = ?", (entry_id,))
    entry = c.fetchone()
    conn.close()

    if entry is None:
        flash('Entry not found.', 'danger')
        return redirect(url_for('home'))

    if request.method == 'POST':
        content = request.form['content']

        conn = sqlite3.connect('site.db')
        c = conn.cursor()
        c.execute("UPDATE blog_entries SET content = ? WHERE id = ?", (content, entry_id))
        conn.commit()
        conn.close()

        flash('Entry updated successfully!', 'success')
        return redirect(url_for('view_post', post_id=entry[1]))

    return render_template('edit_entry.html', entry=entry)

@app.route('/my_posts')
def my_posts():
    if 'username' not in session:
        flash('You need to be logged in to view your posts.', 'danger')
        return redirect(url_for('login'))

    conn = sqlite3.connect('site.db')
    c = conn.cursor()
    c.execute("SELECT * FROM blog_posts WHERE author = ?", (session['username'],))
    posts = c.fetchall()
    conn.close()

    return render_template('my_posts.html', posts=posts)

@app.route('/user/<username>')
def user_posts(username):
    conn = sqlite3.connect('site.db')
    c = conn.cursor()
    c.execute("SELECT * FROM blog_posts WHERE author = ?", (username,))
    posts = c.fetchall()
    conn.close()

    return render_template('user_posts.html', posts=posts, username=username)

if __name__ == '__main__':
    app.run(debug=True)