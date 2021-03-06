# -*- coding: utf-8 -*-
import math
import codecs

base_dir = '/data/project/dexbot/pywikipedia-git/'
f = codecs.open('%sde_kian4.txt' % base_dir, 'r', 'utf-8')
a = f.read().split('\n')
f.close()
f = codecs.open('%skian1_1.txt' % base_dir, 'r')
cats = eval(f.read())
f.close()
f = codecs.open('%sHuman.txt' % base_dir, 'r', 'utf-8')
humans_and_not = set(f.read().split('\n'))
f.close()
f = codecs.open('%sNotHuman.txt' % base_dir, 'r', 'utf-8')
humans_and_not = humans_and_not.union(set(f.read().split('\n')))
f.close()
f = codecs.open('%skian_res.txt' % base_dir, 'w', 'utf-8')
f.write('')
f.close()
rrres = []
# noqa ckb theta = [[[2e-323, 2e-323, -2e-323, 2e-323, 2e-323, -2e-323], [-0.00043176778056034564, 1.484016280120311, -0.08659442042765618, 0.1491053083259633, 0.3599555849299492, -2.297482660868937], [-0.0004279421441273935, 1.4819077656806594, -0.10899962633405397, 0.1947955999676962, 0.35771619960110335, -2.3056447830404245], [0.000412242739155189, -1.3814515191579375, 0.03300444137430453, -0.1795016263352709, -0.3599444017494041, 2.1980089641009424], [-0.00043946885571465114, 1.4779682422837148, -0.04779782127522804, 0.09447447564922161, 0.3686740157447475, -2.2948374894790957], [-0.00045208090684272265, 1.4725756257215807, -0.07399120226673019, 0.11807677489401815, 0.32832196578936174, -2.1720348775912255]], [[0.02110510787227155, 0.18443128496994915, 0.18449509725064692, -0.16251383194580848, 0.18435706815303177, 0.18364474373213188]]]
# noqa de theta = [[[2e-323, 2e-323, 2e-323, -2e-323, -2e-323, -2e-323], [-0.0003855748012225437, 1.123507805738474, -0.2750338741031472, -0.2752608666762779, -0.8654304341063274, -1.94308038626915], [0.0003907577623924355, -1.1389257362517857, 0.27738289969104923, 0.2910876576164902, 0.8788039048270229, 1.9545426398933807], [-0.0003815721583477605, 1.134135551187454, -0.27591491684611846, -0.3101912488820203, -0.8612560748260452, -1.9326841675071573], [0.00039962979532541434, -1.1269831508653372, 0.28221502202761084, 0.2533250237574603, 0.8718435037385459, 1.954339820008679], [-0.00039068743229116323, 1.11865269324989, -0.2768748046941166, -0.2556487317363091, -0.8685303429739881, -1.9319896176934208]], [[-0.005969030182988597, 0.1773252149236631, -0.18337382735362176, 0.17728656418209596, -0.18335244024467748, 0.17727213206764175]]]
# noqa en theta = [[[2e-323, 2e-323, 2e-323, 2e-323, -2e-323, -2e-323], [0.00015785029375929775, -0.7240420090876171, -0.08621754361078793, 0.02029398274006565, 0.2870383754844149, 1.8251054382798797], [0.00015790723946104669, -0.7242384812503742, -0.08896512357458305, 0.020286424055462878, 0.2878190434802338, 1.8290107118267944], [0.00016085664233371553, -0.7323769800730814, -0.0830142281503349, 0.021594508967483467, 0.2975932613108389, 1.7800463694859192], [0.00015447382230296603, -0.7315693246953553, -0.06691234843038599, 0.01992035242283499, 0.28632492140160465, 1.8252199439416126], [0.00015459787939305005, -0.734310833360795, -0.06381535394991007, 0.020137767076279553, 0.2882849956522387, 1.8169511729252223]], [[0.0224797666268793, -0.1683741735459372, -0.16839230840372355, -0.16816089069970566, -0.16837149659532027, -0.1683320898580983]]]
# noqa hi theta = [[[-2e-323, 2e-323, 2e-323, -2e-323, 2e-323, 2e-323], [-6.744953916390573e-05, 1.3836336985258608, 1.029751808746444, 0.38688234125210236, -0.13185377289829223, -1.9296874191047546], [-7.884586472121509e-05, 1.3767083733874197, 1.0857400520009999, 0.3467962280149071, -0.13205905269398002, -1.8509026443658434], [5.258173298160592e-05, -1.2842238042916743, -1.0196682945520579, -0.33395443981633005, 0.1231003394898986, 1.7233241951231362], [-7.55243160712464e-05, 1.4277473486243466, 1.0628510988817796, 0.350880338985743, -0.1324325665684435, -1.8933407627296523], [5.409117222751138e-05, -1.3385737994179105, -0.9540046807956423, -0.34226659243197605, 0.1273568868355114, 1.6928597738005469]], [[0.04498480492447108, 0.20361492249561414, 0.20335697143072265, -0.1575908595521869, 0.20358369922702144, -0.15748571615492452]]]
# noqa ka theta = [[[-2e-323, 2e-323, 2e-323, 2e-323, 2e-323, 2e-323], [-0.0003042624234093845, 1.1831183567981607, 0.883186892928901, 0.5032044605350213, -0.266065258764445, -2.408692299969728], [-0.0002995660860113945, 1.18987993441264, 0.8826916391033076, 0.5129738594367326, -0.2651620508377627, -2.443210529044394], [-0.0002989023281075458, 1.1793274066815882, 0.8840324497057503, 0.5169635928008278, -0.26068338097585597, -2.448697337862049], [-0.0003045112450615721, 1.19169467824793, 0.8827013944870088, 0.503593058364966, -0.2727386200398259, -2.4063631613723118], [-0.00030030210129910345, 1.1734057660567485, 0.9022865423278127, 0.49905550138300325, -0.24742497351010667, -2.4519921865677103]], [[0.026197507680022863, 0.1806495548683328, 0.180851550923036, 0.18087213167810806, 0.18064675458129908, 0.18088292904057401]]]
# noqa kn theta = [[[2e-323, -2e-323, -2e-323, -2e-323, -2e-323, 2e-323], [-0.00013022200050319423, -1.2018255222059535, -1.2001399560550772, -0.3448805464970005, 0.11906234011447077, 1.5151722304903115], [-0.00012100652630693929, -1.2367076596788986, -1.206940977374956, -0.34977677559475745, 0.1249357493292009, 1.5106614118868316], [-0.0001267429077131275, -1.2074234599408353, -1.1460468511817143, -0.41454027811854993, 0.12771870707203498, 1.5455947704280404], [0.00012482763737173635, 1.3002765120387836, 1.2632526696468693, 0.37578797419935717, -0.11889022328290082, -1.6357407208984873], [-0.00012309353315669548, -1.1930101948790752, -1.2152630893241014, -0.3765461243736519, 0.12203663029666988, 1.55177815674505]], [[0.034607601734346335, -0.17010109415436112, -0.17016756973179045, -0.1701265139784474, 0.20541634345948262, -0.17026321403355565]]]
# noqa zh theta = [[[2e-323, -2e-323, 2e-323, -2e-323, -2e-323, 2e-323], [0.00019035459514230902, -0.9082258517233203, -0.25886822456148717, 0.08987874455188445, 0.08598584208857213, 1.9451724399904526], [-0.00020257613812040877, 0.8615911060633259, 0.2769176333048897, -0.08245872543789338, -0.011986007284251686, -2.247641144661896], [0.0001969640590186249, -0.8745200844545801, -0.29459387387164293, 0.09629968086462644, 0.06287929261376321, 1.965806415037164], [-0.0001969459047526024, 0.8406606909042396, 0.2937172990792201, -0.08357947700759873, 0.0009303155119195019, -2.2864875672787135], [0.00018131951110627996, -0.9050337576992619, -0.24713271231700135, 0.07432757547730334, 0.09780565932273658, 1.9606258060965427]], [[0.04486487857956735, -0.15708076361288315, 0.20369324421308285, -0.15723571725780358, 0.20391044485599893, -0.15715610734833196]]]
# noqa sa theta = [[[-2e-323, -2e-323, 2e-323, -2e-323, 2e-323, 2e-323], [0.00018018727276754518, 1.8612443417621956, 1.6881990463310226, 0.5489695188779775, 0.0727809469613696, -2.7375879091693727], [0.0001723769682237718, 1.9369155308646768, 1.7121507044007809, 0.5494181574710332, 0.0698515377859341, -2.7786272193726727], [0.00018971712657274374, 1.881105421450681, 1.6748224544554429, 0.5663695356733695, 0.07852572074993819, -2.8152710800792935], [0.00017786592702727401, 1.8516003083893657, 1.6874051949019713, 0.5724840831743147, 0.07399702260417879, -2.7747570243185367], [0.0002466631202662804, 1.639383119059833, 1.3453894609796138, 0.42233793506536643, 0.08240938391916743, -2.2594361835324532]], [[0.0011398812008037518, 0.17310854517036003, 0.1737213530187143, 0.17361506148445308, 0.1733198638551677, 0.16672242085827613]]]
theta = [
    [
        [-2e-323, 2e-323, -2e-323, 2e-323, 2e-323, 2e-323],
        [0.0002866305964814606, -0.8943729270254588, -0.5502521104862738, -0.32466016680671056, 0.18588244632092868, 2.7090804456227024],
        [0.00028874521130109113, -0.8883620661869525, -0.5475385942449733, -0.32139014913545433, 0.18168696204358573, 2.6893392701984027],
        [-0.0002904045686519801, 0.8931304529162672, 0.5503662755766398, 0.32061170232193453, -0.19028666651851756, -2.6694608229975767],
        [0.00028710905366480504, -0.8938001764933924, -0.5383380013458424, -0.33216988648927936, 0.18992161866328483, 2.6952171290275997],
        [-0.0002904532136481996, 0.8787680014258603, 0.5643110587648539, 0.32374481620276707, -0.18263724941475956, -2.6880223941139385]
    ],
    [
        [-0.0022423909057235287, -0.18217210473100906, -0.18203767562544887, 0.17965989206619548, -0.18207254484131732, 0.17979930150635967],
    ]
]


