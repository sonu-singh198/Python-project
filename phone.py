import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your number with +__: ")
phone = phonenumbers.parse(number)  # Parses the input number
time = timezone.time_zones_for_number(phone)  # Gets the time zone
car = carrier.name_for_number(phone, "en")  # Gets the carrier name
reg = geocoder.description_for_number(phone, "en")  # Gets the region

print(f"Phone: {phone}")
print(f"Time Zone: {time}")
print(f"Carrier: {car}")
print(f"Region: {reg}")

