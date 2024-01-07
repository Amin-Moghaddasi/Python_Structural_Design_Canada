import json
from operator import itemgetter
from math import fabs


class Analysis_Data_Load:
    def column_axial_force_P(self, file_name):
        file = open(file_name)
        data = json.load(file)
        P_values = []
        for i in data["Column_x0020_Forces"]:
            P_values.append(i["P"])
            result = [sorted(P_values)[0],sorted(P_values)[-1]]
            for j in range (len(result)):
                if result[j] < 0:
                    result[j] = result[j] * (-1)
        return sorted(result)

    def column_axial_force_T(self, file_name):
        file = open(file_name)
        data = json.load(file)
        P_values = []
        for i in data["Column_x0020_Forces"]:
            P_values.append(i["T"])
        result = [sorted(P_values)[0], sorted(P_values)[-1]]
        for j in range(len(result)):
            if result[j] < 0:
                result[j] = result[j] * (-1)
        return sorted(result)

    def column_shear_force_2(self, file_name):
        file = open(file_name)
        data = json.load(file)
        P_values = []
        for i in data["Column_x0020_Forces"]:
            P_values.append(i["V2"])
        result = [sorted(P_values)[0], sorted(P_values)[-1]]
        for j in range(len(result)):
            if result[j] < 0:
                result[j] = result[j] * (-1)
        return sorted(result)

    def column_shear_force_3(self, file_name):
        file = open(file_name)
        data = json.load(file)
        P_values = []
        for i in data["Column_x0020_Forces"]:
            P_values.append(i["V3"])
        result = [sorted(P_values)[0], sorted(P_values)[-1]]
        for j in range(len(result)):
            if result[j] < 0:
                result[j] = result[j] * (-1)
        return sorted(result)

    def column_moment_2(self, file_name):
        file = open(file_name)
        data = json.load(file)
        P_values = []
        for i in data["Column_x0020_Forces"]:
            P_values.append(i["M2"])
        result = [sorted(P_values)[0], sorted(P_values)[-1]]
        for j in range(len(result)):
            if result[j] < 0:
                result[j] = result[j] * (-1)
        return sorted(result)

    def column_moment_3(self, file_name):
        file = open(file_name)
        data = json.load(file)
        P_values = []
        for i in data["Column_x0020_Forces"]:
            P_values.append(i["M3"])
        result = [sorted(P_values)[0], sorted(P_values)[-1]]
        for j in range(len(result)):
            if result[j] < 0:
                result[j] = result[j] * (-1)
        return sorted(result)


class Sawn_Lumber:
    def section_proposal(self, M_r, V_r, Es_I, load_factor):
        file_name = 'Sawn_Lumber.json'
        file = open(file_name)
        data = json.load(file)
        counter = 0
        result = []
        for i in data["D.Fir-L"]:
            if i["M_r"] >= M_r * load_factor and i["V_r"] >= V_r * load_factor and i["Es_I"] >= Es_I:
                counter += 1
                result.append(i)
        file.close()
        return result

    def sorted_by_M_r(self, section_array):
        return sorted(section_array, key=itemgetter("M_r"))

    def sorted_by_V_r(self, section_array):
        return sorted(section_array, key=itemgetter("V_r"))

    def sorted_by_Es_I(self, section_array):
        return sorted(section_array, key=itemgetter("Es_I"))
