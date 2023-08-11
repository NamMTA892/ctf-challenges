from flask import Flask, request, abort, render_template, render_template_string
import re
import os

app = Flask(__name__)
app.config['FLAG'] = os.environ['FLAG']


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')


@app.route('/admin', methods=['GET'])
def admin():
    return abort(403)


@app.route('/submit', methods=['POST'])
def validation():
    data = request.form['payload']
    bad_chars = "'_#&;+"
    bad_cmds = ['config', 'os', 'popen', 'subprocess']
    if len(data) > 64:
        return render_template('error.html')
    if any(char in bad_chars for char in data):
        return render_template('error.html')
    if data.find('import') != -1:
        return render_template('error.html')
    for cmd in bad_cmds:
        if findWholeWord(cmd)(data):
            return render_template('error.html')

    valid_submitted_template = """
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Feedback Form</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous"
    />
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous"
    ></script>
  </head>
  <body>
    <!-- Responsive navbar-->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="#">BKSEC 2023</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Admin Panel</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- Page content-->
    <div class="container">
      <div class="text-center mt-5">
        <h1>Feedback form for Watermelon clan</h1>
        <p class="lead">We hope you have a good time with us!</p>
      </div>

      <div class="alert alert-info" role="alert">Your message is: """ + data + """ </div>
      <div class="alert alert-info" role="alert">
        It will soon be checked by our admins!
      </div>
    </div>
    <div class="container">
  <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <p class="col-md-4 mb-0 text-muted">Proudly powered by Flask 2.2.2.</p>
  </footer>
</div>
  </body>
</html>
"""
    return render_template_string(valid_submitted_template)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'], debug=False)