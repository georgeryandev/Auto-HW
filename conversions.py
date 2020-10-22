import re
def convertTemperatures(values):
    for i in values:
        celsius_to_farenheit = re.search("C to F", str(i))
        celsius_to_kelvin = re.search("C to K", str(i))
        farenheit_to_celsius = re.search("F to C", str(i))
        farenheit_to_kelvin = re.search("F to K", str(i))
        kelvin_to_celsius = re.search("K to C", str(i))

        if(celsius_to_farenheit):
            #9/5 C +32
            start = celsius_to_farenheit.start()
            number = float(i[0:start])
            conversion = round(9/5*number+32,3)
            print(conversion)
            print("Formula Used: 9/5 C +32")
            print("\n")     
        elif(celsius_to_kelvin):
            start = celsius_to_kelvin.start()
            number = float(i[0:start])
            conversion = round(number + 273,3)
            print(conversion)
            print("Formula Used: C + 273")
            print("\n")    
        elif(farenheit_to_celsius):
            start = farenheit_to_celsius.start()
            number = float(i[0:start])
            #5/9(F-32)
            conversion = round(5/9*(number-32),3)
            print(conversion)
            print("Formula Used: 5/9(F-32)")
            print("\n")    
        elif(farenheit_to_kelvin):
            start = farenheit_to_kelvin.start()
            number = float(i[0:start])
            #Convert to celsius
            celsius = 5/9*(number-32)
            conversion = round(celsius+ 273,3)
            print(conversion)
            print("Formula Used: Convert F to C, then C+273")
            print("\n")    
        elif(kelvin_to_celsius):
            start = kelvin_to_celsius.start()
            number = float(i[0:start])
            #Convert to kelvin
            conversion = number-273
            print(conversion)
            print("Formula Used: K - 273")
            print("\n")    
        else:
            print("Not found. :(")
"""def convertLengths(values):

    feet_to_inches = re.search()
    inches_to_feet = re.search()
    m_to_mm = re.search()
    mm_to_m = re.search()
    mm_to_cm = re.search()
    cm_to_mm = re.search()
    cm_to_in = re.search()
    in_to_cm = re.search()
    km_to_m = re.search()
    m_to_km = re.search()
    yd_to_cm = re.search()
    cm_to_yd = re.search()
    
def convertVolumes(values):
    l_to_ml = re.search()
    ml_to_l = re.search()
    fl_oz_to_l = re.search()
def convertMass(values):
    g_to_kg = re.search()
    kg_to_g = re.search()
"""
#Initial Commit?