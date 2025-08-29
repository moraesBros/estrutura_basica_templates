from flask import Flask

app = Flask(__name__)

# Cabeçalho HTML comum com estilo
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
    /* Faixa preta full-width */
    header {
      background-color: #000;
      width: 100%;
    }
    /* Navegação dentro da faixa, recuada 1em da esquerda */
    header nav {
      margin-left: 1em;
      padding: 0.5em 0;
    }
    /* Links em cinza e sem sublinhado */
    header nav a {
      color: gray;
      text-decoration: none;
      margin-right: 20px;
    }
    /* Parágrafos padrão */
    p {
      margin-left: 1em;
      margin-bottom: 2em;
    }
    /* Títulos alinhados ao mesmo recuo e em Arial */
    h1 {
      margin: 0;
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
        <a href="/Flasky">.Flasky</a>
        <a href="/Home">.Home</a>
      </nav>
    </header>
    <h1>Hello World!</h1>
    <p></p>  <!-- parágrafo extra em branco -->
    <hr>
    """ + COMMON_FOOTER

@app.route('/Home')
def Home():
    return COMMON_HEADER + """
    <header>
      <nav>
        <a href="/Flasky">.Flasky</a>
        <a href="/Home">.Home</a>
      </nav>
    </header>
    <h1>Hello, Ednilton Moraes!</h1>
    <p></p>  <!-- parágrafo extra em branco -->
    <hr>
    <p><a href="/">voltar</a></p>
    """ + COMMON_FOOTER

@app.route('/Flasky')
def flasky():
    return COMMON_HEADER + """
    <header>
      <nav>
        <a href="/Flasky">.Flasky</a>
        <a href="/Home">.Home</a>
      </nav>
    </header>
    <h1>Hello World!</h1>
    <p></p>  <!-- parágrafo extra em branco -->
    <hr>
    """ + COMMON_FOOTER

if __name__ == '__main__':
    app.run(debug=True)
