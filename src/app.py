import sys
import pygame as pg
from .settings import *
from .ui import *
from .graph import Graph
#Define app class and set text and colors
class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.screen = pg.display.set_mode(SIZE, 0, 32)
        self.clock = pg.time.Clock()
        # UI
        self.instructions = Button("Οδηγίες", (100, 30), (10, 10))
        self.instructions.on_click(self.show_instructions)
        self.pause = Button("Παύση", (100, 30), (790, 10), bg_color=pg.Color('lightgray'), anchor='topright')
        self.pause.on_click(self.do_pause)
        self.sett, self.inst = False, False
        self.paused = False
        # Navigation Graph
        self.graph = Graph((600, 500), (50, 150))
    #show instructions ui
    def show_instructions(self):
        self.inst = not self.inst
    #Pause and continue
    def do_pause(self):
        self.pause.set_text("Παύση" if self.paused else "Συνέχεια")
        self.paused = not self.paused
    # responsible for drawing and updating the app
    def run(self):
        while True:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                self.instructions.event(ev)
                self.pause.event(ev)
                self.graph.event(ev)
            # Draw
            self.screen.fill(BACKGROUND)
            draw_header(self.screen)
            self.graph.draw(self.screen)
            self.instructions.draw(self.screen)
            self.pause.draw(self.screen)
            if self.inst:
                draw_instructions(self.screen)
            pg.display.flip()
            # Update
            dt = self.clock.tick(FPS) / 1000.0
            if not self.paused:
                self.graph.update(dt)
