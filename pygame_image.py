import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("projExD2023/ex01-20230613/fig/pg_bg.jpg")
    kk_img = pg.image.load("projExD2023/ex01-20230613/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img_1 = pg.transform.rotozoom(kk_img, 3.5, 1.0)
    kk_img_2 = pg.transform.rotozoom(kk_img, 7, 1.0)
    kk_img_3 = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_img_4 = pg.transform.rotozoom(kk_img, 7, 1.0)
    kk_img_5 = pg.transform.rotozoom(kk_img, 3.5, 1.0) 
    lst = [kk_img, kk_img_1, kk_img_2, kk_img_3, kk_img_4, kk_img_5]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-(tmr%3200) + 3200, 0])
        screen.blit(pg.transform.flip(bg_img, True, False),[-(tmr%3200)+1600, 0])
        screen.blit(bg_img, [-(tmr%3200), 0])
        screen.blit(lst[tmr%6], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()