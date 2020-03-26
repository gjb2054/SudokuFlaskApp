from flask import Flask, render_template, request, session, redirect, url_for
from UserLibrary import UserLibrary
from SudokuBoard import SudokuBoard
import SudokuSolver

app = Flask(__name__)
app.secret_key = "testing_secret_key_help"

UL = UserLibrary()


@app.route('/', methods=["GET"])
def home():
    if request.method == 'GET':
        if session.get('username') is not None:
            if not UL.user_exist(session['username']):
                session.pop('username')
        return render_template("index.html", username=session.get("username"))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if UL.add_user(username):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template("login.html", err_msg="Login Failed, Please Try Again.")
    return render_template("login.html")


@app.route('/logout')
def logout():
    UL.logout(session.get('username'))
    session.pop('username')
    return redirect(url_for('home'))


@app.route('/game', methods=["POST", "GET"])
def game():
    user = UL.get_user(session['username'])
    sb = user.sb
    csb = user.copy_sb()
    if session.get('in_game') is None:
        session['in_game'] = True
    if request.method == "POST":
        csb = user.copy_sb()
        for num in request.form:
            input_value = request.form[num]
            if input_value != '':
                x, y = int(num[0]), int(num[1])
                csb.set_value(x, y, int(input_value))
        if SudokuSolver.solved_check(csb):
            sb = SudokuBoard(csb.grid)
        return render_template("board.html", board=sb, csb=csb)
    return render_template("board.html", board=sb, csb=csb)


@app.route('/easy')
def easy():
    user = UL.get_user(session['username'])
    user.reset_boards()
    sb = user.sb
    SudokuSolver.solve(sb)
    SudokuSolver.removal(sb, 0)
    return redirect('/game')


@app.route('/medium')
def medium():
    user = UL.get_user(session['username'])
    user.reset_boards()
    sb = user.sb
    SudokuSolver.solve(sb)
    SudokuSolver.removal(sb, 1)
    return redirect('/game')


@app.route('/hard')
def hard():
    user = UL.get_user(session['username'])
    user.reset_boards()
    sb = user.sb
    SudokuSolver.solve(sb)
    SudokuSolver.removal(sb, 2)
    return redirect('/game')


@app.route('/help')
def help_move():
    user = UL.get_user(session['username'])
    csb = SudokuBoard(user.sb.grid)
    cds = [0, 0]
    csb.find_empty_space(cds)
    SudokuSolver.solve(csb)
    sb = user.sb
    sb.set_value(cds[0], cds[1], csb.grid[cds[0]][cds[1]])
    user.csb = SudokuBoard(user.sb.grid)
    return redirect('/game')


@app.route('/solve')
def solve_board():
    user = UL.get_user(session['username'])
    SudokuSolver.solve(user.sb)
    return redirect('/game')


@app.route('/reset')
def reset():
    user = UL.get_user(session['username'])
    user.csb = SudokuBoard(user.sb.grid)
    return redirect('/game')


@app.route('/new')
def new_board():
    user = UL.get_user(session['username'])
    user.reset_boards()
    return redirect('/')


if __name__ == '__main__':
    app.run()
