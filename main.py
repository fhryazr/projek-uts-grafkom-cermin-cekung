import pygame
import canvas


width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))


ukuran_benda = 200
jarak_benda = 0
titik_fokus = 0

warna_benda = (0, 0, 0)
warna_surface = (240,255,255)
warna_garis = (0, 0, 0)
warna_teks = (0, 0, 0)
warna_teks2 = (0, 0, 0)
 
image1 = pygame.image.load('./Asset/merah-infinit.png')

def display_text(layer, text, input_box, box_color):
	pygame.draw.rect(layer, box_color, input_box, 0, 18)
	text_surface = input_font.render(text, True, warna_teks2)
	layer.blit(text_surface, (input_box.x+5, input_box.y+5))

def jarak_bayang():
	varDummy = jarak_benda
	fokusDummy = titik_fokus
	if ZeroDivisionError():
		varDummy += 0.1
		fokusDummy -= 0.1
		s = 1/(1/(fokusDummy) - 1/(varDummy))
		return s
	else:
		s = 1/(1/(titik_fokus) - 1/(jarak_benda))
		return s

def pembesaran():
	varDummy = jarak_benda
	if ZeroDivisionError():
		varDummy += 0.1
		M = jarak_bayang()/(varDummy)
		return (M)
	else:
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
		# pygame.draw.rect(surface_kanvas, line_color, (x, y, 1, 1))
		surface_kanvas.set_at((int(round(x)),int(round(y))), line_color)
		x += x_increment
		y += y_increment

	# Tampilkan hasil gambar
	pygame.display.update()

def dda_MODIF(x1, y1, x2, y2, line_color):
	# Hitung selisih x dan y
	dx = x2 - x1
	dy = y2 - y1

	# Tentukan jumlah langkah yang diperlukan untuk membuat garis
	if abs(dx) > abs(dy):
		if abs(dx) == 0:
			steps = 1
		else:
			steps = abs(dx)
	else:
		if abs(dy) == 0:
			steps = -1
		else:
			steps = abs(dy)

	# Hitung perubahan x dan y per langkah
	x_increment = dx / steps
	y_increment = dy / steps

	# Inisialisasi koordinat awal
	x, y = x1, y1
	steps += 9999

	# Gambar garis dengan algoritma DDA
	for i in range(steps):
		pygame.draw.rect(surface_kanvas, line_color, (x, y, 1, 1))
		# surface_kanvas.set_at((int(round(x)),int(round(y))), line_color)
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
box_color4 = (210,210,210)

#kotak input
input_box_ukuran = pygame.Rect(130,10,100,32)
input_box_jarak = pygame.Rect(130,50,100,32)
input_box_fokus = pygame.Rect(130,90,100,32)
output_box_ukuran_bayangan = pygame.Rect(130,130,100,32)
output_box_jarak_bayangan = pygame.Rect(130,170,100,32)
box_slider = pygame.Rect(0, height-50, width, 50)
box_slider2 = pygame.Rect(width-25, 0, 25, height-50)
box_theme = pygame.Rect(width-70,20,25,25)

#teks default
input_text_ukuran = f'{ukuran_benda}'
input_text_jarak = f'{jarak_benda}'
input_text_fokus = f'{titik_fokus}'

active1 = False
active2 = False
active3 = False
dragging_jarak = False
dragging_fokus = False
dragging_ukuran = False
theme = False
#END TABLE DATA


