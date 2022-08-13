#!/usr/bin/env python3

def mile_to_km(mile: float) -> int:
   bir_mile = 0.62137 # BUG fixed
   return int(mile*bir_mile)
def km_to_mile(km: int) -> float:
   bir_km = 1.6 # BUG fixed
   return km/bir_km

print("\t\tSEÇENEKLER")
print("\t\t KM TO MİL")
print("\t\t MİL TO KM")
print("\t\t yazabileceğin komutlar kmye çevirmek için km\nmile çevirmek için mil yazmanız gerekli")

while True:
    cvp = input("Neyi neyi çevirmek istiyorsunuz: ").lower()
    cvp = cvp.split()
    header = cvp[0]
    if not header == '':
       if header == "km":
          km = int(input("Kilometre giriniz: "))
          print("Girdiğiniz %s kilometre %s mil yapıyor" % (km,km_to_mile(km)))
       elif header == "mil":
          mil = float(input("Mil giriniz: "))
          print("Girdiğiniz %s mil %s kilometre yapıyor" % (mil,mile_to_km(mil)))
       else:
          print("Geçersiz cevap: %s " % (header))
    
