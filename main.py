import pygame
import canvas


width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))

ukuran_benda = 100
jarak_benda = 200
titik_fokus = 50

# START TABLE INPUT DATA 
pygame.font.init()
input_font = pygame.font.SysFont('Century', 16)
text_color = (0, 0, 0)
box_color1 = (255,255,255)
box_color2 = (255,255,255)
box_color3 = (255,255,255)

#kotak input
input_box_ukuran = pygame.Rect(120,10,100,32)
input_box_jarak = pygame.Rect(120,50,100,32)
input_box_fokus = pygame.Rect(120,90,100,32)

#teks default
input_text_ukuran = f'{ukuran_benda}'
input_text_jarak = f'{jarak_benda}'
input_text_fokus = f'{titik_fokus}'

active1 = False
active2 = False
active3 = False
#END TABLE DATA

def display_text(layer, text, input_box, box_color):
	pygame.draw.rect(layer, box_color, input_box)
	text_surface = input_font.render(text, True, (0))
	layer.blit(text_surface, (input_box.x+5, input_box.y+5))

def jarak_bayang():
	varDummy = jarak_benda
	if varDummy-titik_fokus == 0:
		varDummy -= 0.1
		s = 1/(1/(titik_fokus) - 1/(varDummy))
		return s
	else:
		s = 1/(1/(titik_fokus) - 1/(jarak_benda))
		return s

def pembesaran():
	M = jarak_bayang()/(jarak_benda)
	return (M)

