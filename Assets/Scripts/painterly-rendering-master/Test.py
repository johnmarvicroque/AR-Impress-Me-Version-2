import numpy
import os

path = "D:\Thesis\CapturedUnalteredScene"
path1 = r"D:\Thesis\CapturedUnalteredScene\GistOutput"

centroidOne = [0.0451056, 0.0896504, 0.0984765, 0.0660195, 0.0344274, 0.0703501, 0.0810796, 0.0805062, 0.0402381,
                   0.0651527, 0.0716088, 0.070411, 0.0441306, 0.0637218, 0.0678075, 0.0636398, 0.0379922, 0.0791748,
                   0.086041, 0.0533129, 0.0345918, 0.0594824, 0.0715001, 0.0686518, 0.0434129, 0.0639245, 0.0649115,
                   0.0654347, 0.0419893, 0.0560994, 0.0647893, 0.0612118, 0.0361144, 0.0668622, 0.0803275, 0.047652,
                   0.0389292, 0.0506117, 0.0662168, 0.0602009, 0.0421523, 0.0578541, 0.0664805, 0.065978, 0.0396973,
                   0.0521031, 0.0607607, 0.0693276, 0.0389018, 0.0550969, 0.0768354, 0.0488397, 0.0415153, 0.0479104,
                   0.0685919, 0.0720416, 0.0435838, 0.0583748, 0.070559, 0.0722941, 0.0440471, 0.0520432, 0.0709158,
                   0.0788619, 0.0430592, 0.05229, 0.0814178, 0.0490701, 0.0462266, 0.0482386, 0.070193, 0.0613129,
                   0.0467731, 0.0599985, 0.0787415, 0.0667233, 0.0503267, 0.0547492, 0.0832057, 0.0881188, 0.0375099,
                   0.0549796, 0.0773152, 0.0437065, 0.0422584, 0.0457911, 0.0631115, 0.0505545, 0.044501, 0.0572387,
                   0.0702981, 0.0607446, 0.0482864, 0.0515764, 0.0666283, 0.0747312, 0.0326889, 0.0563368, 0.0762364,
                   0.0434101, 0.0362067, 0.0465136, 0.0637879, 0.050977, 0.0428628, 0.0531229, 0.0653565, 0.0575304,
                   0.0444012, 0.0528516, 0.0571915, 0.0668846, 0.0363361, 0.0698484, 0.0845174, 0.0506593, 0.0370841,
                   0.0566463, 0.0703851, 0.0630727, 0.0393481, 0.054277, 0.0668892, 0.0607792, 0.0417606, 0.0573478,
                   0.058556, 0.0640117, 0.0372091, 0.0777637, 0.0727935, 0.059781, 0.0261709, 0.0617239, 0.0745389,
                   0.0673812, 0.0276367, 0.0550669, 0.0582247, 0.0618901, 0.029857, 0.0546027, 0.062954, 0.0529443,
                   0.0290027, 0.0758186, 0.0655521, 0.0513711, 0.0241698, 0.0540439, 0.0628038, 0.0627853, 0.0289547,
                   0.0491531, 0.0544293, 0.0583018, 0.0253833, 0.0437925, 0.06201, 0.052696, 0.0245414, 0.0648432,
                   0.0728917, 0.0411835, 0.030642, 0.0404728, 0.0602937, 0.0585239, 0.0288685, 0.0426243, 0.0504221,
                   0.0653737, 0.0236872, 0.043054, 0.0541719, 0.0613647, 0.0284038, 0.0486432, 0.0715243, 0.0417228,
                   0.0336765, 0.0360139, 0.0678644, 0.0855024, 0.0336828, 0.0474514, 0.0580886, 0.078124, 0.0291516,
                   0.0454891, 0.0651761, 0.0659599, 0.0358579, 0.047248, 0.0776371, 0.0431428, 0.0403343, 0.0373826,
                   0.0649147, 0.0616016, 0.0390354, 0.0520445, 0.0698885, 0.0568219, 0.0380576, 0.0456986, 0.0804192,
                   0.0716914, 0.0303101, 0.0429179, 0.0685282, 0.0354464, 0.034215, 0.0361861, 0.0543955, 0.0453849,
                   0.0346342, 0.0441215, 0.0641169, 0.0451232, 0.0342992, 0.0414818, 0.0632621, 0.0582797, 0.0270189,
                   0.0465268, 0.0625953, 0.0317572, 0.0261475, 0.037845, 0.0530825, 0.0466001, 0.0279797, 0.0375093,
                   0.0559755, 0.0472365, 0.0268838, 0.039934, 0.0518013, 0.0570125, 0.0317661, 0.0594921, 0.0677231,
                   0.0405262, 0.0268417, 0.0484663, 0.0634181, 0.0514517, 0.0268198, 0.0444109, 0.0569944, 0.0521637,
                   0.0274576, 0.0448217, 0.0519892, 0.0548363, 0.0275536, 0.0869741, 0.0649768, 0.0558001, 0.021445,
                   0.0579206, 0.0644298, 0.0499388, 0.0228493, 0.0452373, 0.0492797, 0.0515656, 0.0228141, 0.040565,
                   0.0576639, 0.0375746, 0.027168, 0.0655648, 0.0613407, 0.041604, 0.0183136, 0.0552121, 0.0517932,
                   0.0566496, 0.0240823, 0.0391855, 0.0448619, 0.0592219, 0.0174144, 0.0353113, 0.0502385, 0.0416725,
                   0.022071, 0.0617349, 0.0705049, 0.0364728, 0.0243028, 0.0418209, 0.0603473, 0.0499441, 0.0228527,
                   0.0399421, 0.0410864, 0.0772152, 0.0204743, 0.0451784, 0.0461278, 0.0496001, 0.025986, 0.0515044,
                   0.0755279, 0.0417043, 0.0280949, 0.0355865, 0.0694112, 0.0684482, 0.0226675, 0.0486593, 0.0506471,
                   0.0772888, 0.0228293, 0.0429127, 0.0680017, 0.0456093, 0.0282684, 0.0439969, 0.0826749, 0.0450161,
                   0.0358546, 0.0354041, 0.0715555, 0.0507477, 0.0314633, 0.0529149, 0.065968, 0.0438458, 0.0282343,
                   0.0413948, 0.0925076, 0.0355309, 0.0256357, 0.0352397, 0.0604139, 0.0379665, 0.0296623, 0.0337985,
                   0.0644377, 0.0480906, 0.0276672, 0.0411926, 0.0595287, 0.0437691, 0.0247101, 0.0371521, 0.0571891,
                   0.0352337, 0.0209249, 0.0404839, 0.0457877, 0.0310342, 0.0238223, 0.0367235, 0.049179, 0.04487,
                   0.0232822, 0.039336, 0.0570155, 0.0381233, 0.0194635, 0.0366844, 0.0450741, 0.039048, 0.0235039,
                   0.0556759, 0.0545058, 0.0388983, 0.0232207, 0.0488433, 0.054334, 0.0446772, 0.0231087, 0.0391755,
                   0.0480191, 0.0456172, 0.0228924, 0.0392228, 0.0497499, 0.033296, 0.0306748, 0.0869526, 0.0483643,
                   0.0500926, 0.0250355, 0.0518727, 0.0439058, 0.0441085, 0.0190714, 0.0427092, 0.0645059, 0.0486748,
                   0.0199883, 0.042838, 0.0465567, 0.0276171, 0.0224582, 0.0794322, 0.05224, 0.0399643, 0.0167898,
                   0.0444465, 0.0477343, 0.0554796, 0.0148005, 0.0323892, 0.0390333, 0.0442945, 0.0126962, 0.0372784,
                   0.0316544, 0.037308, 0.0205931, 0.0729038, 0.0783873, 0.0319681, 0.0189787, 0.0369865, 0.0591321,
                   0.043555, 0.0179073, 0.0325999, 0.0269911, 0.0646882, 0.015442, 0.0434815, 0.0363507, 0.0341488,
                   0.0350877, 0.0469501, 0.0846859, 0.0383676, 0.0246737, 0.0326944, 0.0721429, 0.0599005, 0.014676,
                   0.0298627, 0.0444873, 0.0710699, 0.016039, 0.0420881, 0.0791474, 0.0266425, 0.0355393, 0.0430106,
                   0.0697311, 0.0510989, 0.0263716, 0.0382438, 0.0579636, 0.0612449, 0.0207903, 0.0491116, 0.0611424,
                   0.0376403, 0.0149372, 0.049974, 0.125885, 0.0319417, 0.0221061, 0.0348764, 0.0433571, 0.035968,
                   0.0226149, 0.0368159, 0.0604309, 0.0556308, 0.0298669, 0.0477356, 0.0556285, 0.0486474, 0.0184489,
                   0.0416534, 0.0631656, 0.0308689, 0.0218958, 0.0441334, 0.0429694, 0.0398633, 0.0186524, 0.029424,
                   0.0494149, 0.0495368, 0.0226837, 0.0421083, 0.0602807, 0.0427842, 0.0143972, 0.0433503, 0.036574,
                   0.030147, 0.0281409, 0.0495646, 0.045968, 0.0451389, 0.0187831, 0.0484779, 0.0442487, 0.0385835,
                   0.0230794, 0.0356385, 0.0492939, 0.0507823, 0.0188204, 0.0477498, 0.0377547, 0.0222094]
