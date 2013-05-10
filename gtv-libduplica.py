# -*- coding: utf-8 -*-
#!/user/bin/env python

import os
import sys

"""
Coloca barra nos espacos em branco no arquivo
Como utilizar a funcao:
	Recebe um parametro que é o nome do arquivo com espacos
	Variavel vNomeArquivo

Sintax:
	colocaBarra(string:nome_do_iso)

Uso:
	colocaBarra("26_46357 PERMANECER EM DEUS PE FABIO DE MELO 080311.img")

retorna: "26_46357\ PERMANECER\ EM\ DEUS\ PE\ FABIO\ DE\ MELO\ 080311.img"
"""
def colocaBarra(vNomeArquivo): # vNomeArquivo = lnome = linhaComando.ISO
	nome = ""

	for barra in range(len(vNomeArquivo)):#
		nome = nome + vNomeArquivo[barra]
		if barra < len(vNomeArquivo) -1 :
			nome = nome + "\ "
	return nome

"""
Cria uma lista com as palavras separadas por espacos
Como usar:
	nomeIMG("Este é um teste")

retorna:
	[Este, é, um, teste]
"""
def nomeIMG(vLinha): # -> Funcao by @neviim
	return vLinha.split()[0], vLinha.split() # retira o codigo da imagem da string

"""
Grava iso em um leitor específico
Recebe por parâmetro:
	Path
	Nome do arquivo
	Gravadora
"""
def gravaISO(vPath, vNome, vGravadora):
	# comando = "cdrecord -v -dao dev=2,0,0 speed=4 -eject " + path + colocaBarra(lnome) 
	comando = "cdrecord -v -dao dev=" + str(vGravadora) + ",0,0 speed=4 -eject " + vPath + vNome
	executar = "os.system('" + comando + "')"
	#exec executar
	print executar
	
	return True

def localizaArquivo(vPath, vIdCodigo):
	diretorio = os.listdir( vPath ) # -> trazendo a lista pra dentro do programa
	lnome = []
	grava = False

	arquivo = ""
	for linha in diretorio: # -> localizar se o codigo consta em minha lista
		codigo, lnome = nomeIMG(linha)

		if vIdCodigo == codigo:
			arquivo = linha.split()
			grava = True

	return (grava, arquivo)

