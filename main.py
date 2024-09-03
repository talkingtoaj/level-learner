from fasthtml.common import *
import json
from models import QuizQuestion, User
from database import Database
import markdown
import atexit

app, rt = fast_app(hdrs=(Link(rel="stylesheet", href="/static/styles.css"),))

db = Database()

def load_quiz(level):
    with open(f'content/quiz-{level}.json', 'r') as f:
        return [QuizQuestion(**q) for q in json.load(f)]

def load_tutorial(level):
    with open(f'content/tutorial-{level}.md', 'r') as f:
        return markdown.markdown(f.read())

def update_tutorial_buttons(username):
    user = db.get_user(username)
    return Div(
        *[Button(f"Level {i}", hx_get=f"/tutorial/{i}", hx_target="#content")
          for i in range(1, user.current_level + 1)],
        id="tutorial-links-content",
        hx_swap_oob="true"
    )

@rt('/')
def get():
    return Titled("Python RE Tutorial",
        Div(
            Div(
                Div(
                    Form(
                        Input(name="username", placeholder="Enter your username"),
                        Button("Start", type="submit"),
                        hx_post="/start",
                        hx_target="#content"
                    ),
                    id="login-form"
                ),
                Div(id="content"),
                cls="main-content"
            ),
            Div(id="tutorial-links-content", cls="tutorial-pane"),
            cls="container"
        )
    )

@rt('/start')
def post(username: str):
    user = db.get_user(username) or db.create_user(username)
    return Div(
        quiz_page(user),
        update_tutorial_buttons(username),
        Script("document.getElementById('login-form').style.display = 'none';")
    )

def quiz_page(user):
    quiz = load_quiz(user.current_level)
    question_index = len(user.quiz_scores) % len(quiz)
    return Div(
        H2(f"Level {user.current_level} Quiz"),
        Form(
            P(quiz[question_index].question),
            Input(name="answer", placeholder="Your answer", autofocus=True),
            Hidden(name="question_index", value=str(question_index)),
            Hidden(name="username", value=user.username),
            Button("Submit", type="submit"),
            hx_post="/check",
            hx_target="#content",
            _js="this.addEventListener('submit', function(e) { e.preventDefault(); htmx.trigger(this, 'submit'); });"
        ),
        Div(id="result"),
        Button("Logout", hx_post="/logout", hx_target="body"),
        _replace=True
    )

@rt('/check')
def post(username: str, answer: str, question_index: int):
    user = db.get_user(username)
    quiz = load_quiz(user.current_level)
    correct = quiz[question_index].answer == answer
    
    user.quiz_scores.append(1 if correct else 0)
    if len(user.quiz_scores) > 4:
        user.quiz_scores = user.quiz_scores[-4:]
    
    if correct:
        result = P("Correct!")
    else:
        result = Div(
            P("Incorrect. The correct answer is:"),
            P(quiz[question_index].answer, cls="correct-answer"),
            Form(
                Button("Continue", type="submit"),
                hx_post=f"/next_question/{username}/{question_index}",
                hx_target="#content",
                _js="this.addEventListener('submit', function(e) { e.preventDefault(); htmx.trigger(this, 'submit'); });"
            )
        )
    
    if len(user.quiz_scores) >= 4 and sum(user.quiz_scores) / len(user.quiz_scores) > 0.75:
        user.current_level += 1
        user.quiz_scores = []
        db.update_user(user)
        return Div(
            H2("Level Complete!"),
            P(f"You've advanced to Level {user.current_level}"),
            Button("Start Next Level", hx_post=f"/start_level/{username}", hx_target="#content"),
            update_tutorial_buttons(username)
        )
    
    db.update_user(user)
    
    return Div(
        result,
        _after=update_tutorial_buttons(username),
        _replace=True
    ) if not correct else next_question(username, question_index)

@rt('/next_question/{username}/{question_index}')
def post(username: str, question_index: int):
    return next_question(username, question_index)

def next_question(username: str, question_index: int):
    user = db.get_user(username)
    quiz = load_quiz(user.current_level)
    next_index = (int(question_index) + 1) % len(quiz)
    return Div(
        H2(f"Level {user.current_level} Quiz"),
        Form(
            P(quiz[next_index].question),
            Input(name="answer", placeholder="Your answer", autofocus=True),
            Hidden(name="question_index", value=str(next_index)),
            Hidden(name="username", value=username),
            Button("Submit", type="submit"),
            hx_post="/check",
            hx_target="#content",  # Changed from htmx_target to hx_target
            _js="this.addEventListener('submit', function(e) { e.preventDefault(); htmx.trigger(this, 'submit'); });"
        ),
        Div(id="result"),
        Button("Logout", hx_post="/logout", hx_target="body"),
        update_tutorial_buttons(username),
        _replace=True
    )

@rt('/start_level/{username}')
def post(username: str):
    user = db.get_user(username)
    return Div(
        quiz_page(user),
        update_tutorial_buttons(username)
    )

@rt('/tutorial/{level}')
def get(level: int):
    content = load_tutorial(level)
    return Div(
        H2(f"Level {level} Tutorial"),
        Div(NotStr(content)),
        Button("Back to Quiz", hx_get="/quiz", hx_target="#content")
    )

@rt('/quiz')
def get(username: str = None):
    if username:
        user = db.get_user(username)
        return Div(
            quiz_page(user),
            update_tutorial_buttons(username)
        )
    else:
        return Titled("Python RE Tutorial",
            Form(
                Input(name="username", placeholder="Enter your username"),
                Button("Start", type="submit"),
                hx_post="/start",
                hx_target="#content"
            ),
            Div(id="content")
        )

@rt('/logout')
def post():
    return Div(
        Form(
            Input(name="username", placeholder="Enter your username"),
            Button("Start", type="submit"),
            hx_post="/start",
            hx_target="#content"
        ),
        id="login-form",
        _after=Div(id="content"),
        _replace=True
    )

def cleanup():
    if hasattr(db._local, 'connection'):
        db._local.connection.close()

atexit.register(cleanup)

serve()