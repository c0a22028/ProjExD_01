import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("projExD2023/ex01-20230613/fig/pg_bg.jpg")
    kk_img = pg.image.load("projExD2023/ex01-20230613/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    lst = [bg_img, kk_img]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(lst[0], [0, 0])
        screen.blit(lst[1], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()