def tinggi_bayang():
    tinggi_bayang = pembesaran()*(ukuran_benda)
    return tinggi_bayang

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
			
		# if event.type == pygame.KEYDOWN:
		# 	if event.key == pygame.K_BACKSPACE:
		# 		# Hapus karakter terakhir dari teks input jika tombol backspace ditekan
		# 		input_ukuran_benda_text = input_ukuran_benda_text[:-1]
		# 	elif event.key == pygame.K_RETURN:
		# 		# Proses teks input jika tombol enter ditekan
		# 		newUkuranBenda = int(input_ukuran_benda_text)
		# 		ukuran_benda = newUkuranBenda
		# 	else:
		# 		# Tambahkan karakter ke teks input jika tombol lainnya ditekan
		# 		input_ukuran_benda_text += event.unicode

		if event.type == pygame.MOUSEBUTTONDOWN:
			if input_box_ukuran.collidepoint(event.pos):
				active1 = True
				box_color1 = (240,240,240)
			else:
				active1 = False
				box_color1 = (255,255,255)
			if input_box_jarak.collidepoint(event.pos):
				active2 = True
				box_color2 = (240,240,240)
			else:
				active2 = False
				box_color2 = (255,255,255)
			if input_box_fokus.collidepoint(event.pos):
				active3 = True
				box_color3 = (240,240,240)
			else:
				active3 = False
				box_color3 = (255,255,255)
		
		if event.type == pygame.KEYDOWN:
			if active1:
				if event.key == pygame.K_BACKSPACE:
					input_text_ukuran = input_text_ukuran[:-1]
				elif event.key == pygame.K_RETURN:
					newUkuran = int(input_text_ukuran)
					ukuran_benda = newUkuran
					box_color1 = (255,255,255)
				elif event.key == pygame.K_UP:
					input_text_ukuran = f'{ukuran_benda+1}'
					newUkuran = int(input_text_ukuran)
					ukuran_benda = newUkuran
				elif event.key == pygame.K_DOWN:
					input_text_ukuran = f'{ukuran_benda-1}'
					newUkuran = int(input_text_ukuran)
					ukuran_benda = newUkuran
				else:
					input_text_ukuran += event.unicode

			if active2:
				if event.key == pygame.K_BACKSPACE:
					input_text_jarak = input_text_jarak[:-1]
				elif event.key == pygame.K_RETURN:
					newJarak = int(input_text_jarak)
					jarak_benda = newJarak
					box_color2 = (255,255,255)
				elif event.key == pygame.K_UP:
					input_text_jarak = f'{jarak_benda+1}'
					newJarak = int(input_text_jarak)
					jarak_benda = newJarak
				elif event.key == pygame.K_DOWN:
					input_text_jarak = f'{jarak_benda-1}'
					newJarak = int(input_text_jarak)
					jarak_benda = newJarak	
				else:
					input_text_jarak += event.unicode

			if active3:
				if event.key == pygame.K_BACKSPACE:
					input_text_fokus = input_text_fokus[:-1]
				elif event.key == pygame.K_RETURN:
					newFokus = int(input_text_fokus)
					titik_fokus = newFokus
					box_color3 = (255,255,255)
				elif event.key == pygame.K_UP:
					input_text_fokus = f'{titik_fokus+1}'
					newFokus = int(input_text_fokus)
					titik_fokus = newFokus
				elif event.key == pygame.K_DOWN:
					input_text_fokus = f'{titik_fokus-1}'
					newFokus = int(input_text_fokus)
					titik_fokus = newFokus
				else:
					input_text_fokus += event.unicode

	# Kanvas
	obj_kanvas = canvas.Canvas(1280, 600) #pembuatan objek
	surface_kanvas = obj_kanvas.buatSurface(obj_kanvas, (240,255,255))#pembuatan surface

	
	#START KARTESIUS
	kartesius_x = obj_kanvas.buatGaris(surface_kanvas, (0,0,0), (0, obj_kanvas.midPointY), (obj_kanvas.panjangKanvas, obj_kanvas.midPointY))

	kartesius_y = obj_kanvas.buatGaris(surface_kanvas, (0,0,0), (obj_kanvas.midPointX, 0), (obj_kanvas.midPointX, obj_kanvas.lebarKanvas))
	#END KARTESIUS


	# START BENDA
	x1, y1 = obj_kanvas.midPointX-jarak_benda, obj_kanvas.midPointY
	x2, y2 = obj_kanvas.midPointX-jarak_benda, obj_kanvas.midPointY-ukuran_benda
	
	r = titik_fokus*2
	f = r+titik_fokus

	pygame.draw.line(surface_kanvas, (0,255,0), (x1,y1), (x2,y2))
	# END BENDA

	#titik F
	obj_kanvas.buatTeks(surface_kanvas, 'f', (obj_kanvas.midPointX-titik_fokus-2, obj_kanvas.midPointY-20)) #teks
	pygame.draw.circle(surface_kanvas, (0), (obj_kanvas.midPointX - titik_fokus, obj_kanvas.midPointY), 2) #titik

	#titik R
	obj_kanvas.buatTeks(surface_kanvas, 'r', (obj_kanvas.midPointX-r-2, obj_kanvas.midPointY-20)) #teks
	pygame.draw.circle(surface_kanvas, (0), (obj_kanvas.midPointX - r, obj_kanvas.midPointY), 2) #titik

	#START BAYANGAN
	pygame.draw.line(surface_kanvas, (0,255,0), ((obj_kanvas.midPointX)-jarak_bayang(), obj_kanvas.midPointY),((obj_kanvas.midPointX)-jarak_bayang(), (obj_kanvas.midPointY)+tinggi_bayang()))
	#END BAYANGAN


	#START CAHAYA DATANG
	warna_cahaya = (0,0,255)
	
	pygame.draw.line(surface_kanvas, warna_cahaya, (x2, y2), (obj_kanvas.midPointX, y2)) #1

	pygame.draw.line(surface_kanvas, warna_cahaya, (x2, y2), (obj_kanvas.midPointX, (obj_kanvas.midPointY)+tinggi_bayang())) #2
	#END CAHAYA DATANG


	#START PANTULAN CAHAYA
	warna_pantulan = (255,165,0)

	pygame.draw.line(surface_kanvas, warna_pantulan, (obj_kanvas.midPointX, y2), ((obj_kanvas.midPointX)-jarak_bayang(), (obj_kanvas.midPointY)+tinggi_bayang())) #1

	pygame.draw.line(surface_kanvas, warna_pantulan, (obj_kanvas.midPointX, (obj_kanvas.midPointY)+tinggi_bayang()), ((obj_kanvas.midPointX)-jarak_bayang(), (obj_kanvas.midPointY)+tinggi_bayang())) #2
	#END PANTULAN CAHAYA


	# START TABEL DATA
	obj_kanvas.buatTeks(surface_kanvas, "Ukuran Benda", (10,18))
	display_text(surface_kanvas, input_text_ukuran, input_box_ukuran, box_color1)
	obj_kanvas.buatTeks(surface_kanvas, "Jarak Benda", (10,58))
	display_text(surface_kanvas, input_text_jarak, input_box_jarak, box_color2)
	obj_kanvas.buatTeks(surface_kanvas, "Titik Fokus", (10,98))
	display_text(surface_kanvas, input_text_fokus, input_box_fokus, box_color3)
	# END TABEL DATA

	# OUTPUT DISPLAY
	screen.blits([(surface_kanvas, (0,0))])
	pygame.display.flip()