while True:
	# Kanvas
	obj_kanvas = canvas.Canvas(width, height) #pembuatan objek
	surface_kanvas = obj_kanvas.buatSurface(obj_kanvas, warna_surface)#pembuatan surface

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		nilai_jarak_bayangan = round(jarak_bayang())
		nilai_ukuran_bayangan = round(tinggi_bayang())

		if input_text_jarak == input_text_fokus:
			output_text_ukuran_bayangan = f''
			output_text_jarak_bayangan = f''
		else:
			output_text_ukuran_bayangan = f'{nilai_ukuran_bayangan}'
			output_text_jarak_bayangan = f'{nilai_jarak_bayangan}'

		if event.type == pygame.MOUSEBUTTONDOWN:
			if input_box_ukuran.collidepoint(event.pos):
				active1 = True
			else:
				active1 = False
				newUkuran = int(input_text_ukuran)
				ukuran_benda = newUkuran
			if input_box_jarak.collidepoint(event.pos):
				active2 = True
			else:
				active2 = False
			if input_box_fokus.collidepoint(event.pos):
				active3 = True
			else:
				active3 = False

			if pygame.draw.rect(surface_kanvas, warna_benda, box_theme, 0, 10).collidepoint(event.pos):
				if theme:
					theme = False
				else:
					theme = True
					
			if pygame.draw.line(surface_kanvas, (0,0,0), (line_start[0], line_start[1]+13), (line_end[0], line_end[1]+13), 3).collidepoint(event.pos):
				x, y = event.pos
				if x >= box_slider.left and x <= box_slider.right:
					jarak_benda = int(obj_kanvas.midPointX-x)
					input_text_jarak = f'{jarak_benda}'
				dragging_jarak = True

			if pygame.draw.line(surface_kanvas, (0,0,0), (line_start[0], line_start[1]-13), (line_end[0], line_end[1]-13), 3).collidepoint(event.pos):
				x, y = event.pos
				if x >= box_slider.left and x <= box_slider.right:
					titik_fokus = int(obj_kanvas.midPointX-x)
					input_text_fokus = f'{titik_fokus}'
				dragging_fokus = True

			if pygame.draw.line(surface_kanvas, (0,0,0), line_start_ukuran, line_end_ukuran, 3).collidepoint(event.pos):
				x, y = event.pos
				if y >= box_slider2.top and y <= box_slider2.bottom-10:
					ukuran_benda = int(obj_kanvas.midPointY-y)
					input_text_ukuran = f'{ukuran_benda}'
				dragging_ukuran = True

		if event.type == pygame.MOUSEBUTTONUP:
			dragging_fokus, dragging_jarak, dragging_ukuran =False, False, False
			

		if event.type == pygame.MOUSEMOTION:
			if dragging_jarak:
				x, y = event.pos
				if x >= box_slider.left and x <= box_slider.right:
					jarak_benda = int(obj_kanvas.midPointX-x)
					input_text_jarak = f'{jarak_benda}'
			if dragging_fokus:
				x, y = event.pos
				if x >= box_slider.left and x <= box_slider.right:
					titik_fokus = int(obj_kanvas.midPointX-x)
					input_text_fokus = f'{titik_fokus}'
			if dragging_ukuran:
				x, y = event.pos
				if y >= box_slider2.top and y <= box_slider2.bottom-10:
					ukuran_benda = int(obj_kanvas.midPointY-y)
					input_text_ukuran = f'{ukuran_benda}'

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

	
	
#START KARTESIUS
	dda(0, obj_kanvas.midPointY, obj_kanvas.panjangKanvas, obj_kanvas.midPointY, warna_garis) # kartesius X
	dda(obj_kanvas.midPointX, 0, obj_kanvas.midPointX, obj_kanvas.lebarKanvas, warna_garis) # kartesius Y
#END KARTESIUS


