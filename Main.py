from ORC import *
from WritingToDatabase import *
from vehiclesTypes import *

import json

filename_true = 'pic/true.jpg'
filename_false = 'pic/false.jpg'

for x in [1, 2]:
    # get the vehicle number from ORC with TRUE result
    if x == 1:
        orc_file = ocr_space_file(filename_true)
    else:
        # get the vehicle number from ORC with FALSE result
        orc_file = ocr_space_file(filename_false)

    js = json.loads(orc_file)
    vehicle_number = js['ParsedResults'][0]['ParsedText'].replace("\r\n", '')
    result = vehiclesTypes(vehicle_number)
    dataBase(vehicle_number, result[0], result[1])
