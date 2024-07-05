from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valo_hora = input("Digite o valor da hora hora trabalhada: ")
prazo = input("Digite o prazo estimado para conclusão: ")


valor_total = int(horas_estimadas)*int(valo_hora)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115,175, valo_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")
