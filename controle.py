from PyQt5 import uic, QtWidgets

def executar():

    salario = formulario.txtSalario.text()
    salario = float(salario)
    desconto = formulario.txtDescontos.text()
    desconto = float(desconto)

    resultado = salario-desconto

    formulario.lblResultado.setText(str(resultado))



app=QtWidgets.QApplication([])
formulario=uic.loadUi('tela.ui')
formulario.btnCalcular.clicked.connect(executar)

formulario.show()
app.exec()