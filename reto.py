import requests
import json

def nombrePokemon(url, limit):
#Función para contar los pokemones que tienen en su nombre 'at' y poseen 2 a en su nombre
	args = {'limit': '2000'}
	response = requests.get(url, params = args)
	cont = 0
	listPK = []
	
	if response.status_code == 200:
		
		payload = response.json()
		results = payload.get('results',[])
			
		if results:
    			
			for pokemon in results:
				
				cont += 1
				name = pokemon ['name']
				
				#Se verifica que el nombre contenga la subcadena 'at'			
				if 'at' in name:
					cont = 0
					#Se cuenta el numero de 'a' del nombre del pokemon				
					for characters in name:
						if characters == 'a':
							cont += 1

					if cont == 2:
						listPK.append(name)

		#Se imprime el tamaño de la lista que contiene los pokemones que cumplen las condiciones 						
		print(len(listPK))			
					

def EggGroup(url,limit):
#Función para definir con cuantás especies de pokemon puede procrear raichu
	args = {'limit': '2000'}
	response = requests.get(url2)
	cont = 0
	listapk = []
		
	if response.status_code == 200:
    	
		payload = response.json()
		eggs = payload.get('egg_groups',[])
		
		if eggs:
    		
			for i in eggs:
				response = i.get('url',[])
				payload = requests.get(response)
				groups = payload.json()

				for i in groups:
					especies = groups.get('pokemon_species',[])
					listapk.append(especies)
				
	print(len(listapk))
				

if __name__ == '__main__':
	url='https://pokeapi.co/api/v2/pokemon/'
	url2='https://pokeapi.co/api/v2/pokemon-species/raichu'
	nombrePokemon(url,2000)
	EggGroup(url2,2000)

		
		