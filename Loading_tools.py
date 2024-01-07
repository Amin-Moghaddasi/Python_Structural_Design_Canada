from math import pow
from math import e


class Loading_tools:
    def snow(self, I_s, S_s, C_b, C_w, C_s, C_a, S_r):
        """
        :param I_s: importance factor for snow load, as provided in Table 4.1.6.2.-A
        :param S_s: 1-in-50-year ground snow load, in kPa, determined in accordance with Subsection 1.1.3.
        :param C_b: basic roof snow load factor in Sentence (2)
        :param C_w: wind exposure factor in Sentences (3) and (4)
        :param C_s:  slope factor in Sentences (5) to (7)
        :param C_a:  accumulation factor in Sentence (8)
        :param S_r:1-in-50-year associated rain load, in kPa, determined in accordance with Subsection 1.1.3., but not greater than Ss(Cb Cw Cs Ca)
        :return: Returns snow load
        """
        return I_s * ((S_s * C_b * C_a * C_w * C_s) + S_r)

    def l_c(self, w, l):
        """
        :param w: smaller plan dimension (roof)
        :param l: larger plan dimension (roof)
        :return: characteristic length of the upper or lower roof
        """
        return (2 * w) - ((pow(w, 2)) / l)

    def C_b(self, lc, C_w):
        """

        :param lc: characteristic length of the upper or lower roof
        :param C_w: wind exposure factor in Sentences (3) and (4)
        :return: basic roof snow load factor in Sentence (2)
        """
        if lc <= (70 / (pow(C_w, 2))):
            C_b = 0.8
        else:
            C_b = (1 - (1 - (0.8 * C_w * pow(e, ((70 - lc * pow(C_w, 2)) / 100)))))
        return C_b
    def Cs(self, Ice_slide_off, roof_angle):
        """

        :param Ice_slide_off: True or False
        :param roof_angle: roof angle
        :return: slope factor in Sentences (5) to (7)
        """
        if Ice_slide_off == True:
            if roof_angle <= 15:
                C_s = 1
            elif roof_angle > 15 and roof_angle <= 60:
                C_s = (60 - roof_angle) / 45
            elif roof_angle > 60:
                C_s = 0
        else:
            if roof_angle <= 30:
                C_s = 1
            elif roof_angle > 30 and roof_angle <= 70:
                C_s = (70 - roof_angle) / 40
            elif roof_angle > 70:
                C_s = 0
        return C_s
