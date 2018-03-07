from random import choice

eyes = [":", ";", "X", ".", "|"]
noses = [">", "<", "D", "O", "-"]
mouths = ["D", ")", "(", "(", "p", "P"]

eye = choice(eyes)
nose = choice(noses)
mouth = choice(mouths)

print(eye, nose, mouth)
