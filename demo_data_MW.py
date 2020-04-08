#######################################
### Demo Data for Microwave Thellier###
#######################################

# here is the full data set, and a custom made selection
# MNSAMS-106B selection is from step 3 to 10 (including check)
# MNSAMS-106C selection is from step 3 to 8 (including check)

_data_MNSAMS106B = [
    ["MNSAMS", "106B", -2.33E+00, -6.12E+00, 2.87E+00, 0.99, 200.8427777, 23.66620583, 7.149839159, "02/05/2015", "15:33:39", 0, 0, 0, 0, 0, 0],
    ["MNSAMS", "106B", -2.40E+00, -6.05E+00, 1.22E+00, 0.99, 201.6379412, 10.61649584, 6.622001208, "02/05/2015", "15:33:39", 0, 0, 0, 0, 1, 0],
    ["MNSAMS", "106B", -2.43E+00, -5.80E+00, 1.59E+00, 0.99, 202.7320033, 14.18948039, 6.486370326, "02/05/2015", "15:33:39", 10, 248, 90, 1, 1, 1],
    ["MNSAMS", "106B", -2.85E+00, -4.43E+00, 1.23E+00, 0.99, 212.7548324, 13.14328501, 5.409279065, "02/05/2015", "15:33:39", 10, 248, 90, 1, 2, 1],
    ["MNSAMS", "106B", -3.20E+00, -3.80E+00, 1.78E-01, 0.99, 220.1009075, 2.052032866, 4.971084791, "02/05/2015", "15:33:39", 0, 0, 0, 0, 2, 2],
    ["MNSAMS", "106B", -3.16E+00, -3.69E+00, 6.16E-01, 0.99, 220.5757105, 7.226371832, 4.89705585, "02/05/2015", "15:33:39", 10, 248, 90, 2, 1, 2],
    ["MNSAMS", "106B", -3.03E+00, -3.01E+00, -2.21E-01, 0.99, 225.1897204, -2.962125261, 4.276662367, "02/05/2015", "15:33:39", 0, 0, 0, 0, 3, 1],
    ["MNSAMS", "106B", -3.06E+00, -3.38E+00, 6.77E-01, 0.99, 222.1553444, 8.445848637, 4.609374036, "02/05/2015", "15:33:39", 10, 248, 90, 1, 3, 3],
    ["MNSAMS", "106B", -3.15E+00, -3.18E+00, 9.65E-01, 0.99, 224.7284581, 12.16632611, 4.578878138, "02/05/2015", "15:33:39", 10, 248, 90, 1, 4, 3],
    ["MNSAMS", "106B", -3.17E+00, -3.22E+00, -6.05E-02, 0.99, 224.5516854, -0.767101623, 4.518955659, "02/05/2015", "15:33:39", 0, 0, 0, 0, 4, 4],
    ["MNSAMS", "106B", -3.19E+00, -3.26E+00, 4.88E-01, 0.99, 224.3782097, 6.106933278, 4.587138978, "02/05/2015", "15:33:39", 10, 248, 90, 2, 2, 4],
    ["MNSAMS", "106B", -3.24E+00, -3.44E+00, -3.14E-01, 0.99, 223.2850698, -3.801529005, 4.736010557, "02/05/2015", "15:33:39", 0, 0, 0, 0, 5, 2],
    ["MNSAMS", "106B", -3.18E+00, -3.34E+00, 7.16E-01, 0.99, 223.5942507, 8.825082099, 4.666975037, "02/05/2015", "15:33:39", 10, 248, 90, 1, 5, 5],
    ["MNSAMS", "106B", -2.96E+00, -3.20E+00, 1.03E+00, 0.99, 222.7688254, 13.29447987, 4.479118217, "02/05/2015", "15:33:39", 10, 248, 90, 1, 6, 5],
    ["MNSAMS", "106B", -3.05E+00, -3.24E+00, -1.39E-01, 0.99, 223.269811, -1.789215033, 4.45190083, "02/05/2015", "15:33:39", 0, 0, 0, 0, 6, 6],
    ["MNSAMS", "106B", -3.24E+00, -3.19E+00, 2.75E-01, 0.99, 225.4455259, 3.461126758, 4.555142698, "02/05/2015", "15:33:39", 10, 248, 90, 2, 4, 6],
    ["MNSAMS", "106B", -3.11E+00, -2.28E+00, -4.27E-01, 0.99, 233.75415, -6.318618041, 3.879797546, "02/05/2015", "15:33:39", 0, 0, 0, 0, 7, 4],
    ["MNSAMS", "106B", -3.22E+00, -2.37E+00, 1.11E+00, 0.99, 233.6460084, 15.51612062, 4.149385497, "02/05/2015", "15:33:39", 10, 248, 90, 1, 7, 7],
    ["MNSAMS", "106B", -2.88E+00, -1.86E+00, 1.35E+00, 0.99, 237.144278, 21.49295565, 3.684630239, "02/05/2015", "15:33:39", 10, 248, 90, 1, 8, 7],
    ["MNSAMS", "106B", -2.68E+00, -2.00E+00, 3.92E-02, 0.99, 233.2671733, 0.671616405, 3.344239322, "02/05/2015", "15:33:39", 0, 0, 0, 0, 8, 8],
    ["MNSAMS", "106B", -2.68E+00, -2.01E+00, 8.26E-01, 0.99, 233.1301024, 13.85097729, 3.450329839, "02/05/2015", "15:33:39", 10, 248, 90, 2, 6, 8],
    ["MNSAMS", "106B", -2.18E+00, -1.46E+00, -4.63E-01, 0.99, 236.1887999, -10.00771399, 2.66427645, "02/05/2015", "15:33:39", 0, 0, 0, 0, 9, 6],
    ["MNSAMS", "106B", -2.00E+00, -1.38E+00, 2.11E+00, 0.99, 235.3943244, 40.96939985, 3.218151643, "02/05/2015", "15:33:39", 10, 248, 90, 1, 9, 9],
    ["MNSAMS", "106B", -1.43E+00, -1.03E+00, 3.34E+00, 0.99, 234.2355591, 62.18193859, 3.776426883, "02/05/2015", "15:33:39", 10, 248, 90, 1, 10, 9],
    ["MNSAMS", "106B", -1.22E+00, -9.29E-01, -2.14E-02, 0.99, 232.7116197, -0.799541795, 1.533590219, "02/05/2015", "15:33:39", 0, 0, 0, 0, 10, 10],
    ["MNSAMS", "106B", -1.09E+00, -1.47E+00, 1.68E+00, 0.99, 216.5568091, 42.5525252, 2.484230263, "02/05/2015", "15:33:39", 10, 248, 90, 2, 8, 10],
    ["MNSAMS", "106B", -8.59E-01, -7.97E-01, -5.34E-01, 0.99, 227.1441304, -24.4993879, 1.287729009, "02/05/2015", "15:33:39", 0, 0, 0, 0, 11, 8],
    ["MNSAMS", "106B", -4.73E-01, -4.39E-01, 4.66E+00, 0.99, 227.1350381, 82.11567113, 4.704471277, "02/05/2015", "15:33:39", 10, 248, 90, 1, 11, 11],
    ["MNSAMS", "106B", -2.65E-01, -6.78E-01, 5.23E+00, 0.99, 201.3483146, 82.07607559, 5.280417502, "02/05/2015", "15:33:39", 10, 248, 90, 1, 12, 11],
    ["MNSAMS", "106B", -6.92E-02, -9.29E-01, 2.86E-02, 0.99, 184.2600206, 1.758470293, 0.932012661, "02/05/2015", "15:33:39", 0, 0, 0, 0, 12, 12],
    ["MNSAMS", "106B", -3.98E-01, -5.65E-01, 2.85E+00, 0.99, 215.1618152, 76.36924575, 2.932597654, "02/05/2015", "15:33:39", 10, 248, 90, 2, 10, 12]
]
_data_MNSAMS106B_selection = [
    ["MNSAMS", "106B", -3.03E+00, -3.01E+00, -2.21E-01, 0.99, 225.1897204, -2.962125261, 4.276662367, "02/05/2015", "15:33:39", 0, 0, 0, 0, 3, 1],
    ["MNSAMS", "106B", -3.06E+00, -3.38E+00, 6.77E-01, 0.99, 222.1553444, 8.445848637, 4.609374036, "02/05/2015", "15:33:39", 10, 248, 90, 1, 3, 3],
    ["MNSAMS", "106B", -3.15E+00, -3.18E+00, 9.65E-01, 0.99, 224.7284581, 12.16632611, 4.578878138, "02/05/2015", "15:33:39", 10, 248, 90, 1, 4, 3],
    ["MNSAMS", "106B", -3.17E+00, -3.22E+00, -6.05E-02, 0.99, 224.5516854, -0.767101623, 4.518955659, "02/05/2015", "15:33:39", 0, 0, 0, 0, 4, 4],
    ["MNSAMS", "106B", -3.24E+00, -3.44E+00, -3.14E-01, 0.99, 223.2850698, -3.801529005, 4.736010557, "02/05/2015", "15:33:39", 0, 0, 0, 0, 5, 2],
    ["MNSAMS", "106B", -3.18E+00, -3.34E+00, 7.16E-01, 0.99, 223.5942507, 8.825082099, 4.666975037, "02/05/2015", "15:33:39", 10, 248, 90, 1, 5, 5],
    ["MNSAMS", "106B", -2.96E+00, -3.20E+00, 1.03E+00, 0.99, 222.7688254, 13.29447987, 4.479118217, "02/05/2015", "15:33:39", 10, 248, 90, 1, 6, 5],
    ["MNSAMS", "106B", -3.05E+00, -3.24E+00, -1.39E-01, 0.99, 223.269811, -1.789215033, 4.45190083, "02/05/2015", "15:33:39", 0, 0, 0, 0, 6, 6],
    ["MNSAMS", "106B", -3.24E+00, -3.19E+00, 2.75E-01, 0.99, 225.4455259, 3.461126758, 4.555142698, "02/05/2015", "15:33:39", 10, 248, 90, 2, 4, 6],
    ["MNSAMS", "106B", -3.11E+00, -2.28E+00, -4.27E-01, 0.99, 233.75415, -6.318618041, 3.879797546, "02/05/2015", "15:33:39", 0, 0, 0, 0, 7, 4],
    ["MNSAMS", "106B", -3.22E+00, -2.37E+00, 1.11E+00, 0.99, 233.6460084, 15.51612062, 4.149385497, "02/05/2015", "15:33:39", 10, 248, 90, 1, 7, 7],
    ["MNSAMS", "106B", -2.88E+00, -1.86E+00, 1.35E+00, 0.99, 237.144278, 21.49295565, 3.684630239, "02/05/2015", "15:33:39", 10, 248, 90, 1, 8, 7],
    ["MNSAMS", "106B", -2.68E+00, -2.00E+00, 3.92E-02, 0.99, 233.2671733, 0.671616405, 3.344239322, "02/05/2015", "15:33:39", 0, 0, 0, 0, 8, 8],
    ["MNSAMS", "106B", -2.68E+00, -2.01E+00, 8.26E-01, 0.99, 233.1301024, 13.85097729, 3.450329839, "02/05/2015", "15:33:39", 10, 248, 90, 2, 6, 8],
    ["MNSAMS", "106B", -2.18E+00, -1.46E+00, -4.63E-01, 0.99, 236.1887999, -10.00771399, 2.66427645, "02/05/2015", "15:33:39", 0, 0, 0, 0, 9, 6],
    ["MNSAMS", "106B", -2.00E+00, -1.38E+00, 2.11E+00, 0.99, 235.3943244, 40.96939985, 3.218151643, "02/05/2015", "15:33:39", 10, 248, 90, 1, 9, 9],
    ["MNSAMS", "106B", -1.43E+00, -1.03E+00, 3.34E+00, 0.99, 234.2355591, 62.18193859, 3.776426883, "02/05/2015", "15:33:39", 10, 248, 90, 1, 10, 9],
    ["MNSAMS", "106B", -1.22E+00, -9.29E-01, -2.14E-02, 0.99, 232.7116197, -0.799541795, 1.533590219, "02/05/2015", "15:33:39", 0, 0, 0, 0, 10, 10],
    ["MNSAMS", "106B", -1.09E+00, -1.47E+00, 1.68E+00, 0.99, 216.5568091, 42.5525252, 2.484230263, "02/05/2015", "15:33:39", 10, 248, 90, 2, 8, 10]
]


