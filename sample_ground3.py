spades = ['as', 'ks', 'qs', 'js', '10s', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s']
clubs = ['ac', 'kc', 'qc', 'jc', '10c', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']
diamonds = ['ad', 'kd', 'qd', 'jd', '10d', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d']
hearts = ['ah', 'kh', 'qh', 'jh', '10h', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h']

suits = [spades, clubs, diamonds, hearts]
allCards = [spades + clubs + diamonds + hearts]

availableCards = [['as', 'ks'], ['qs', 'js', '10s'], ['ks', 'qs', 'js'], ['10s', '9s']]

spadesForOpponent = spades

spadesForOpponent.remove('as')

print spadesForOpponent
print spades
