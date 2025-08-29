from flask import Flask

app = Flask(__name__)

COMMON_HEADER = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Flasky App</title>
  <style>
    /* Zera margem do body para a faixa ocupar 100% da largura */
    body {
      margin: 0;
    }
    /* Faixa preta full-width com padding para alinhar o conteúdo */
    header {
      background-color: #000;
      width: 100%;
      padding: 1em 0 1em 1em;
    }
    /* Links em cinza, sem sublinhado, espaçamento entre eles */
    header nav a {
      color: gray;
      text-decoration: none;
      font-family: Arial, sans-serif;
      margin-right: 20px;
    }
    /* .Flasky dobra o recuo da margem esquerda (de 3em para 6em) */
    header nav a.flasky {
      margin-left: 6em;
    }

    /* Títulos alinhados ao mesmo recuo de .Flasky (1em de padding + 6em) */
    h1 {
      margin: 0;
      margin-left: 6em;
      font-family: Arial, sans-serif;
    }

    /* Parágrafos padrão */
    p {
      margin-left: 1em;
      margin-bottom: 2em;
      font-family: Arial, sans-serif;
    }

    /* Linha horizontal com mesmo afastamento das margens esquerda e direita */
    hr {
      margin-left: 7em;
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

if __name__ == '__main__':
    app.run(debug=True)
