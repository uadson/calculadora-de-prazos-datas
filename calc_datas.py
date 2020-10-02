# Cálculo de datas para contagem de prazo


# 1 Importando bibliotecas necessárias
from datetime import date, datetime
import calendar


# 2 Incluindo Cabeçalho e linhas divisórias
print('CALCULADORA DE PRAZOS')

def linha():
	print('=' * 45, '\n')

linha()


# 3 Execução do Script com Loop while True
while True:

# 4 Solicitando os dados do usuário com tratamento de exceção
	while True:
		try:
			string = input('\nData da Infração ex.:(01011999): ').strip()
		except ValueError:
			print('Informe uma data válida!')
		else:
			if len(string) > 8 or len(string) < 8:
				print('Informe uma data válida! Ex.: 01011999')
			else:
				break

	while True:
		try:
			prazo = int(input('Informe o prazo(em dias): '))
		except ValueError:
			print('Dados Incorretos! Digite novamente!')
		else:
			break


	# 5 Convertendo a string para o tipo data - saída 0000-00-00
	date = datetime.strptime(string, '%d%m%Y')

	
	# 6 Obtendo o mês e o ano relativo a data informada
	mes = date.month
	ano = date.year


	# 7 Obtendo data final após prazo informado

	final_date = date.fromordinal(date.toordinal()+(prazo))


	# 8 Obtendo o dia útil da semana com base na data final
	dias = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 
		'Sexta-Feira', 'Sábado', 'Domingo')

	dia_util = dias[final_date.weekday()]


	# 9 Caso a data final caia em um sábado ou domingo, deverá retornar o próximo dia útil
	if dias[final_date.weekday()] == 5 or dias[final_date.weekday()] == 6:
		prox_dia_util = date.fromordinal(final_date.toordinal()+2)
		# o dia útil então será baseado nesta nova data
		dia_util = dias[prox_dia_util.weekday()]

	else:

		dia_util = dias[final_date.weekday()]

	
	# 10 Obtendo o mês baseadao na data final, quando esta cai no mês subsequente	
	prox_mes = final_date.month

	
	# 11 Organizando o calendários com as datas obtidas

	# calendario do mes referente a primeira data informada
	c1 = calendar.TextCalendar(calendar.SUNDAY)
	cal1 = c1.formatmonth(ano, mes)

	# calendario do mes referente a data final quando esta cai para o mês seguinte
	c2 = calendar.TextCalendar(calendar.SUNDAY)
	cal2 = c2.formatmonth(ano, prox_mes)

	linha()

	print(cal1)

	print()

	# o segundo calendário será apresentado somente se a data cair para o próximo mês
	if prox_mes != mes:
		print(cal2)

	print()

	linha()


	# 12 Formatando a saída para o modelo de data desejado 00/00/0000 (data final)
	data_fim = final_date.strftime('%d/%m/%Y')

	# apresentando o resultado
	print(f'Prazo Final: {data_fim}, {dia_util}')

	linha()

	# 13 Pra finalizar uma variável que receberá um valor que definirá a continuidade
	# ou não do loop.
	resposta = input('\nDeseja Continuar ? [S/N]').strip().upper()
	
	if resposta in 'Nn':
		break
		
	
	







