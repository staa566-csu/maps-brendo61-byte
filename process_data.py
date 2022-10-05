import pandas as pd

RAW_DATA = """AK - Alaska	11	1,290	43,372	237,042	$6,042,146
AL - Alabama	90	15,007	531,503	2,878,957	$68,481,334
AR - Arkansas	52	8,032	305,081	1,469,942	$30,446,114
AS - American Samoa	1	131	4,607	28,024	$68,160
AZ - Arizona	77	14,181	589,957	2,873,532	$89,697,762
CA - California	339	74,344	2,861,010	14,334,388	$502,216,842
CO - Colorado	60	8,431	380,409	1,867,500	$81,058,301
CT - Connecticut	35	8,722	341,341	1,779,025	$44,623,400
DC - Washington D.C.	7	2,188	85,801	560,383	$14,149,695
DE - Delaware	8	2,117	93,179	488,118	$8,989,003
FL - Florida	220	56,516	2,434,500	12,351,056	$389,451,470
GA - Georgia	112	22,998	898,991	5,135,870	$131,923,512
GU - Guam	3	407	9,732	78,413	$536,835
HI - Hawaii	14	2,533	81,569	498,169	$8,896,362
IA - Iowa	39	6,374	245,619	1,214,753	$28,154,818
ID - Idaho	18	2,644	110,380	504,938	$15,621,201
IL - Illinois	142	173,054	1,127,524	5,692,200	$164,456,172
IN - Indiana	100	15,696	632,900	3,114,867	$88,502,646
KS - Kansas	55	6,434	262,609	1,213,609	$38,340,906
KY - Kentucky	73	13,153	486,871	2,559,648	$67,760,200
LA - Louisiana	110	14,990	475,528	2,462,405	$63,190,349
MA - Massachusetts	72	14,353	678,637	3,584,627	$77,074,448
MD - Maryland	52	10,663	502,158	2,724,092	$20,239,460
ME - Maine	19	2,897	102,235	562,609	$13,560,290
MI - Michigan	103	22,940	940,857	4,667,497	$105,190,174
MN - Minnesota	55	10,363	450,497	2,206,466	$51,508,471
MO - Missouri	81	17,049	636,338	3,260,151	$80,111,159
MP - Northern Mariana Islands	1	74	3,384	15,548	$0
MS - Mississippi	70	9,897	310,495	1,506,938	$38,658,100
MT - Montana	17	2,248	75,849	363,588	$8,045,127
NC - North Carolina	110	22,907	955,481	5,110,294	$117,019,026
ND - North Dakota	10	2,030	73,723	371,768	$9,978,591
NE - Nebraska	27	4,404	156,834	804,912	$17,031,400
NH - New Hampshire	14	3,187	97,630	507,288	$15,630,024
NJ - New Jersey	78	20,578	853,236	4,327,244	$130,146,763
NM - New Mexico	37	3,805	156,690	782,856	$19,520,431
NV - Nevada	31	5,988	279,650	1,532,652	$55,522,761
NY - New York	187	57,526	2,019,760	11,450,940	$296,059,116
OH - Ohio	151	27,974	1,189,745	5,768,174	$168,907,266
OK - Oklahoma	91	10,043	399,032	1,956,919	$54,816,129
OR - Oregon	36	6,278	280,843	1,432,749	$31,717,122
PA - Pennsylvania	182	34,890	1,385,260	6,929,273	$231,616,128
PR - Puerto Rico	53	8,015	250,855	1,510,038	$4,439,932
RI - Rhode Island	11	2,434	101,213	520,769	$10,572,625
SC - South Carolina	66	11,270	493,422	2,514,100	$72,490,971
SD - South Dakota	24	2,805	95,891	427,693	$14,142,115
TN - Tennessee	97	18,791	759,894	3,913,419	$98,535,257
TX - Texas	373	59,929	2,577,147	13,120,843	$395,621,977
UT - Utah	36	4,896	208,878	880,555	$24,791,361
VA - Virginia	90	17,699	678,748	3,577,410	$94,811,361
VI - Virgin Islands	2	226	5,229	32,446	$256,891
VT - Vermont	7	867	35,617	198,281	$5,033,877
WA - Washington	60	10,143	465,016	2,538,520	$72,795,029
WI - Wisconsin	87	11,075	449,608	2,260,765	$67,389,734
WV - West Virginia	34	5,367	193,605	1,055,661	$22,875,685
WY - Wyoming	14	1,262	29,282	122,474	$3,444,658
TOTAL	3,944	894,115	29,895,222	153,882,398	$4,272,160,687"""

