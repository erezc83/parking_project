"""
function that gets the vehicle number from main
and defines what type of vehicle it is.
"""
vehicle_number = 0
vehicle_type = None
allowed = None


# defines what type of vehicle
def vehiclesTypes(vec_num):
    global vehicle_number, vehicle_type, allowed, temp
    vehicle_number = vec_num
    temp = 0
    str_find = "1234567890"
    length_number = vehicle_number.__len__()

    heb_char = vehicle_number[-1]  # last char on the the vehicle number

    # Temporary variable after deleting value hebrew char.
    if str_find.find(heb_char) == -1:
        temp = str(vec_num).replace(heb_char, '')

    temp_vec_num = str(temp).replace('-', '')  # Temporary variable after deleting value "-"

    Last_two_digits = int(temp_vec_num) % 100  # Finding the last 2 digits of the number
    length = temp_vec_num.__len__()
    number_vehicle = int(temp_vec_num)

    # Public transportation vehicles - their license plates always end with 25 or 26.
    if Last_two_digits == 25 or Last_two_digits == 26:
        vehicle_type = "public transportation"
        allowed = 0
        # print(vehicle_number, vehicle_type, allowed)
        return vehicle_type, allowed

    # Old vehicle - 7 digits numbers which their two last digits are 85/86/87/88/89/00.
    elif length == 7 and (84 < Last_two_digits < 90 or Last_two_digits == 0):
        vehicle_type = "Old vehicle"
        allowed = 0
        # print(vehicle_number, vehicle_type, allowed)
        return vehicle_type, allowed

    # Military and law enforcement vehicles - include an Hebrew letter
    elif str_find.find(heb_char) == -1:
        vehicle_type = "military or law enforcement"
        allowed = 0
        # print(vehicle_number, vehicle_type, allowed)
        return vehicle_type, allowed

    # if seven or eight digits license plate numbers which their digits sum divided by 7
    elif 6 < length < 9:
        if number_vehicle % 7 == 0:
            vehicle_type = "gas"
            allowed = 0
            # print(vehicle_number, vehicle_type, allowed)
            return vehicle_type, allowed
        else:
            vehicle_type = "normal vehicle"
            allowed = 1
            # print(vehicle_number, vehicle_type, allowed)
            return vehicle_type, allowed
    else:
        vehicle_type = "normal vehicle"
        allowed = 1
        # print(vehicle_number, vehicle_type, allowed)
        return vehicle_type, allowed
