import math

class UIColor :

    # white, ghostwhite, whitesmoke
    WHITES = [[255,255,255],[248,248,255], [245,245,245]]

    # aliceblue, skyblue, royalblue
    BLUES = [[240,248,255], [135,206,235], [65,105,225]]

    # lightyellow, ?, yellow
    YELLOWS = [[255,255,224], [255,255,127], [255,255,0]]

    ORANGES = [[]]

    REDS = [[]]

    def convert(celsius):
        # Convert celsius to rgb
        
        rgb = [0,0,0]

        if celsius < 0:
            # 0 to 10 -> White
            rgb = UIColor.WHITES[int(round((celsius*2)/10))]
        elif celsius < 10:
            # Blue
            rgb = UIColor.BLUES[int(round((celsius*2)/15))]
        elif celsius < 15:
            # Yellow
            rgb = UIColor.YELLOWS[int(round((celsius*2)/20))]
        elif celsius < 20:
            # Orange
            rgb = UIColor.ORANGES[int(round((celsius*2)/40))]
        else:
            # Red
            red = UIColor.REDS[0]

        return rgb