# START BENDA
	x1, y1 = int(obj_kanvas.midPointX-jarak_benda), int(obj_kanvas.midPointY)
	x2, y2 = int(obj_kanvas.midPointX-jarak_benda), int(obj_kanvas.midPointY-ukuran_benda)
	
	r = titik_fokus*2
	f = r+titik_fokus

	#benda Pensil
	pygame.draw.line(surface_kanvas, warna_benda, (x2, y2), (x2+int(ukuran_benda/5), y2+int(ukuran_benda/5)))
	pygame.draw.line(surface_kanvas, warna_benda,(x2, y2), (x2-int(ukuran_benda/5), y2+int(ukuran_benda/5)))

	pygame.draw.line(surface_kanvas, warna_benda,(x2+int(ukuran_benda/5), y2+int(ukuran_benda/5)), (x2+int(ukuran_benda/5), y1-int(ukuran_benda/30)))
	pygame.draw.line(surface_kanvas, warna_benda,(x2-int(ukuran_benda/5), y2+int(ukuran_benda/5)), (x2-int(ukuran_benda/5), y1-int(ukuran_benda/30)))

	pygame.draw.line(surface_kanvas, warna_benda,(x2+int(ukuran_benda/5), y1-int(ukuran_benda/30)), (x2+int(ukuran_benda/12), y1))
	pygame.draw.line(surface_kanvas, warna_benda,(x2-int(ukuran_benda/5), y1-int(ukuran_benda/30)), (x2-int(ukuran_benda/12), y1))

	pygame.draw.line(surface_kanvas, warna_benda,(x2+int(ukuran_benda/5), y2+int(ukuran_benda/5)), (x2+int(ukuran_benda/12), y2+int(ukuran_benda/4)))
	pygame.draw.line(surface_kanvas, warna_benda,(x2-int(ukuran_benda/5), y2+int(ukuran_benda/5)), (x2-int(ukuran_benda/12), y2+int(ukuran_benda/4)))

	pygame.draw.line(surface_kanvas, warna_benda,(x2+int(ukuran_benda/12), y2+int(ukuran_benda/4)), (x2+int(ukuran_benda/12), y1))
	pygame.draw.line(surface_kanvas, warna_benda,(x2-int(ukuran_benda/12), y2+int(ukuran_benda/4)), (x2-int(ukuran_benda/12), y1))
	
	pygame.draw.line(surface_kanvas, warna_benda,(x2+int(ukuran_benda/12), y2+int(ukuran_benda/4)), (x2-int(ukuran_benda/12), y2+int(ukuran_benda/4)))
	pygame.draw.line(surface_kanvas, warna_benda,(x2+int(ukuran_benda/12), y1), (x2-int(ukuran_benda/12), y1))
	# END BENDA

#titik F
	obj_kanvas.buatTeks(surface_kanvas, 'f', (obj_kanvas.midPointX-titik_fokus-2, obj_kanvas.midPointY-20), warna_teks) #teks
	pygame.draw.circle(surface_kanvas, (255, 0, 0), (obj_kanvas.midPointX - titik_fokus, obj_kanvas.midPointY), 2) #titik

	obj_kanvas.buatTeks(surface_kanvas, 'f', (obj_kanvas.midPointX+titik_fokus-2, obj_kanvas.midPointY-20), warna_teks) #teks
	pygame.draw.circle(surface_kanvas, (255, 0, 0), (obj_kanvas.midPointX + titik_fokus, obj_kanvas.midPointY), 2) #titik

#titik R
	obj_kanvas.buatTeks(surface_kanvas, 'r', (obj_kanvas.midPointX-r-2, obj_kanvas.midPointY-20), warna_teks) #teks
	pygame.draw.circle(surface_kanvas, (255, 0, 0), (obj_kanvas.midPointX - r, obj_kanvas.midPointY), 2) #titik

	obj_kanvas.buatTeks(surface_kanvas, 'r', (obj_kanvas.midPointX + r-2, obj_kanvas.midPointY-20), warna_teks) #teks
	pygame.draw.circle(surface_kanvas, (255, 0, 0), (obj_kanvas.midPointX + r, obj_kanvas.midPointY), 2) #titik


#START CAHAYA DATANG
	warna_cahaya = (30, 144, 255)
	
	if jarak_benda > 0:
		dda(-1, y2, int(obj_kanvas.midPointX), y2 , warna_cahaya)
		dda_MODIF(int(obj_kanvas.midPointX), int((obj_kanvas.midPointY)+tinggi_bayang()), x2, y2,  warna_cahaya)
	else:
		dda(surface_kanvas.get_width(), y2, int(obj_kanvas.midPointX), y2 , warna_cahaya)
		dda_MODIF(int(obj_kanvas.midPointX), int((obj_kanvas.midPointY)+tinggi_bayang()), x2, y2,  warna_cahaya)

	#END CAHAYA DATANG


