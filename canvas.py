import pygame

class Canvas:
	def __init__(self, panjangKanvas, lebarKanvas):
		self.panjangKanvas = panjangKanvas
		self.lebarKanvas = lebarKanvas
		self.midPointX = panjangKanvas/2
		self.midPointY = lebarKanvas/2


	def buatSurface(self, surface, color):
		surface = pygame.Surface((self.panjangKanvas, self.lebarKanvas))
		pygame.Surface.fill(surface, color)
		return surface
		
	def buatGaris(self, surface, color, start_pos, end_pos):
		pygame.draw.line(surface, color, start_pos, end_pos)

	def buatTeks(self, layer, text, posisi, color):
		my_font = pygame.font.SysFont("Calibri", 16)
		teks = my_font.render(text, True, color)
		layer.blit(teks, posisi)




