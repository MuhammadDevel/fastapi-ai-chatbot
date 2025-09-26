import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+917394516271")
phone_number2 = phonenumbers.parse("+918878586271")
phone_number3 = phonenumbers.parse("+12136574429")
phone_number4 = phonenumbers.parse("+201234567890")

print("\nPhone Numbers Location\n")

print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4, "en"))
#LETS TRACK PHONE NUMBERS