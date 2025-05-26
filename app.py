from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory "database"
books = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def list_books():
    return render_template('books.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        books.append({'title': title, 'author': author})
        return redirect(url_for('list_books'))
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)