#START PANTULAN CAHAYA
	warna_pantulan = (255,165,0)

	if jarak_bayang() > 0:
		dda(-1, int((obj_kanvas.midPointY)+tinggi_bayang()) ,int(obj_kanvas.midPointX), int((obj_kanvas.midPointY)+tinggi_bayang()), warna_pantulan)
		dda_MODIF(int(obj_kanvas.midPointX), y2, int((obj_kanvas.midPointX)-jarak_bayang()), int((obj_kanvas.midPointY)+tinggi_bayang()), warna_pantulan)
	else:
		dda(int(obj_kanvas.midPointX), int((obj_kanvas.midPointY)+tinggi_bayang()), surface_kanvas.get_width(), int((obj_kanvas.midPointY)+tinggi_bayang()), warna_pantulan)
		dda_MODIF(int(obj_kanvas.midPointX), y2, int((obj_kanvas.midPointX)-jarak_bayang()), int((obj_kanvas.midPointY)+tinggi_bayang()), warna_pantulan)
	#END PANTULAN CAHAYA

#START BAYANGAN
	x1, y1 = int(obj_kanvas.midPointX-jarak_bayang()), int(obj_kanvas.midPointY)
	x2, y2 = int(obj_kanvas.midPointX-jarak_bayang()), int(obj_kanvas.midPointY+tinggi_bayang())

	#Bayangan benda Pensil
	pygame.draw.line(surface_kanvas, warna_benda, (x2,y2), (x2+int(tinggi_bayang()/5), y2-int(tinggi_bayang()/5)))
	pygame.draw.line(surface_kanvas, warna_benda, (x2,y2), (x2-int(tinggi_bayang()/5), y2-int(tinggi_bayang()/5)))

	pygame.draw.line(surface_kanvas, warna_benda, (x2+int(tinggi_bayang()/5), y2-int(tinggi_bayang()/5)), (x2+int(tinggi_bayang()/5), y1+int(tinggi_bayang()/30)))
	pygame.draw.line(surface_kanvas, warna_benda, (x2-int(tinggi_bayang()/5), y2-int(tinggi_bayang()/5)), (x2-int(tinggi_bayang()/5), y1+int(tinggi_bayang()/30)))

	pygame.draw.line(surface_kanvas, warna_benda, (x2+int(tinggi_bayang()/5), y1+int(tinggi_bayang()/30)), (x2+int(tinggi_bayang()/12), y1))
	pygame.draw.line(surface_kanvas, warna_benda, (x2-int(tinggi_bayang()/5), y1+int(tinggi_bayang()/30)), (x2-int(tinggi_bayang()/12), y1))

	pygame.draw.line(surface_kanvas, warna_benda, (x2+int(tinggi_bayang()/5), y2-int(tinggi_bayang()/5)), (x2+int(tinggi_bayang()/12), y2-int(tinggi_bayang()/4)))
	pygame.draw.line(surface_kanvas, warna_benda, (x2-int(tinggi_bayang()/5), y2-int(tinggi_bayang()/5)), (x2-int(tinggi_bayang()/12), y2-int(tinggi_bayang()/4)))

	pygame.draw.line(surface_kanvas, warna_benda, (x2+int(tinggi_bayang()/12), y2-int(tinggi_bayang()/4)), (x2+int(tinggi_bayang()/12), y1))
	pygame.draw.line(surface_kanvas, warna_benda, (x2-int(tinggi_bayang()/12), y2-int(tinggi_bayang()/4)), (x2-int(tinggi_bayang()/12), y1))
	
	pygame.draw.line(surface_kanvas, warna_benda, (x2+int(tinggi_bayang()/12), y2-int(tinggi_bayang()/4)),(x2-int(tinggi_bayang()/12), y2-int(tinggi_bayang()/4)))
	pygame.draw.line(surface_kanvas, warna_benda, (x2+int(tinggi_bayang()/12), y1), (x2-int(tinggi_bayang()/12), y1))
	#END BAYANGAN