_data_MNSAMS106C = [
    ["MNSAMS", "106C", 3.38E+00, 1.38E+00, -2.03E+00, 0.99, 67.79059084, -29.07550055, 4.177283806, "02/05/2015", "15:33:39", 0, 0, 0, 0, 0, 0],
    ["MNSAMS", "106C", 3.56E+00, 1.36E+00, -1.67E-01, 0.99, 69.09201953, -2.509170556, 3.814588969, "02/05/2015", "15:33:39", 0, 0, 0, 0, 1, 0],
    ["MNSAMS", "106C", 3.49E+00, 1.31E+00, -6.73E-01, 0.99, 69.42596553, -10.23379196, 3.788024419, "02/05/2015", "15:33:39", 15, 0, -90, 1, 1, 1],
    ["MNSAMS", "106C", 3.77E+00, 1.50E+00, -7.87E-01, 0.99, 68.3034797, -10.9770245, 4.133070166, "02/05/2015", "15:33:39", 15, 0, -90, 1, 2, 1],
    ["MNSAMS", "106C", 3.64E+00, 1.56E+00, -1.32E-01, 0.99, 66.80140949, -1.909055117, 3.962401292, "02/05/2015", "15:33:39", 0, 0, 0, 0, 2, 2],
    ["MNSAMS", "106C", 3.36E+00, 1.69E+00, -7.62E-01, 0.99, 63.29869277, -11.45318499, 3.837491889, "02/05/2015", "15:33:39", 15, 0, -90, 2, 1, 2],
    ["MNSAMS", "106C", 3.74E+00, 1.73E+00, 1.46E-01, 0.99, 65.1763037, 2.02917089, 4.123325842, "02/05/2015", "15:33:39", 0, 0, 0, 0, 3, 1],
    ["MNSAMS", "106C", 3.70E+00, 1.78E+00, -6.91E-01, 0.99, 64.30867293, -9.553044267, 4.163637953, "02/05/2015", "15:33:39", 15, 0, -90, 1, 3, 3],
    ["MNSAMS", "106C", 3.76E+00, 1.68E+00, -1.06E+00, 0.99, 65.92450174, -14.43409483, 4.252481628, "02/05/2015", "15:33:39", 15, 0, -90, 1, 4, 3],
    ["MNSAMS", "106C", 3.56E+00, 1.73E+00, 0.00E+00, 0.99, 64.08233121, 0.00E+00, 3.958092975, "02/05/2015", "15:33:39", 0, 0, 0, 0, 4, 4],
    ["MNSAMS", "106C", 3.45E+00, 1.83E+00, -6.09E-01, 0.99, 62.05696558, -8.863418495, 3.952503131, "02/05/2015", "15:33:39", 15, 0, -90, 2, 2, 4],
    ["MNSAMS", "106C", 3.15E+00, 1.32E+00, 1.64E-01, 0.99, 67.26399512, 2.749112523, 3.419326834, "02/05/2015", "15:33:39", 0, 0, 0, 0, 5, 2],
    ["MNSAMS", "106C", 2.88E+00, 1.27E+00, -2.72E+00, 0.99, 66.20385314, -40.83207397, 4.160012019, "02/05/2015", "15:33:39", 15, 0, -90, 1, 5, 5],
    ["MNSAMS", "106C", 2.48E+00, 9.98E-01, -3.67E+00, 0.99, 68.07919131, -53.92991673, 4.540407911, "02/05/2015", "15:33:39", 15, 0, -90, 1, 6, 5],
    ["MNSAMS", "106C", 2.50E+00, 8.60E-01, 1.50E-01, 0.99, 71.01678294, 3.24729969, 2.648037009, "02/05/2015", "15:33:39", 0, 0, 0, 0, 6, 6],
    ["MNSAMS", "106C", 2.46E+00, 9.98E-01, -1.24E+00, 0.99, 67.91804543, -25.03682651, 2.930051877, "02/05/2015", "15:33:39", 15, 0, -90, 2, 4, 6],
    ["MNSAMS", "106C", 1.90E+00, 7.78E-01, 3.57E-02, 0.99, 67.73219161, 0.996170472, 2.053426037, "02/05/2015", "15:33:39", 0, 0, 0, 0, 7, 4],
    ["MNSAMS", "106C", 1.64E+00, 6.90E-01, -4.27E+00, 0.99, 67.18196626, -67.37928048, 4.625862082, "02/05/2015", "15:33:39", 15, 0, -90, 1, 7, 7],
    ["MNSAMS", "106C", 1.32E+00, 3.89E-01, -5.33E+00, 0.99, 73.57991445, -75.52324088, 5.504781649, "02/05/2015", "15:33:39", 15, 0, -90, 1, 8, 7],
    ["MNSAMS", "106C", 1.29E+00, 1.88E-01, 1.03E-01, 0.99, 81.70829141, 4.517572698, 1.307689948, "02/05/2015", "15:33:39", 0, 0, 0, 0, 8, 8],
    ["MNSAMS", "106C", 1.25E+00, 2.26E-01, -2.89E+00, 0.99, 79.75163435, -66.27266494, 3.156845894, "02/05/2015", "15:33:39", 15, 0, -90, 2, 6, 8],
    ["MNSAMS", "106C", 1.09E+00, -5.65E-02, 2.78E-01, 0.99, 92.96726321, 14.2896226, 1.126310903, "02/05/2015", "15:33:39", 0, 0, 0, 0, 9, 6],
    ["MNSAMS", "106C", 7.72E-01, -1.07E-01, -5.90E+00, 0.99, 97.89098145, -82.47489487, 5.951254742, "02/05/2015", "15:33:39", 15, 0, -90, 1, 9, 9],
    ["MNSAMS", "106C", 4.44E-01, -1.51E-01, -6.46E+00, 0.99, 108.78266, -85.84780205, 6.477000618, "02/05/2015", "15:33:39", 15, 0, -90, 1, 10, 9],
    ["MNSAMS", "106C", 8.41E-01, -3.14E-02, -7.73E-01, 0.99, 92.1382309, -42.56759561, 1.142714295, "02/05/2015", "15:33:39", 0, 0, 0, 0, 10, 10],
    ["MNSAMS", "106C", 5.47E-01, -7.53E-02, -3.89E+00, 0.99, 97.83807148, -81.92122882, 3.928992121, "02/05/2015", "15:33:39", 15, 0, -90, 2, 8, 10]
]

