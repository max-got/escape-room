
R = [255, 0, 0]  # Red
G = [0, 255, 0]  # Green
O = [0, 0, 0]  # Black

symbols = {
"up" : [
    O, O, O, R, R, O, O, O,
    O, O, R, R, R, R, O, O,
    O, R, O, R, R, O, R, O,
    R, O, O, R, R, O, O, R,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O
],
"down": [
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    R, O, O, R, R, O, O, R,
    O, R, O, R, R, O, R, O,
    O, O, R, R, R, R, O, O,
    O, O, O, R, R, O, O, O
],
"right":[
    O, O, O, O, R, O, O, O,
    O, O, O, O, O, R, O, O,
    O, O, O, O, O, O, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, O, O, O, O, O, R, O,
    O, O, O, O, O, R, O, O,
    O, O, O, O, R, O, O, O
],

"left":[
    O, O, O, R, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, R, O, O, O, O, O, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, O, O, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, O, O, R, O, O, O, O
],

"middle":[
    O, O, O, O, O, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, R, R, R, R, O, O,
    O, R, R, R, R, R, R, O,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, O, O, O, O, O
],
}

checkmark = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, G,
    O, O, O, O, O, O, G, O,
    G, O, O, O, O, G, O, O,
    O, G, O, O, G, O, O, O,
    O, O, G, G, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

x = [
    R, O, O, O, O, O, O, R,
    O, R, O, O, O, O, R, O,
    O, O, R, O, O, R, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, R, O, O, R, O, O,
    O, R, O, O, O, O, R, O,
    R, O, O, O, O, O, O, R
]