# START TABEL DATA
	obj_kanvas.buatTeks(surface_kanvas, "Ukuran Benda", (10,18), warna_teks)
	display_text(surface_kanvas, input_text_ukuran, input_box_ukuran, box_color1)
	obj_kanvas.buatTeks(surface_kanvas, "Jarak Benda", (10,58), warna_teks)
	display_text(surface_kanvas, input_text_jarak, input_box_jarak, box_color2)
	obj_kanvas.buatTeks(surface_kanvas, "Titik Fokus", (10,98), warna_teks)
	display_text(surface_kanvas, input_text_fokus, input_box_fokus, box_color3)
	obj_kanvas.buatTeks(surface_kanvas, "Ukuran Bayangan", (10,138), warna_teks)
	display_text(surface_kanvas, output_text_ukuran_bayangan, output_box_ukuran_bayangan, box_color4)
	obj_kanvas.buatTeks(surface_kanvas, "Jarak Bayangan", (10,178), warna_teks)
	display_text(surface_kanvas, output_text_jarak_bayangan, output_box_jarak_bayangan, box_color4)
	# END TABEL DATA
	pygame.draw.rect(surface_kanvas, box_color4, output_box_jarak_bayangan, 0, 20)
	pygame.draw.rect(surface_kanvas, box_color4, output_box_ukuran_bayangan, 0, 20)
	if input_text_jarak == input_text_fokus:
		image = [surface_kanvas.blit(image1, (150,130)),
				surface_kanvas.blit(image1, (150,170))]
	else:
		display_text(surface_kanvas, output_text_jarak_bayangan, output_box_jarak_bayangan, box_color4)
		display_text(surface_kanvas, output_text_ukuran_bayangan, output_box_ukuran_bayangan, box_color4)

	#Slider
	line_start = (box_slider.left, box_slider.centery)
	line_end = (box_slider.right, box_slider.centery)
	pygame.draw.rect(surface_kanvas, (244, 244, 244), box_slider)
	pygame.draw.rect(surface_kanvas, (244, 244, 244), box_slider2)

	#Slider jarak
	pygame.draw.line(surface_kanvas, (0,0,0), (line_start[0], line_start[1]+13), (line_end[0], line_end[1]+13), 3)
	pygame.draw.circle(surface_kanvas, (200,0,0), (obj_kanvas.midPointX-jarak_benda, box_slider.centery+13), 5)

	#slider fokus
	pygame.draw.line(surface_kanvas, (0,0,0), (line_start[0], line_start[1]-13), (line_end[0], line_end[1]-13), 3)
	pygame.draw.circle(surface_kanvas, (200,0,0), (obj_kanvas.midPointX - titik_fokus, box_slider.centery-13), 5)

	#slider ukuran
	line_start_ukuran = (box_slider2.centerx, box_slider2.top)
	line_end_ukuran = (box_slider2.centerx, box_slider2.bottom-10)
	
	pygame.draw.line(surface_kanvas, (0,0,0), line_start_ukuran, line_end_ukuran, 3)
	pygame.draw.circle(surface_kanvas, (200,0,0), (box_slider2.centerx, obj_kanvas.midPointY - ukuran_benda), 5)

	#theme box
	pygame.draw.rect(surface_kanvas, warna_benda, box_theme, 0, 10)
	if theme:
		warna_benda, warna_garis, warna_teks = (255,255,255), (255,255,255), (255, 255, 255)
		warna_surface = (30, 30, 30)
		
		box_color1 = (150, 150, 150)
		box_color2 = (150, 150, 150)
		box_color3 = (150, 150, 150)
		box_color4 = (90, 90, 90)
		if active1:
			box_color1 = (50, 50, 50)
			warna_teks2 = (0, 0, 0)
		if active2:
			box_color2 = (50, 50, 50)
			warna_teks2 = (0, 0, 0)
		if active3:
			box_color3 = (50, 50, 50)
			warna_teks2 = (0, 0, 0)
	else:
		warna_benda, warna_garis, warna_teks = (0, 0, 0), (0, 0, 0), (0, 0, 0)
		warna_surface = (240, 255, 255)

		box_color1 = (255,255,255)
		box_color2 = (255,255,255)
		box_color3 = (255,255,255)
		box_color4 = (240, 240, 240)
		if active1:
			box_color1 = (240, 240, 240)
		if active2:
			box_color2 = (240, 240, 240)
		if active3:
			box_color3 = (240, 240, 240)

# OUTPUT DISPLAY
	screen.blits([(surface_kanvas, (0,0))])
	pygame.display.flip()