_data_MNSAMS106C_selection = [
    ["MNSAMS", "106C", 3.74E+00, 1.73E+00, 1.46E-01, 0.99, 65.1763037, 2.02917089, 4.123325842, "02/05/2015", "15:33:39", 0, 0, 0, 0, 3, 1],
    ["MNSAMS", "106C", 3.70E+00, 1.78E+00, -6.91E-01, 0.99, 64.30867293, -9.553044267, 4.163637953, "02/05/2015", "15:33:39", 15, 0, -90, 1, 3, 3],
    ["MNSAMS", "106C", 3.76E+00, 1.68E+00, -1.06E+00, 0.99, 65.92450174, -14.43409483, 4.252481628, "02/05/2015", "15:33:39", 15, 0, -90, 1, 4, 3],
    ["MNSAMS", "106C", 3.56E+00, 1.73E+00, 0.00E+00, 0.99, 64.08233121, 0.00E+00, 3.958092975, "02/05/2015", "15:33:39", 0, 0, 0, 0, 4, 4],
    ["MNSAMS", "106C", 3.15E+00, 1.32E+00, 1.64E-01, 0.99, 67.26399512, 2.749112523, 3.419326834, "02/05/2015", "15:33:39", 0, 0, 0, 0, 5, 2],
    ["MNSAMS", "106C", 2.88E+00, 1.27E+00, -2.72E+00, 0.99, 66.20385314, -40.83207397, 4.160012019, "02/05/2015", "15:33:39", 15, 0, -90, 1, 5, 5],
    ["MNSAMS", "106C", 2.48E+00, 9.98E-01, -3.67E+00, 0.99, 68.07919131, -53.92991673, 4.540407911, "02/05/2015", "15:33:39", 15, 0, -90, 1, 6, 5],
    ["MNSAMS", "106C", 2.50E+00, 8.60E-01, 1.50E-01, 0.99, 71.01678294, 3.24729969, 2.648037009, "02/05/2015", "15:33:39", 0, 0, 0, 0, 6, 6],
    ["MNSAMS", "106C", 2.46E+00, 9.98E-01, -1.24E+00, 0.99, 67.91804543, -25.03682651, 2.930051877, "02/05/2015", "15:33:39", 15, 0, -90, 2, 4, 6],
    ["MNSAMS", "106C", 1.90E+00, 7.78E-01, 3.57E-02, 0.99, 67.73219161, 0.996170472, 2.053426037, "02/05/2015", "15:33:39", 0, 0, 0, 0, 7, 4],
    ["MNSAMS", "106C", 1.64E+00, 6.90E-01, -4.27E+00, 0.99, 67.18196626, -67.37928048, 4.625862082, "02/05/2015", "15:33:39", 15, 0, -90, 1, 7, 7],
    ["MNSAMS", "106C", 1.32E+00, 3.89E-01, -5.33E+00, 0.99, 73.57991445, -75.52324088, 5.504781649, "02/05/2015", "15:33:39", 15, 0, -90, 1, 8, 7],
    ["MNSAMS", "106C", 1.29E+00, 1.88E-01, 1.03E-01, 0.99, 81.70829141, 4.517572698, 1.307689948, "02/05/2015", "15:33:39", 0, 0, 0, 0, 8, 8],
    ["MNSAMS", "106C", 1.25E+00, 2.26E-01, -2.89E+00, 0.99, 79.75163435, -66.27266494, 3.156845894, "02/05/2015", "15:33:39", 15, 0, -90, 2, 6, 8]
]


