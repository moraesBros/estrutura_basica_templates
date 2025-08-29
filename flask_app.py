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
    /* Faixa preta full-width com padding dobrado para aumentar a altura */
    header {
      background-color: #000;
      width: 100%;
      padding: 1em 0 1em 1em;  /* top/bottom: 1em (dobrado de 0.5em); esquerda: 1em */
    }
    /* Navegação sem margem adicional */
    header nav {
      /* padding interno já está no header */
    }
    /* Links em cinza, sem sublinhado, .Flasky com recuo triplo */
    header nav a {
      color: gray;
      text-decoration: none;
      font-family: Arial, sans-serif;
      margin-right: 20px;
    }
    /* Recuo extra apenas em .Flasky */
    header nav a.flasky {
      margin-left: 3em;  /* triplo do recuo básico de 1em */
    }
    /* Parágrafos padrão */
    p {
      margin-left: 1em;
      margin-bottom: 2em;
      font-family: Arial, sans-serif;
    }
    /* Títulos alinhados ao mesmo recuo e em Arial */
    h1 {
      margin: 00;
      margin-left: 1em;
      font-family: Arial, sans-serif;
    }
    /* Linha horizontal alinhada às margens dos textos */
    hr {
      margin-left: 1em;
      margin-right: 1em;
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
    <!-- Duas linhas em branco antes do título -->
    <p></p>
    <p></p>
    <h1>Hello World!</h1>
    <p></p>
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
    <!-- Duas linhas em branco antes do título -->
    <p></p>
    <p></p>
    <h1>Hello, Ednilton Moraes!</h1>
    <p></p>
    <hr>
    <p><a href="/">voltar</a></p>
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
    <!-- Duas linhas em branco antes do título -->
    <p></p>
    <p></p>
    <h1>Hello World!</h1>
    <p></p>
    <hr>
    """ + COMMON_FOOTER

if __name__ == '__main__':
    app.run(debug=True)