DOCS_PER_CAP = """United States	278.49
Alabama	223.32
Alaska	259.16
Arizona	245.76
Arkansas	212.61
California	273.41
Colorado	288.57
Connecticut	360.73
Delaware	257.70
District of Columbia	672.22
Florida	264.63
Georgia	226.70
Hawaii	300.92
Idaho	188.43
Illinois	287.09
Indiana	227.39
Iowa	215.30
Kansas	252.75
Kentucky	241.20
Louisiana	276.63
Maine	325.49
Maryland	363.63
Massachusetts	435.38
Michigan	303.71
Minnesota	307.13
Mississippi	194.14
Missouri	276.54
Montana	243.31
Nebraska	255.83
Nevada	203.99
New Hampshire	313.64
New Jersey	317.42
New Mexico	239.67
New York	369.76
North Carolina	257.87
North Dakota	240.53
Ohio	297.29
Oklahoma	209.56
Oregon	296.04
Pennsylvania	328.25
Rhode Island	407.47
South Carolina	234.15
South Dakota	241.50
Tennessee	263.69
Texas	228.35
Utah	226.04
Vermont	382.43
Virginia	268.53
Washington	270.70
West Virginia	261.02
Wisconsin	266.39
Wyoming	196.37"""


def hospital_counts():
    # trim last line
    # and remove state abbreviations
    # and split by tabs
    # and only care about state and hospital
    # and format back to str object separated by commas
    data = "\n".join([','.join(line[5:].split("\t")[:2]) for line in RAW_DATA.splitlines()[:-1]]).lower()
    data = f"state, hospital_count\n{data}"

    with open("hospital_count.csv", 'w') as f:
        f.write(data)


def life_expectancy():
    mapping1 = {pair[0]: pair[1] for pair in [line.split("\t")[0].lower().split('-') for line in RAW_DATA.splitlines()[:-1]]}

    mapping = {}
    for i, j in mapping1.items():
        mapping[i.replace(" ", "")] = j[1:]

    new_contents = []
    with open('Life_Expectancy_at_Birth_by_State.csv', 'r') as f:
        for line in f.read().splitlines()[1:]:
            split_line = line.split(",")
            state = mapping[split_line[1].lower()]
            new_contents.append(f'{state},{split_line[2]}')

    with open('Life_Expectancy_at_Birth_by_State_corrected.csv', 'w') as f:
        f.write('STATE,RATE\n')
        f.write('\n'.join(new_contents))


def docs_per_cap():
    data = ['state, doc_per_100k']
    for line in DOCS_PER_CAP.splitlines()[1:]:
        s = line.split("\t")
        data.append(','.join(s).lower())

    with open('docs_per_cap.csv', 'w') as f:
        f.write("\n".join(data))


def empty_file():
    new_contents = []
    with open('Life_Expectancy_at_Birth_by_State.csv', 'r') as f:
        for line in f.read().splitlines()[1:]:
            split_line = line.split(",")
            state = split_line[1].lower()
            new_contents.append(f'{state},')

    with open('average_time_to_see_doc_at_hos.csv', 'w') as f:
        f.write('STATE,TIME\n')
        f.write('\n'.join(new_contents))


def wait_time_corrected():
    mapping1 = {pair[0]: pair[1] for pair in [line.split("\t")[0].lower().split('-') for line in RAW_DATA.splitlines()[:-1]]}

    mapping = {}
    for i, j in mapping1.items():
        mapping[i.replace(" ", "")] = j[1:]

    new_contents = []
    with open('average_time_to_see_doc_at_hos.csv', 'r') as f:
        for line in f.read().splitlines()[1:]:
            split_line = line.split(",")
            state = mapping[split_line[0].lower()]
            new_contents.append(f'{state},{split_line[1]}')

    with open('average_time_to_see_doc_at_hos_corrected.csv', 'w') as f:
        f.write('STATE,TIME\n')
        f.write('\n'.join(new_contents))


if __name__ == '__main__':
    # hospital_counts()
    # life_expectancy()
    # docs_per_cap()
    # empty_file()
    wait_time_corrected()
