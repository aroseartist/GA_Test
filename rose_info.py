
first_name = raw_input('What\'s your first name? ')
last_name = raw_input('What is your last name? ')
favorite_color = raw_input('What is your favorite color? ')
how_many_pets = raw_input('How many pets do you have? ')

print 'It is wonderful to meet you %s %s. ' \
'I also think %s is a wonderful color, and hope to meet your %s friends someday.' \
% (first_name, last_name, favorite_color, how_many_pets)