centroidTwo = [0.0547128, 0.0534731, 0.0655651, 0.0614566, 0.0500532, 0.0618512, 0.0654156, 0.065096, 0.0587998,
               0.0638584, 0.0712679, 0.0635438, 0.054433, 0.0596306, 0.0618551, 0.0583478, 0.0529594, 0.0477156,
               0.0625308, 0.0633621, 0.0471268, 0.0566348, 0.0650499, 0.0619675, 0.0546443, 0.0624422, 0.0701239,
               0.0625226, 0.0533254, 0.0576401, 0.0595238, 0.0563105, 0.0525043, 0.0442925, 0.0554539, 0.05816,
               0.0410142, 0.0536674, 0.0644848, 0.0630424, 0.052389, 0.0640152, 0.075277, 0.064473, 0.0531579,
               0.0554599, 0.0591614, 0.054614, 0.0521019, 0.0457505, 0.0530401, 0.0593594, 0.0466458, 0.052527,
               0.065219, 0.0683813, 0.053137, 0.0638835, 0.0760512, 0.0738401, 0.0517512, 0.0511408, 0.0604505,
               0.0605125, 0.0526128, 0.0472773, 0.054117, 0.0640303, 0.0489372, 0.0515017, 0.0661429, 0.0739581,
               0.0576927, 0.0648772, 0.0805641, 0.0784163, 0.0523486, 0.0549011, 0.0627139, 0.071155, 0.050069,
               0.0429712, 0.0535127, 0.0604, 0.0485383, 0.0502265, 0.0656317, 0.0647734, 0.05816, 0.0614117,
               0.0732809, 0.0675698, 0.0532216, 0.0517024, 0.0581066, 0.0601208, 0.0475083, 0.0467293, 0.0534986,
               0.0592068, 0.0469867, 0.0545317, 0.0634249, 0.064245, 0.0538349, 0.0605762, 0.0676848, 0.0656627,
               0.0527614, 0.0512466, 0.0529579, 0.053256, 0.052492, 0.0527538, 0.0584476, 0.0583126, 0.0475056,
               0.0574481, 0.0608863, 0.0637131, 0.0539871, 0.0638355, 0.0673089, 0.06549, 0.0508221, 0.0551697,
               0.0561831, 0.056099, 0.0619187, 0.0493684, 0.0659961, 0.0545637, 0.0441717, 0.0640018, 0.0544222,
               0.0529831, 0.0526004, 0.0542307, 0.0584478, 0.0523271, 0.0433188, 0.0535137, 0.0534296, 0.0496067,
               0.0534711, 0.0419489, 0.0588529, 0.0537508, 0.0394613, 0.0491958, 0.0503443, 0.0508538, 0.0484995,
               0.05357, 0.0519135, 0.0545432, 0.0460924, 0.0503187, 0.0518663, 0.0451016, 0.0452506, 0.0361356,
               0.0420092, 0.048177, 0.033422, 0.0430714, 0.0481689, 0.0478575, 0.0431654, 0.0495831, 0.0541187,
               0.0557579, 0.0395441, 0.0419333, 0.0475918, 0.0459024, 0.0435831, 0.0357022, 0.0376566, 0.0496177,
               0.0356902, 0.0430519, 0.0496522, 0.0551208, 0.0393815, 0.0476914, 0.0606662, 0.055709, 0.0365122,
               0.0391312, 0.0499384, 0.0458763, 0.042735, 0.0331805, 0.0405613, 0.0479339, 0.0359576, 0.0409509,
               0.0480127, 0.0586207, 0.0480634, 0.0462169, 0.0573393, 0.057862, 0.0363983, 0.040163, 0.0544143,
               0.0534758, 0.0402951, 0.0322307, 0.040813, 0.0445399, 0.0368059, 0.0413905, 0.0465776, 0.0533383,
               0.0490968, 0.0460808, 0.050899, 0.048409, 0.0342336, 0.0366785, 0.0485076, 0.0477704, 0.0395329,
               0.037909, 0.0423125, 0.0493279, 0.0380503, 0.0449624, 0.051792, 0.0483971, 0.0416971, 0.0393943,
               0.0496647, 0.0455931, 0.0392685, 0.0374047, 0.0433291, 0.0408237, 0.0488596, 0.0454828, 0.0467545,
               0.0507258, 0.0412565, 0.0550955, 0.0497587, 0.0517847, 0.0440919, 0.0433725, 0.0490861, 0.0469826,
               0.0417459, 0.0463757, 0.0468522, 0.0435617, 0.0937855, 0.0618415, 0.0550735, 0.0523858, 0.0447598,
               0.0645367, 0.0537676, 0.0433129, 0.0512453, 0.0527014, 0.058093, 0.0451472, 0.0460134, 0.0579731,
               0.0469656, 0.0391346, 0.0607137, 0.0436603, 0.0527128, 0.0470879, 0.035035, 0.0511485, 0.039482,
               0.0458505, 0.0470019, 0.0634828, 0.051907, 0.0397505, 0.0433402, 0.0447743, 0.0476989, 0.0412051,
               0.0367684, 0.0321728, 0.0366526, 0.0406246, 0.0342339, 0.0403667, 0.0445854, 0.0446843, 0.0384762,
               0.0478642, 0.044044, 0.0468076, 0.0377376, 0.0344435, 0.0428025, 0.0398584, 0.0345654, 0.0278747,
               0.0341378, 0.0579232, 0.0341881, 0.036598, 0.041328, 0.0564635, 0.0353662, 0.0414668, 0.0518391,
               0.0519061, 0.0343803, 0.0304856, 0.0459139, 0.0387555, 0.0381084, 0.0287909, 0.0434962, 0.059526,
               0.032894, 0.0398387, 0.0485841, 0.0583686, 0.0475559, 0.0428872, 0.0515616, 0.0534102, 0.0358834,
               0.0299884, 0.062106, 0.0428405, 0.0384233, 0.0308252, 0.0452824, 0.0443339, 0.0375881, 0.0416188,
               0.0437448, 0.0509373, 0.0497185, 0.0427778, 0.0524455, 0.0441455, 0.0292985, 0.0340492, 0.0459479,
               0.0317835, 0.0388849, 0.035413, 0.0424016, 0.0477629, 0.0305571, 0.0427868, 0.0413433, 0.0406988,
               0.035295, 0.0361267, 0.0422551, 0.035724, 0.0285436, 0.0324101, 0.0298803, 0.0295806, 0.0561759,
               0.0406666, 0.0414721, 0.0380023, 0.030697, 0.0515593, 0.0477585, 0.0416806, 0.0375146, 0.0394224,
               0.0468086, 0.0356167, 0.0394023, 0.0396749, 0.0401084, 0.0362598, 0.0931867, 0.08344, 0.050962,
               0.0517988, 0.0420298, 0.0457701, 0.0514798, 0.0317227, 0.0368036, 0.0550121, 0.0539901, 0.0584893,
               0.0573711, 0.050229, 0.0388231, 0.032333, 0.0456309, 0.0492431, 0.0536314, 0.036043, 0.0290764,
               0.0568162, 0.0413021, 0.0290579, 0.019814, 0.069514, 0.0400725, 0.0404446, 0.047816, 0.049918,
               0.0433366, 0.0271138, 0.0303794, 0.0248559, 0.0334599, 0.0329476, 0.0333467, 0.0427112, 0.0394212,
               0.0356332, 0.0279874, 0.0510962, 0.0506939, 0.0460724, 0.0416315, 0.0366615, 0.0399169, 0.0266382,
               0.0339799, 0.0276075, 0.032524, 0.0452821, 0.0400179, 0.0245554, 0.0383818, 0.0402073, 0.0293022,
               0.0366893, 0.0606931, 0.0506525, 0.0324746, 0.0274683, 0.0435214, 0.0444618, 0.0323025, 0.0391755,
               0.0370768, 0.0462277, 0.0382585, 0.0352555, 0.0565446, 0.0458625, 0.0478376, 0.0448181, 0.0528791,
               0.0420863, 0.0326159, 0.0378337, 0.0418096, 0.0452144, 0.0243078, 0.0290429, 0.0457711, 0.0281383,
               0.0321862, 0.0374976, 0.0521528, 0.047736, 0.061423, 0.0337188, 0.0563343, 0.045902, 0.0345198,
               0.0402521, 0.0340454, 0.0410534, 0.0348366, 0.0436633, 0.0337909, 0.0292423, 0.0258301, 0.0382074,
               0.0488813, 0.0340062, 0.0352631, 0.034681, 0.0332732, 0.0395843, 0.0271902, 0.0278386, 0.0241029,
               0.0325316, 0.0483818, 0.0459333, 0.0315827, 0.0337553, 0.0282746, 0.0544957, 0.0507041, 0.0340914,
               0.0411757, 0.037339, 0.0464895, 0.0438363, 0.0292777, 0.035544, 0.0423996, 0.0395727]

