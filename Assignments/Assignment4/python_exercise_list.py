## Python Exercise Lists

#3.1
names = ["Abubakar","Umar","Usman","Ali"]

for name in names:
    print(name)

#3.2
for name in names:
    print("Hello {},".format(name))

#3.3
statements = ["I would like to own a BMW car.","I would like to own a Audi car.","I would like to own a Honda car."]

for statement in statements:
    print(statement)

#3.4
guest_list = ["Akhlaq","Abdur Rehman","Qasim"]
message = "Hello {}, i would like to invite you on dinner"

for guest in guest_list:
    print(message.format(guest))



#3.5
guest_list = ["Akhlaq","Abdur Rehman","Qasim"]
message_invitation = "Hello {}, i would like to invite you on dinner"
message_not_attending = "{} couldn't attend the dinner"


print(message_not_attending.format(guest_list[0]))


guest_list[0] = "Ansar"

for guest in guest_list:
    print(message.format(guest))




#3.6
guest_list = ["Akhlaq","Abdur Rehman","Qasim"]
message_invitation = "Hello {}, i would like to invite you on dinner"
message_not_attending = "{} couldn't attend the dinner"

guest_list[0] = "Ansar"

print("I have found a bigger table and i will be inviting more people.")

#Start
guest_list.insert(0,"Farooq")

#Middle
guest_list.insert(2,"Hassaan")

#Last
guest_list.append("Ihsan")

for guest in guest_list:
    print(message_invitation.format(guest))


#3.7
guest_list = ["Akhlaq","Abdur Rehman","Qasim"]
message_invitation = "Hello {}, i would like to invite you on dinner"
message_not_attending = "{} couldn't attend the dinner"
message_invited = "Hello {}, you are still invited to the dinner"

guest_list[0] = "Ansar"

print("I will be inviting only 2 people.")

#Start
guest_list.insert(0,"Farooq")

#Middle
guest_list.insert(2,"Hassaan")

#Last
guest_list.append("Ihsan")

# for guest in guest_list:
#     print(message_invitation.format(guest))



while len(guest_list) > 2:
    guest_list.pop()



for guest in guest_list:
    print(message_invited.format(guest))

print(guest_list)

guest_list.clear()

print(guest_list)


#3.8
locations = ["Kandahar","Baku","Silicon Valley","Chicago","Palo Alto"]

print(locations)

print(sorted(locations))

print(locations)

print(sorted(locations, reverse=True))

print(locations)

locations.reverse()

print(locations)

locations.reverse()

print(locations)

locations.sort()

print(locations)

locations.sort(reverse=True)

print(locations)


#3.9
cities = ["Lahore","Islamabad","Landi Kotal", "Miranshah","Faisalabad","Abottabad"]

#i 
for city in cities:
    print(city)

#ii
message = "{} is a beautiful city"

for city in cities:
    print(message.format(city))

#iii
cities.insert(0,"Okara")

print(cities)

#iv
cities.insert(3,"Nawabshah")

print(cities)

#v
cities.append("Sukkur")

#vi
cities.pop(4)

print(cities)

#vii
print(sorted(cities))

print(cities)

#viii
print(sorted(cities, reverse=True))

print(cities)

#ix
print(sorted(cities, reverse=True))

#x
cities.reverse()

print(cities)

#xi
cities.sort()

print(cities)

#xii
cities.sort(reverse=True)

print(cities)


#3.10
cities = ["Lahore","Islamabad","Landi Kotal", "Miranshah","Faisalabad","Abottabad"]

print(cities)

cities.pop(5)

print(cities[5])
