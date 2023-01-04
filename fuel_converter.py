
def liters_100km_to_miles_gallon(liters): 
    kms_per_mile=1.609344
    liters_per_gallon=3.785411784
    kms_per_liter=100/liters
    kms_per_gallon=kms_per_liter*liters_per_gallon
    miles_per_gallon=kms_per_gallon/kms_per_mile
    return miles_per_gallon


  
def miles_gallon_to_liters_100km(miles):
    kms_per_mile=1.609344
    liters_per_gallon=3.785411784
    gallons_per_100miles=100/miles
    gallons_per_100kms=gallons_per_100miles/kms_per_mile
    liters_per_100kms=gallons_per_100kms*liters_per_gallon
    return liters_per_100kms

print(liters_100km_to_miles_gallon(3.9))  # should be 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # should be 31.36194444444444
print(liters_100km_to_miles_gallon(10.))  # should be 23.52145833333333


print(miles_gallon_to_liters_100km(60.3))  # should be 3.9007393587617463
print(miles_gallon_to_liters_100km(31.4))  # should be 7.490910297239915
print(miles_gallon_to_liters_100km(23.5))  # should be 10.009131205673757