def forward(a, theta):
    sum_i = []
    for i in range(len(theta)):
        sum_i_2 = 0
        for j in range(len(a)):
            sum_i_2 += a[j]*theta[i][j]
        sum_i.append(sum_i_2)
    return sum_i


def sigmoid(a):
    return 1.0/(1 + math.exp(-1*a))


def kian(theta, case):
    z = [[]]*3
    a = [[]]*3
    a[0] = [1] + case
    z[1] = forward(a[0], theta[0])
    a[1] = [1] + [sigmoid(i) for i in z[1]][1:]
    z[2] = forward(a[1], theta[1])
    a[2] = [sigmoid(i) for i in z[2]]
    return a[2]


def check(name, list_of_ctas):
    set_of = [0, 0, 0, 0, 0]
    for cat in list_of_ctas:
        if cat in cats:
            a = cats[cat][2]
            if not a:
                set_of[-1] += 1
            elif a < 20.0:
                set_of[-2] += 1
            elif a <= 50.0:
                set_of[-3] += 1
            elif a <= 80.0:
                set_of[-4] += 1
            else:
                set_of[-5] += 1
    res = kian(theta, set_of)[0]
    rrres.append(res)
    if res > 0.5:
        f = codecs.open('%skian_res.txt' % base_dir, 'a', 'utf-8')
        f.write('\n%s' % name)
        f.close()

name = None
c = 0
for line in a[1:]:
    try:
        line.split('\t')[1]
    except:
        continue
    if name and name != line.split("\t")[0]:
        #print 'check'
        if name in humans_and_not:
            c += 1
            continue
        if u'快速删除候选' in a:
            a = []
            continue
        print 'Can work on it'
        check(name, a)
        a = []
    name = line.split("\t")[0]
    a.append(line.split("\t")[1])
rrres.sort()
f = codecs.open('%skian_res2.txt' % base_dir, 'w', 'utf-8')
f.write(str(rrres))
f.close()
print c
print rrres
