from flask import Flask, render_templeate

app = Flask(__name__)

@app.route('/')
def inicio():
nome = "Turma de Programação"
curso = "Phyton com HTML"

return render_templeate(
'index.html',
nome = nome,
curso = curso
)

@app.route('/sobre')
def sobre():
return
"""
<H1>Sobre o Projeto</H1>
<p>Este código foi criado com Phyton e Flask.</p>
<a href="/"> Volta para i inicio<a>
"""
if__name__=='__main__':
app.run(host='0.0.0.0', port=3000, debug=True)