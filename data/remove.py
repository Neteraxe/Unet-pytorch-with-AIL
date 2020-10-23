import os


b = False
def remove_d(i1, m2):
    for i in i1:
        if (i == "."):
            continue
        for m in m2:
            if (i == m):
                b = True
                break
        if not b:
            print(os.remove(os.getcwd()+"\imgs\\" + i + ".jpg"))
                

imgs = os.listdir(os.getcwd()+"\imgs")
i1 = list(imgs)
i1 = [a[:-4] for a in i1]

masks=os.listdir(os.getcwd()+"\masks")
m2 = list(masks)
m2 = [b[:-9] for b in m2]

remove_d(i1, m2)

