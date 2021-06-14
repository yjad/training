from flask import Flask, render_template, url_for

posts_data = [
    {'author': 'Yahia Jad',
     'title': "How to learn Python in 5 days",
     'content':'this is a book/ video for learning Python',
     'date_posted':'18-2-2020'
    },
    {'author': 'Author-2',
     'title': "title-2",
     'content':'content-2',
     'date_posted': '21-01-2020'
    }
]

app = Flask(__name__)

@app.route ("/")
@app.route('/home')
def home():
    return render_template("home.html",posts = posts_data, title = 'Blogs')


@app.route('/about')
def about():
    # return render_template("about.html",posts = posts_data, title="By Yahia")
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)

