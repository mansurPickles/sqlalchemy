from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Brandon Luong',
        'title': 'Hello World',
        'content': 'Hello World!',
        'data_posted': 'April 01 2019'
    },
    {
        'author': 'Alice',
        'title': 'Second Post',
        'content': 'Lorem Ipsom',
        'data_posted': 'April 02 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")


if __name__ == '__main__':
    app.run(debug=True)
