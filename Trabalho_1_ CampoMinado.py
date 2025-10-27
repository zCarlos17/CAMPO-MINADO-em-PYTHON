linha = 0																												#QUANTIDADE DE LINHAS DO CAMPO
coluna = 0																												#QUANTIDADE DE COLUNAS DO CAMPO
quantidade_minas = 0																									#QUANTIDADE DE MINAS DEFINIDAS PELO JOGADOR
maximo_minas = 0																										#MAXIMO DE MINAS PERMITIDO (50%AREA DO CAMPO)
minas_colocadas = 0																										#CONTADOR DE MINAS COLOCADAS
campo_real = []																											#MATRIZ QUE CONTEM AS MINAS E NUMEROS REAIS
campo_visivel = []																										#MATRIZ QUE O JOGADOR ENXERGA( INICIALMENTE VAZIA!)
import random																	
from colorama import Fore, Back, Style, init																	
init()																													#INICIALIZA O COLORAMA PARA USAR CORES NO TERMINAL
#======================================================================		FUNÇOES AUXILIARES		=================================================================================
def definir_mapa():
	global linha, coluna, campo_real, campo_visivel
	while True:
		try :
			linha = int(input("||	Digite o tamanho da linha (Max 10): ")) 											#Solicitando o tamanho de Linha, com limite ate 10
			if (linha <3 or linha >10): 																				# Se o usuario digitar um tamnho maior que 10 entra como tratamento de erro
				print(Fore.RED+"||	  Tamanho inválido !! Tente novamente"+Style.RESET_ALL)
			else:																										# Caso contrario e o usuario digitar um valor que esta dentro dos parametros, finaliza o while e prossegue o codigo!
				print(Fore.GREEN+"||	  Tamanho de Linha selecionado com sucesso!"+Style.RESET_ALL)
				break
		except ValueError:
				print(Fore.RED+"||	  Apenas Numeros inteiros sao permitidos"+Style.RESET_ALL)
	while True:
		try :
			coluna = int(input("||	Digite o tamanho da Coluna (Max 10): ")) 											# Solicitando o tamanho de Linha, com limite ate 10
			if (coluna <3 or coluna >10): 																				# Se o usuario digitar um tamnho maior que 10 entra como tratamento de erro
				print(Fore.RED+"||	  Tamanho inválido !! Tente novamente"+Style.RESET_ALL)
			else:																										# Caso contrario e o usuario digitar um valor que esta dentro dos parametros, finaliza o while e prossegue o codigo!
				print(Fore.GREEN+"||	  Tamanho de Coluna selecionado com sucesso!"+Style.RESET_ALL)
				break
		except ValueError:
				print(Fore.RED+"||	  Apenas Numeros inteiros sao permitidos"+Style.RESET_ALL)
	campo_real = [["[0]" for _ in range(coluna)] for _ in range(linha)]
	campo_visivel = [["[ ]" for _ in range(coluna)] for _ in range(linha)]
	
def definir_minas():
	global linha, coluna, quantidade_minas, maximo_minas
	while True:
		if (linha == 0 and coluna == 0):
			print("||  Valores da Linha e Coluna não especificados !!\n||  Por favor defina-os primeiramente!!\n")
			break
		else:
			maximo_minas = int((linha * coluna) * 0.5)
			while True:
				try:
					quantidade_minas = int(input(f"||	Por favor insira a quantidade de Minas (Max. {maximo_minas}): "))
					if quantidade_minas > maximo_minas or quantidade_minas<=0:
						print("||	Valor máximo excedido!! Digite novamente!!")
					else:
						print(Fore.GREEN+"||	Quantidade de minas dentro do limite!!\n||	Carregando..."+Style.RESET_ALL)
						break
				except ValueError:
					print(Fore.RED+"||	  Apenas Numeros inteiros sao permitidos"+Style.RESET_ALL)
		break

def gerar_minas(): 																											# Posicionar as minas aleatoriamente no mapa!
	global campo_real
	minas_colocadas = 0
	
	while minas_colocadas < quantidade_minas: 																				#POSICIONAR ALEATORIAMENTE AS MINAS PELO MAPA
		x = random.randint(0, linha - 1) 
		y = random.randint(0, coluna- 1) 
		if campo_real[x][y] != "[*]":
			campo_real[x][y] = "[*]"
			minas_colocadas+=1
	for i in range(linha):																									#PREENCHER OS NUMEROS AO REDOR DAS MINAS
		for j in range(coluna):
			if campo_real[i][j] != "[*]":																					#VERIFICAR AS 8 POSIÇÕES VIZINHAS
				contador = 0
				for dx in range(-1, 2):
					for dy in range(-1, 2):
					    if dx == 0 and dy == 0:
					        continue
					    ni, nj = i + dx, j + dy
					    if 0 <= ni < linha and 0 <= nj < coluna:
					        if campo_real[ni][nj] == "[*]":
					            contador += 1
				campo_real[i][j] = f"[{contador}]"
	print("|| 	Minas geradas com sucesso!!")


