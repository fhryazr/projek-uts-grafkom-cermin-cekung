import pygame
import canvas


width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulasi cermin Cekung")
screen.fill((255,255,255))

ukuran_benda = 100
jarak_benda = 200
titik_fokus = 50

def display_text(layer, text, input_box, box_color):
	pygame.draw.rect(layer, box_color, input_box, 0, 20)
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

def dda(x1, y1, x2, y2, line_color):
	# Hitung selisih x dan y
	dx = x2 - x1
	dy = y2 - y1

	# Tentukan jumlah langkah yang diperlukan untuk membuat garis
	if abs(dx) > abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)

	# Hitung perubahan x dan y per langkah
	x_increment = dx / steps
	y_increment = dy / steps

	# Inisialisasi koordinat awal
	x, y = x1, y1

	# Gambar garis dengan algoritma DDA
	for i in range(steps):
		pygame.draw.rect(surface_kanvas, line_color, (x, y, 1, 1))
		x += x_increment
		y += y_increment

	# Tampilkan hasil gambar
	pygame.display.update()

# START TABLE INPUT DATA 
pygame.font.init()
input_font = pygame.font.SysFont('Century', 16)
text_color = (0, 0, 0)
box_color1 = (255,255,255)
box_color2 = (255,255,255)
box_color3 = (255,255,255)
box_color4 = (240,240,240)

#kotak input
input_box_ukuran = pygame.Rect(130,10,100,32)
input_box_jarak = pygame.Rect(130,50,100,32)
input_box_fokus = pygame.Rect(130,90,100,32)
output_box_ukuran_bayangan = pygame.Rect(130,130,100,32)
output_box_jarak_bayangan = pygame.Rect(130,170,100,32)
box_slider = pygame.Rect(0, height-50, width, 50)

#teks default
input_text_ukuran = f'{ukuran_benda}'
input_text_jarak = f'{jarak_benda}'
input_text_fokus = f'{titik_fokus}'

active1 = False
active2 = False
active3 = False
#END TABLE DATA

while True:
	obj_kanvas = canvas.Canvas(width, height)
	surface_kanvas = obj_kanvas.buatSurface(obj_kanvas, (240,255,255))

	dragging = False
	point_pos = (obj_kanvas.midPointX-jarak_benda, height-25)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		nilai_jarak_bayangan = round(jarak_bayang())
		nilai_ukuran_bayangan = round(tinggi_bayang())

		if input_text_jarak == input_text_fokus:
			output_text_ukuran_bayangan = f'INFINITY'
			output_text_jarak_bayangan = f'INFINITY'
		else:
			output_text_ukuran_bayangan = f'{nilai_ukuran_bayangan}'
			output_text_jarak_bayangan = f'{nilai_jarak_bayangan}'


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
			if pygame.draw.rect(surface_kanvas, (244, 244, 244), box_slider).collidepoint(event.pos):
				x, y = event.pos
				if x >= box_slider.left and x <= box_slider.right:
					point_pos = (x, box_slider.centery)
					jarak_benda = obj_kanvas.midPointX-x
				dragging = True
		if event.type == pygame.MOUSEBUTTONUP:
			dragging = False
		
		if event.type == pygame.MOUSEMOTION and dragging:
			x, y = event.pos
			if x >= box_slider.left and x <= box_slider.right:
				point_pos = (x, box_slider.centery)
				jarak_benda = obj_kanvas.midPointX-x
		
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
	#pembuatan objek
	#pembuatan surface

	
#START KARTESIUS
	dda(0, obj_kanvas.midPointY, obj_kanvas.panjangKanvas, obj_kanvas.midPointY, (0,0,0)) # kartesius X
	dda(obj_kanvas.midPointX, 0, obj_kanvas.midPointX, obj_kanvas.lebarKanvas, (0,0,0)) # kartesius Y

	# kartesius_x = obj_kanvas.buatGaris(surface_kanvas, (0,0,0), (0, obj_kanvas.midPointY), (obj_kanvas.panjangKanvas, obj_kanvas.midPointY))
	# kartesius_y = obj_kanvas.buatGaris(surface_kanvas, (0,0,0), (obj_kanvas.midPointX, 0), (obj_kanvas.midPointX, obj_kanvas.lebarKanvas))
	#END KARTESIUS


