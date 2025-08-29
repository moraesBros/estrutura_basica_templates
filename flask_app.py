from flask import Flask

app = Flask(__name__)

# Cabeçalho HTML comum com estilo para p, h1 e hr
COMMON_HEADER = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Flasky App</title>
  <style>
    /* Recuo de 1em e margem inferior de 2em em todos os parágrafos */
    p {
      margin-left: 1em;
      margin-bottom: 2em;
    }
    /* Remover sublinhado de todos os links */
    a {
      text-decoration: none;
    }
    /* Alinhar h1 com o mesmo recuo dos parágrafos e definir fonte Arial */
    h1 {
      margin: 0;
      margin-left: 1em;
      font-family: Arial, sans-serif;
    }
    /* Linha horizontal alinhada às mesmas margens dos títulos */
    hr {
      margin-left: 1em;
      margin-right: 1em;
      border: none;
      border-top: 1px solid #000;
      margin-bottom: 2em; /* opcional: espaço após a linha */
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
    <p>
      <b><a href="/Flasky" style="margin-left: 20px;">.Flasky</a></b>
      <a href="/Home" style="margin-left: 20px;">.Home</a>
    </p>
    <h1>Hello World!</h1>
    <hr>
    """ + COMMON_FOOTER

@app.route('/Home')
def Home():
    return COMMON_HEADER + """
    <p>
      <b><a href="/Flasky" style="margin-left: 20px;">.Flasky</a></b>
      <a href="/Home" style="margin-left: 20px;">.Home</a>
    </p>
    <h1>Hello, Ednilton Moraes!</h1>
    <hr>
    <p><a href="/" style="margin-left: 20px;">voltar</a></p>
    """ + COMMON_FOOTER

@app.route('/Flasky')
def flasky():
    return COMMON_HEADER + """
    <p>
      <b><a href="/Flasky" style="margin-left: 20px;">.Flasky</a></b>
      <a href="/Home" style="margin-left: 20px;">.Home</a>
    </p>
    <h1>Hello World!</h1>
    <hr>
    """ + COMMON_FOOTER

if __name__ == '__main__':
    app.run(debug=True)
