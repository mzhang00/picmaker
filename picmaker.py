def main():
    f = open("pic.ppm", "w")
    f.write("P3\n500 500\n255\n")
    for x in range(300):
        a = max (300 - x, 130)
        r = 6 * a/200
        g = 66 * a/200
        b = 115 * a/200
        output = ""
        for y in range(500):
            if y < 300 and y > 200 and x < 75:
                output += str(255) + " " + str(170) + " " + str(0) + " "
            else:
                output += str(r) + " " + str(g) + " " + str(b) + " "
        output += "\n"
        f.write(output)
    for x in range(200):
        a = max (x, 80)
        r = min ((238 * a/150), 238)
        g = min ((214 * a/150), 214)
        b = min ((175 * a/150), 175)
        output = ""
        for y in range(500):
            output += str(r) + " " + str(g) + " " + str(b) + " "
        output += "\n"
        f.write(output)
    f.close()

main()