# START BENDA
	x1, y1 = int(obj_kanvas.midPointX-jarak_benda), int(obj_kanvas.midPointY)
	x2, y2 = int(obj_kanvas.midPointX-jarak_benda), int(obj_kanvas.midPointY-ukuran_benda)
	
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
	
	if jarak_benda > 0:
		dda(-1, y2, int(obj_kanvas.midPointX), y2 , warna_cahaya)
		dda(x2, y2, int(obj_kanvas.midPointX), int((obj_kanvas.midPointY)+tinggi_bayang()), warna_cahaya)
	else:
		dda(surface_kanvas.get_width(), y2, int(obj_kanvas.midPointX), y2 , warna_cahaya)
		dda(x2, y2, int(obj_kanvas.midPointX), int((obj_kanvas.midPointY)+tinggi_bayang()), warna_cahaya)

	# pygame.draw.line(surface_kanvas, warna_cahaya, (x2, y2), (obj_kanvas.midPointX, y2)) #1
	# pygame.draw.line(surface_kanvas, warna_cahaya, (x2, y2), (obj_kanvas.midPointX, (obj_kanvas.midPointY)+tinggi_bayang())) #2

	#END CAHAYA DATANG


#START PANTULAN CAHAYA
	warna_pantulan = (255,165,0)

	if jarak_bayang() > 0:
		dda(int(obj_kanvas.midPointX), y2, int((obj_kanvas.midPointX)-jarak_bayang()), int((obj_kanvas.midPointY)+tinggi_bayang()), warna_pantulan)
		dda(-1, int((obj_kanvas.midPointY)+tinggi_bayang()) ,int(obj_kanvas.midPointX), int((obj_kanvas.midPointY)+tinggi_bayang()), warna_pantulan)
	else:
		dda(int(obj_kanvas.midPointX), y2, int((obj_kanvas.midPointX)-jarak_bayang()), int((obj_kanvas.midPointY)+tinggi_bayang()), warna_pantulan)
		dda(int(obj_kanvas.midPointX), int((obj_kanvas.midPointY)+tinggi_bayang()), surface_kanvas.get_width(), int((obj_kanvas.midPointY)+tinggi_bayang()), warna_pantulan) #2

	# pygame.draw.line(surface_kanvas, warna_pantulan, (obj_kanvas.midPointX, y2), ((obj_kanvas.midPointX)-jarak_bayang(), (obj_kanvas.midPointY)+tinggi_bayang())) #1
	# pygame.draw.line(surface_kanvas, warna_pantulan, (obj_kanvas.midPointX, (obj_kanvas.midPointY)+tinggi_bayang()), ((obj_kanvas.midPointX)-jarak_bayang(), (obj_kanvas.midPointY)+tinggi_bayang())) #2

	#END PANTULAN CAHAYA


# START TABEL DATA
	obj_kanvas.buatTeks(surface_kanvas, "Ukuran Benda", (10,18))
	display_text(surface_kanvas, input_text_ukuran, input_box_ukuran, box_color1)
	obj_kanvas.buatTeks(surface_kanvas, "Jarak Benda", (10,58))
	display_text(surface_kanvas, input_text_jarak, input_box_jarak, box_color2)
	obj_kanvas.buatTeks(surface_kanvas, "Titik Fokus", (10,98))
	display_text(surface_kanvas, input_text_fokus, input_box_fokus, box_color3)

	obj_kanvas.buatTeks(surface_kanvas, "Ukuran Bayangan", (10,138))
	display_text(surface_kanvas, output_text_ukuran_bayangan, output_box_ukuran_bayangan, box_color4)
	obj_kanvas.buatTeks(surface_kanvas, "Jarak Bayangan", (10,178))
	display_text(surface_kanvas, output_text_jarak_bayangan, output_box_jarak_bayangan, box_color4)
	# END TABEL DATA

	#Slider
	line_start = (box_slider.left, box_slider.centery)
	line_end = (box_slider.right, box_slider.centery)
	pygame.draw.rect(surface_kanvas, (244, 244, 244), box_slider)
	pygame.draw.line(surface_kanvas, (0,0,0), line_start, line_end, 3)
	pygame.draw.circle(surface_kanvas, (200,0,0), point_pos, 5)
# OUTPUT DISPLAY
	screen.blits([(surface_kanvas, (0,0))])
	pygame.display.flip()