centroidThree = [0.0559953, 0.0648605, 0.0565386, 0.0686197, 0.0622352, 0.0641734, 0.0594773, 0.0792594, 0.0613605,
                 0.0722981, 0.0578206, 0.0556642, 0.0641664, 0.0583653, 0.0518338, 0.0577433, 0.049196, 0.0570245,
                 0.0500365, 0.0507083, 0.0544157, 0.0582911, 0.0495227, 0.064323, 0.0571574, 0.0661409, 0.0493898,
                 0.0450469, 0.0551702, 0.0550668, 0.0441547, 0.0534841, 0.0471257, 0.0494046, 0.0422628, 0.0371807,
                 0.0475499, 0.0464515, 0.04718, 0.0521128, 0.0509714, 0.0627895, 0.0474564, 0.0405704, 0.0419815,
                 0.0534448, 0.0408968, 0.0513526, 0.0526778, 0.0475383, 0.0391347, 0.0344197, 0.050849, 0.0502766,
                 0.0511463, 0.0505864, 0.0513646, 0.0646267, 0.0460381, 0.0430354, 0.0400994, 0.0561398, 0.0405104,
                 0.0498355, 0.0555992, 0.0521901, 0.0393845, 0.036031, 0.0592948, 0.0541609, 0.0509629, 0.049228,
                 0.058954, 0.0658347, 0.0522458, 0.0448502, 0.0443648, 0.0603114, 0.0412559, 0.0518318, 0.0508903,
                 0.0493206, 0.0425192, 0.0370365, 0.0548616, 0.0516971, 0.0543449, 0.050315, 0.0500592, 0.06467,
                 0.0507529, 0.0444923, 0.0413445, 0.05823, 0.0411601, 0.0507686, 0.0462895, 0.0518126, 0.048035,
                 0.0422975, 0.0497251, 0.0501018, 0.0546229, 0.0610309, 0.04388, 0.0655143, 0.048028, 0.0456503,
                 0.0455235, 0.0510376, 0.0404445, 0.0499445, 0.0496508, 0.0615976, 0.0567331, 0.0600914, 0.0510123,
                 0.0565492, 0.0622389, 0.078979, 0.0505778, 0.0664738, 0.0536552, 0.0509904, 0.0542074, 0.0514436,
                 0.0475037, 0.0545538, 0.0446576, 0.0636645, 0.0580956, 0.0587181, 0.0466873, 0.0530342, 0.0500207,
                 0.0751282, 0.0510428, 0.0570113, 0.0423017, 0.0521584, 0.0628966, 0.0491634, 0.038137, 0.0441056,
                 0.0419241, 0.0516897, 0.0497775, 0.050786, 0.0422454, 0.0534045, 0.0421554, 0.0572294, 0.0465258,
                 0.0514174, 0.0370652, 0.0440425, 0.0496092, 0.0442912, 0.0317495, 0.0440055, 0.0482775, 0.0444851,
                 0.0385254, 0.0402931, 0.0447514, 0.0475314, 0.0419775, 0.044696, 0.0433963, 0.0490076, 0.0378495,
                 0.0340762, 0.035635, 0.0421317, 0.0286969, 0.0436076, 0.0537061, 0.0479077, 0.0383098, 0.0327403,
                 0.0523331, 0.0481211, 0.0463246, 0.0431942, 0.0502433, 0.0516664, 0.0396169, 0.0374593, 0.032819,
                 0.0451258, 0.0314608, 0.045347, 0.0555394, 0.0532892, 0.0394079, 0.0377801, 0.0594021, 0.0461713,
                 0.0499584, 0.0428071, 0.0564853, 0.0514104, 0.0468756, 0.038009, 0.0338937, 0.0508985, 0.0309791,
                 0.0482403, 0.0523262, 0.0496624, 0.0463922, 0.041428, 0.0547042, 0.0479563, 0.0478174, 0.0407475,
                 0.0482051, 0.0484814, 0.0498169, 0.039273, 0.0334249, 0.0472341, 0.032325, 0.0463796, 0.0442986,
                 0.0485794, 0.0526806, 0.0460706, 0.0466728, 0.0460049, 0.0543123, 0.0499083, 0.0397185, 0.0514262,
                 0.0418791, 0.0430216, 0.0397166, 0.0429721, 0.0340337, 0.0455451, 0.0432255, 0.0601726, 0.0616937,
                 0.0623128, 0.0473266, 0.0498218, 0.0543063, 0.0685097, 0.0482846, 0.0550498, 0.0407089, 0.0504514,
                 0.0544779, 0.044202, 0.0369241, 0.0441408, 0.0417887, 0.0560719, 0.0707315, 0.0568446, 0.0471243,
                 0.0599138, 0.0528427, 0.0492379, 0.0412001, 0.056448, 0.0403982, 0.0519278, 0.0516682, 0.0469184,
                 0.0391346, 0.043477, 0.0356019, 0.0446937, 0.0544804, 0.0446653, 0.0367647, 0.0497065, 0.0396898,
                 0.0493586, 0.0413633, 0.0442894, 0.0412748, 0.037893, 0.0535739, 0.0388096, 0.0358609, 0.0430682,
                 0.0371019, 0.0448582, 0.0417674, 0.0371826, 0.0412797, 0.0457222, 0.0372161, 0.0363832, 0.0422185,
                 0.0378904, 0.0431817, 0.0365245, 0.0396643, 0.0373841, 0.0278629, 0.0376906, 0.0436448, 0.0528725,
                 0.0398177, 0.0328261, 0.0415787, 0.0501779, 0.0352462, 0.0377953, 0.0576608, 0.0355724, 0.0516914,
                 0.0399386, 0.0382522, 0.0398803, 0.0252726, 0.0392546, 0.0590379, 0.0541549, 0.0400663, 0.0385782,
                 0.0610016, 0.0436046, 0.0501658, 0.0336093, 0.0591555, 0.0450164, 0.0578245, 0.0397687, 0.0336621,
                 0.0400852, 0.0237477, 0.0516088, 0.052437, 0.0489333, 0.0407922, 0.0437323, 0.0527841, 0.0454968,
                 0.0472128, 0.0374808, 0.0459051, 0.0411806, 0.0503226, 0.0383141, 0.0279388, 0.0373533, 0.0263837,
                 0.0487558, 0.0425535, 0.0410873, 0.0567011, 0.0416779, 0.0406646, 0.048585, 0.0423994, 0.0421617,
                 0.0406467, 0.0427584, 0.0464306, 0.0416202, 0.0349369, 0.0313987, 0.0336095, 0.0374223, 0.0491683,
                 0.0447166, 0.0575254, 0.0459277, 0.0455746, 0.0500205, 0.0438123, 0.0453825, 0.0392564, 0.0480489,
                 0.0370144, 0.057866, 0.046147, 0.0391427, 0.035306, 0.0327529, 0.0380446, 0.0522085, 0.0614703,
                 0.0598514, 0.0449234, 0.0393995, 0.049538, 0.0534213, 0.0453081, 0.0554852, 0.0406097, 0.0393543,
                 0.0510612, 0.0455157, 0.0425199, 0.0662427, 0.0263695, 0.046326, 0.0487786, 0.0438143, 0.0404939,
                 0.0423605, 0.0297841, 0.0434962, 0.0425474, 0.0379828, 0.0423223, 0.0321817, 0.0744131, 0.0417364,
                 0.0371864, 0.0567884, 0.0353094, 0.0492885, 0.0395215, 0.0347222, 0.045953, 0.0402453, 0.0283565,
                 0.0401471, 0.0485435, 0.0316015, 0.0392145, 0.0350128, 0.0582033, 0.0369665, 0.0292489, 0.031934,
                 0.0364964, 0.0309355, 0.0266554, 0.0209722, 0.0567215, 0.0438964, 0.0280122, 0.0353987, 0.080787,
                 0.0459661, 0.0453585, 0.0431877, 0.0432992, 0.0593774, 0.0231649, 0.0368181, 0.0594668, 0.0380395,
                 0.0285917, 0.0283659, 0.0758672, 0.0382826, 0.0374015, 0.036058, 0.104759, 0.0440972, 0.0565365,
                 0.052296, 0.0405168, 0.0377347, 0.0185488, 0.0555484, 0.0561116, 0.0347792, 0.0277533, 0.0287748,
                 0.059028, 0.0469253, 0.0407381, 0.031627, 0.0644696, 0.033283, 0.0414739, 0.0391009, 0.0316132,
                 0.033288, 0.0260119, 0.0535639, 0.0381994, 0.0282727, 0.0435005, 0.0269597, 0.0421727, 0.0532867,
                 0.0321495, 0.0224939, 0.0499001, 0.0423894, 0.0452782, 0.0262833, 0.052069, 0.0465883, 0.0350944,
                 0.0422782, 0.044064, 0.0400949, 0.0538456, 0.0346637, 0.0400827, 0.0471272, 0.0497192, 0.0421532,
                 0.049144, 0.053848, 0.0458774, 0.0421182, 0.06449, 0.0548896, 0.041689, 0.0322535]
os.chdir(path)
os.system("gist.exe -i UnalteredScene -o GistOutput")

os.chdir(path1)
f = open("gist.txt", "r", encoding='utf-8', errors='ignore')
f1 = []
for line in f:
    f1.append(line.split(' '))

f1[0].pop()
A = numpy.array(centroidOne[0])
A = A.astype(numpy.float)
B = numpy.array(centroidTwo[0])
B = B.astype(numpy.float)
C = numpy.array(centroidThree[0])
C = C.astype(numpy.float)
D = numpy.array(f1[0])
D = D.astype(numpy.float)

dist1 = numpy.linalg.norm(A - D)
dist2 = numpy.linalg.norm(B - D)
dist3 = numpy.linalg.norm(C - D)

list1 = [dist1, dist2, dist3]
dist = min(list1)
min_index = list1.index(min(list1))

print("Pre-1886: ", dist1)
print("Post-1886: ", dist2)
print("After Years: ", dist3)
print(min_index, dist)

