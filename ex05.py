name = "Jet Pack"
age = 66
height = 72 # inches
weight = 230 # pounds
eyes = "Hazelnut Brown"
teeth = "White-ish"
hair = "Salt n Pepper"
# unit conversion

height_cm = height * 2.54
weight_kg = weight * 0.454

# %s, %d, %r are all Formatters
print "Let's talk about %s." % name
print "He's %r inches tall." % height
print "That is %r centimetres." % height_cm
print "He's %d lbs soaking wet." % weight
print "If you're not American, that would come up to %0.02f kilograms." % round(weight_kg)
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d, and %d, I'd get %d." % (age, height, weight, age+height+weight)