#################
###   logic   ###
#################

_dataset_dict = {
    "MNSAMS106B": _data_MNSAMS106B,
    "MNSAMS106C": _data_MNSAMS106C
}

_dataset_selection_dict = {
    "MNSAMS106B": _data_MNSAMS106B_selection,
    "MNSAMS106C": _data_MNSAMS106C_selection,
}


def get(specimen, selection=False):

    # select the right dataset dictionary
    dict = _dataset_dict
    if selection:
        dict = _dataset_selection_dict

    # check if the specimen is in the dict
    if (specimen in dict) == False:
        print("WARNING: the specimen %s is not present in the demo data, asked for a selection: %s" % (specimen, selection))
        return []
    else:
        return _demo_data_to_real_format(dict[specimen])


def _demo_data_to_real_format(l):
    result = []
    for msrmt in l:
        result.append({
            "site": msrmt[0],
            "specimen": msrmt[1],
            "x": msrmt[2],
            "y": msrmt[3],
            "z": msrmt[4],
            "error": msrmt[5],
            "dec": msrmt[6],
            "inc": msrmt[7],
            "total_m": msrmt[8],
            "date": msrmt[9],
            "time": msrmt[10],
            "lab_field": msrmt[11],
            "lab_field_dec": msrmt[12],
            "lab_field_inc": msrmt[13],
            "type": msrmt[14],
            "step": msrmt[15],
            "previous_step": msrmt[16]
        })
    return result
