from flask import Flask

app = Flask(__name__)

COMMON_HEADER = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Flasky App</title>
  <style>
    body {
      margin: 0;  /* zera margens para a faixa preta ocupar 100% da largura */
    }
    header {
      background-color: #000;
      width: 100%;
      padding: 1em 0 1em 1em;  /* dobra a altura da faixa e alinha 1em da esquerda */
    }
    header nav a {
      color: gray;
      text-decoration: none;
      font-family: Arial, sans-serif;
      margin-right: 20px;
    }
    header nav a.flasky {
      margin-left: 6em;  /* dobro do afastamento padrão para .Flasky */
    }
    h1 {
      margin: 0;
      margin-left: 3em;  /* metade do afastamento de .Flasky */
      font-family: Arial, sans-serif;
    }
    p {
      margin-left: 1em;
      margin-bottom: 2em;
      font-family: Arial, sans-serif;
    }
    hr {
      margin-left: 7em;   /* igual à margem direita para centralizar */
      margin-right: 7em;
      border: none;
      border-top: 1px solid #000;
      margin-bottom: 2em;
    }
  </style>
</head>
<body>
"""

COMMON_FOOTER = """
</body>
</html>
"""

@app.route('/')
def titulo():
    return COMMON_HEADER + """
    <header>
      <nav>
        <a href="/Flasky" class="flasky">.Flasky</a>
        <a href="/Home">.Home</a>
      </nav>
    </header>

    <p></p>
    <p></p>

    <h1>Hello World!</h1>
    <hr>
    """ + COMMON_FOOTER

@app.route('/Home')
def Home():
    return COMMON_HEADER + """
    <header>
      <nav>
        <a href="/Flasky" class="flasky">.Flasky</a>
        <a href="/Home">.Home</a>
      </nav>
    </header>

    <p></p>
    <p></p>

    <h1>Hello, Ednilton Moraes!</h1>
    <hr>
    """ + COMMON_FOOTER

@app.route('/Flasky')
def flasky():
    return COMMON_HEADER + """
    <header>
      <nav>
        <a href="/Flasky" class="flasky">.Flasky</a>
        <a href="/Home">.Home</a>
      </nav>
    </header>

    <p></p>
    <p></p>

    <h1>Hello World!</h1>
    <hr>
    """ + COMMON_FOOTER

@app.route('/rotainexistente')
def rota_inexistente():
    return COMMON_HEADER + """
    <header>
      <nav>
        <a href="/Flasky" class="flasky">.Flasky</a>
        <a href="/Home">.Home</a>
      </nav>
    </header>

    <p></p>
    <p></p>

    <h1>Not Found</h1>
    <hr>
    """ + COMMON_FOOTER

if __name__ == '__main__':
    app.run(debug=True)