def mostrar_campo():							 																			# Demonstra como o jogador enxerga o mapa
	print("\n ", end="") 
	for c in range(coluna): 																								#Mostra o indice de cada linha das colunas no topo
		print(f"{c+1:>4}", end="")
	print()

	for i in range(linha):																								 	#Mostra cada linha numerada e suas celulas
		print(f"{i+1:>2}", end=" ")
		for j in range(coluna):
			celula_visivel = campo_visivel[i][j]
			if celula_visivel == "[M]":
				print(Fore.YELLOW + celula_visivel + Style.RESET_ALL, end=" ")
			elif celula_visivel == "[*]":
				print(Fore.RED + celula_visivel + Style.RESET_ALL, end=" ")
			elif celula_visivel == "[0]":
				print(Fore.CYAN + celula_visivel + Style.RESET_ALL, end=" ")
			elif celula_visivel in ["[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]"]:
				print(Fore.BLUE + celula_visivel + Style.RESET_ALL, end=" ")
			else:
				print(celula_visivel,end=" ")
		print()

def abrir_celula(x,y):
	global campo_visivel
	x_idx = x-1
	y_idx = y-1
	if campo_visivel[x_idx][y_idx] != "[ ]":													#Verifica se já foi aberta ou marcada 
		print("||	Essa posição já foi aberta ou marcada !!")
		return True 																			#Continua o jogo

	if campo_real[x_idx][y_idx] =="[*]":
		for i in range(linha):
			for j in range(coluna):
				if campo_real[i][j] =="[*]":
					campo_visivel[i][j] = "[*]"
		mostrar_campo()
		print(Fore.RED+"KABOOOOOM!! VOCÊ ACERTOU UMA MINAAA !! FIM DE JOGO !!")
		quit()																					#Encerra o jogo
	else:																						#Se nao for mina, revela o numero da celula!
		campo_visivel[x_idx][y_idx] = campo_real[x_idx][y_idx]

		if campo_real[x_idx][y_idx] == "[0]":
			propagacao_abertura(x_idx, y_idx)
		return True 																			#Continua o Jogo

def propagacao_abertura(i, j):																	# Função recursiva para abrir automaticamente células vizinhas quando uma célula com valor '[0]' é aberta. i  e j são índices de matriz (0 a linha-1, 0 a coluna-1).
	global campo_visivel, campo_real, linha, coluna
	if campo_visivel[i][j] == "[ ]":															# Abrir a célula atual (já foi feito em abrir_celula, mas reforçamos a condição aqui)
		campo_visivel[i][j] = campo_real[i][j]

	if campo_real[i][j] != "[0]":																# Se a célula atual for diferente de '0', pare a propagação a partir dela.
		return																					# Se já foi aberta e não é '0', as vizinhas não devem propagar.
	
	for dx in range(-1, 2):																		# Percorre as 8 posições vizinhas
		for dy in range(-1, 2):
			if dx == 0 and dy == 0:
				continue
			
			ni, nj = i + dx, j + dy		
			if 0 <= ni < linha and 0 <= nj < coluna:											# Verifica se a nova posição está dentro dos limites
				if campo_visivel[ni][nj] == "[ ]":												# Se a célula vizinha não estiver aberta (e não for mina)
					campo_visivel[ni][nj] = campo_real[ni][nj]									# Revela a célula vizinha (que é 0 ou número)		
					if campo_real[ni][nj] == "[0]":												# Se for um [0] em campo_real, chama a função recursivamente
						propagacao_abertura(ni, nj)												# para propagar a partir desta nova célula.

def marcar_mina(x, y):	 	
	x-=1																						#Marca ou Desmarca uma posição com mina!!
	y-=1																						#Marca ou Desmarca uma posição com mina!!
	if campo_visivel[x][y] == "[ ]":
		campo_visivel[x][y] = "[M]"																#Marca como mina

	elif campo_visivel[x][y] == "[M]":
		campo_visivel[x][y] = "[ ]"																#Desmarca 
	else:
		print("||	Essa posição já foi aberta, não pode ser marcada!!")

def verificar_vitoria(): 	
	global linha, coluna
	for i in range(linha): 																		# Itera sobre todas as células do campo
		for j in range(coluna):
			if campo_real[i][j] != "[*]":														# 1. Se a célula não é uma mina no campo real ('[*]')
				if campo_visivel[i][j] == "[ ]" or campo_visivel[i][j] == "[M]":				# 2. E se a célula visível ainda estiver fechada ('[ ]') OU marcada como mina ('[M]').
					return False 																# Neste caso, a célula segura ainda não foi revelada, então o jogo não terminou.
    # Se o loop terminar sem retornar False, significa que todas as células seguras 
    # foram reveladas. O jogador venceu.
	return True
def reiniciar_jogo():
	#Redefine todas as variáveis globais para o estado inicial.
	global linha, coluna, quantidade_minas, maximo_minas, minas_colocadas, campo_real, campo_visivel

	linha = 0
	coluna = 0
	quantidade_minas = 0
	maximo_minas = 0
	minas_colocadas = 0
	campo_real = []      
	campo_visivel = []   

	print(Fore.GREEN + "||   Jogo reiniciado com sucesso! Configure o mapa novamente." + Style.RESET_ALL)

