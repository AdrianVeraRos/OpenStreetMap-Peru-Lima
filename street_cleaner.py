#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


expected_st_names = ["Avenida", "Óvalo".decode('utf-8'), "Jirón".decode('utf-8'), "Calle", "Malecón".decode('utf-8'),
                     "Pasaje", "Alameda", "Carretera", "Pasillo", "Prolongación".decode('utf-8'),
                     "Parque", "Camino", "Paseo", "Plaza"]

street_type_re = re.compile(r'^\w+', re.IGNORECASE|re.U)

street_name_mapping = { "Av.":"Avenida", "av.":"Avenida", "avenida":"Avenida", "Avenia":"Avenida",
                       "Av.enida":"Avenida", "Avienda":"Avenida", "Abenida":"Avenida",
                        "Ca." : "Calle", "calle" : "Calle", "Call" : "Calle", "Calleo" : "Calle", "Calles" : "Calle",
                        "Jr." : "Jirón".decode('utf-8'), "Jiron" : "Jirón".decode('utf-8'),
                        "Jirón11".decode('utf-8'): "Jirón".decode('utf-8'),
                        "Malecon" : "Malecón".decode('utf-8'), "malecón".decode('utf-8'):"Malecón".decode('utf-8'),
                        "Ovalo" : "Óvalo".decode('utf-8'), "Pj." : "Pasaje", "Psje." : "Pasaje", "pasaje" : "Pasaje",
                        "Prolongacion":"Prolongación".decode('utf-8')}

def update_name(name, street_name_mapping):
    m = street_type_re.search(name)
    if m and m.group() in street_name_mapping:
        name = re.sub(street_type_re, street_name_mapping[m.group()], name)
    return name