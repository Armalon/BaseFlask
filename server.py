from flask import Flask, escape, request, url_for, render_template, make_response

# https://flask.palletsprojects.com/en/1.1.x/quickstart/
app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get('name', 'World') # this is context local https://flask.palletsprojects.com/en/1.1.x/quickstart/#context-locals
    # request.method
    # request.form
    # request.args.get
    # request.cookies.get('username')
    username = request.cookies.get('username')
    link_address = url_for('show_user_profile', username=username)
    static_link = url_for('static', filename='style.css')
    return f'Hello!, {escape(name)}. Here is the link to <a href="{link_address}">{username}</a> <br> and here is s just <a href="{static_link}">link</a>'


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        # f.save('/var/www/uploads/' + secure_filename(f.filename))


@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    return render_template('hello.html', username=username)


@app.route('/test')
def test():
    resp = make_response(render_template('just_cookies.html'))
    resp.set_cookie('username', 'the username')
    return resp


@app.route('/login')
def login():
    """
    Authorizing user and setting it's data into a session
    :return:
    {
        error: 0,
    }
    """
    pass

@app.route('/logout')
def logout():
    """
    Logging user out
    :return:
    {
        error: 0,
    }
    """

@app.route('/mychats')
def login():
    """
    Show Chats where I can write
    :return:
    {
        error: 0,
        chats: [...Chat]
    }
    """
    pass

@app.route('/chat-messages')
def login():
    """
    Show all Messages in a Chat
    :return:
    {
        error: 0,
        messages: [...Message]
    }
    """
    pass


@app.route('/chat-post-message')
def login():
    """
    Putting Message in a Chat
    :return:
    {
        error: 0,
        message: Message
    }
    """
    pass