#===============================================================================		MENU		=================================================================================
print("="*65)
print("		C A M P O  M I N A D O ")
while True:
	print("-"*65)
	try:	
		opcao_menu= int(input("||	1 - Iniciar Jogo\n||	2 - Configurações\n||	3 - Reiniciar\n||	4 - Sair\n||	Opção: "))
		print("-"*65)
		match opcao_menu:
			case 1 : 																										#Caso o usuario escolha a opçao 1, ele irá iniciar o jogo !
				if (linha == 0 and coluna == 0):																			#Verifica se o tamanho da linha e da coluna já foram definidas
					print("||  Valores da Linha e Coluna não especificados !!\n||  Por favor defina-os primeiramente!!")
					
				elif(quantidade_minas == 0):																				#Verifica se a quantidade de minas já foram definidas
					print("||  Quantidade de Minas não especificado !!\n||  Por favor defina-os primeiramente!!")
					
				else:
					print("||  Todas as Informações foram inseridas!!\n||  INICIANDO O JOGO !!")
					gerar_minas()
				
					jogo_ativo = True
					while True:
						mostrar_campo()
						try:
							opcao_jogar = int(input("||	Escolha uma ação: \n||	1 - Abrir \n||	2 - Marcar\n||	3 - Sair\n||	Opção: "))
							match opcao_jogar:
								case 1:										#ABRIR UMA POSIÇAO
									print(Fore.RED+"||	AÇÃO: ABRIR POSIÇÃO		")
									try:
										x = int(input("||	Digite a linha: "))
										y = int(input("||	Digite a coluna: "+ Style.RESET_ALL))
										if 1<= x <=linha and 1<= y<=coluna:
											abrir_celula(x,y)
											if verificar_vitoria():															#ADICIONADO -- Checa vitoria apos cada jogada
												mostrar_campo()	
												print(Fore.GREEN+"||	PARABÉNS!! VOCE VENCEU O JOGO!!!"+ Style.RESET_ALL)								
												jogo_ativo = False
												break
										else:
												print(Fore.RED + "||	Coordenadas fora do limite do campo!! "+Style.RESET_ALL)
									except ValueError:
										print(Fore.RED+"||	  Apenas Numeros inteiros sao permitidos"+Style.RESET_ALL)			
								case 2:
									print(Fore.YELLOW+"||	AÇÃO: MARCARR MINA		")
									try:
										x = int(input("||	Digite a linha: "))
										y = int(input("||	Digite a coluna: "+ Style.RESET_ALL))
										if 1<= x <=linha and 1<= y<=coluna:
											marcar_mina(x,y)
											if verificar_vitoria():								#ADICIONADO -- Checa vitoria apos cada jogada
												mostrar_campo()
												print(Fore.GREEN+"||	PARABÉNS!! VOCE VENCEU O JOGO!!!"+ Style.RESET_ALL)								
												jogo_ativo = False
												break
										else:
												print(Fore.RED + "||	Coordenadas fora do limite do campo!! "+Style.RESET_ALL)
									except ValueError:
										print(Fore.RED+"||	  Apenas Numeros inteiros sao permitidos"+Style.RESET_ALL)			
								
								case 3:
									print("||	Saindo do jogo... Até logo!!")
									jogo_ativo = False
									break
								case _:
									print(Fore.RED+"||	Opção invalida!! Escolha novamente."+Style.RESET_ALL)
						except ValueError:
							print(Fore.RED+"||	  Apenas Numeros inteiros sao permitidos"+Style.RESET_ALL)
			case 2 :	 																								#Caso o usuario escolha a opçao 2, ele irá para a area de configuraçoes, escolhendo o tamanho do mapa (Linha x Coluna) e a quantidade de Minas(limite = (Linha x Coluna)*70%)// Sendo o limite de Minas 70% da area !
				try:
					opcao_configuracao = int(input("		CONFIGURAÇÕES	\n||	1 - Escolher tamanho do mapa\n||	2 - Escolher quantidade de Minas\n||	Opção: "))
					match opcao_configuracao:
						case 1:																							# Caso o usuario escolha a opçao 1, ele será direcionado para opçao de escolha do tamanho da Linha e Coluna para formar o Mapa!!
							definir_mapa()

						case 2: 																						# Caso o usuario escolha a opçao 2, ele será direcionado para opçao de escolha da quantidade de Minas no mapa!!(limite = (Linha x Coluna)*70%)// Sendo o limite de Minas 70% da area !
							definir_minas()
						case _:
							print("||	Opçao INVALIDA!! Escolha novamente.")					
				except ValueError:
					print(Fore.RED+"||	  Apenas Numeros inteiros sao permitidos"+Style.RESET_ALL)	
			case 3:
					reiniciar_jogo()
			case 4:
				print("|| OBRIGADO POR JOGAR !!")
				print("="*65)
				quit()
			case _:
				print("||	Opçao INVALIDA!! Escolha novamente.")	
	except ValueError:
			print(Fore.RED+"||	  Apenas Numeros inteiros sao permitidos"+Style.RESET_ALL)