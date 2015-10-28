# -*- coding: utf-8 -*-

import re 
from collections import OrderedDict
import simplejson as json


region = ['东城区','西城区','崇文区','宣武区','朝阳区','海淀区','丰台区','石景山区','通州区','平谷区','顺义区','怀柔区','昌平区','门头沟区','房山区','大兴区','密云县','延庆县']
years = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997']
jobs = ['送餐','保洁','家教','分拣','快递']


region_mat = []
for i in jobs:
	dic = OrderedDict()
	dic['text'] = i
	dic['checked'] = False

	region_mat.append(dic)

print json.dumps(region_mat)

