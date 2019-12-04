# %%

first_wire_string = "R994,U598,L555,D997,R997,U529,L251,U533,R640,U120,L813,U927,L908,U214,L276,U306,L679,U187,R156,D654,L866,D520,R299,U424,R683,U49,R965,U531,R303,D4,L210,U425,R99,D892,R564,D671,L294,D908,L89,U855,R275,U790,R214,D588,L754,D873,R297,D97,R979,U850,L953,D281,L580,D254,L747,U115,L996,U641,R976,U585,L383,U498,L112,U329,R650,U772,L952,U325,L861,U831,R71,D853,R696,D812,R389,U456,L710,D116,R789,D829,L57,D940,R908,U569,R617,D832,L492,D397,R152,U898,L960,D806,L867,U928,L617,D281,L516,D214,R426,U530,R694,U774,L752,U215,L930,U305,R463,U774,R234,U786,R425,U470,R90,D383,R692,D626,L160,D588,L141,D351,R574,D237,L869,D499,R873,U856,R148,D919,L582,D804,L413,U201,L247,U907,L828,D279,L28,D950,L587,U290,R636,U344,L591,U118,L614,U203,R381,U634,L301,D197,R594,D373,L459,U504,L703,U852,L672,U613,R816,D712,R813,U97,R824,D690,L556,D308,L568,D924,L384,U540,R745,D679,R705,D808,L346,U927,R145,U751,L769,D152,L648,D553,L738,U456,R864,U486,R894,D923,R76,U211,L78,U145,R977,U297,R93,U200,L71,U665,L392,D309,L399,D594,R118,U552,L328,U317,R369,D109,L673,D306,R441,U836,L305,D59,L870,U648,L817,D381,R676,U711,R115,U344,L815,U286,R194,U526,R844,U106,L547,D312,L116,U783,R786,D390,L115,D483,R691,U802,R569,U13,R854,D90,R22,D819,L440,D13,R438,D640,L952,D394,R984,D825,R1,D554,R349,U746,L816,U301,L397,D85,R437,D746,L698,D75,L964,U155,L268,U612,R838,D338,L188,U38,R830,U538,L245,D885,R194,D989,R8,D69,L268,D677,R163,U784,L308,U605,L737,U919,R117,U449,R698,U547,L134,D860,L234,U923,R495,D55,R954,D531,L212"
second_wire_string = "L1005,D937,L260,D848,R640,U358,R931,U495,R225,U344,R595,U754,L410,D5,R52,D852,L839,D509,R755,D983,R160,U522,R795,D465,R590,U558,R552,U332,R330,U752,R860,D503,L456,U254,R878,D164,R991,U569,R44,U112,L258,U168,L552,U68,R414,U184,R458,D58,R319,U168,R501,D349,R204,D586,R241,U575,L981,D819,L171,D811,L960,U495,R192,D725,R718,D346,R399,D692,L117,D215,L390,U364,L700,D207,R372,U767,L738,D844,L759,D211,R287,U964,R328,D800,R823,U104,L524,D68,R714,D633,R565,D373,R883,U327,R222,D318,L58,D451,R555,D687,R807,U638,L717,U298,R849,D489,L159,D692,L136,U242,R884,U202,R419,U41,L980,U483,R966,D513,L870,D306,R171,D585,R71,D320,R914,U991,R706,U440,R542,D219,L969,U9,R481,U164,R919,U17,L750,U775,R173,U515,L191,D548,L515,U54,L132,U56,R203,U544,L796,D508,L321,D517,L358,U12,L892,D472,L378,U121,L974,U36,R56,D758,L680,D17,L369,D72,L926,D466,L866,U850,R300,D597,L848,U17,L890,D739,L275,U560,L640,U602,R238,U919,R636,D188,R910,D992,L13,U241,R77,U857,R453,U883,L881,D267,R28,U928,R735,U731,L701,D795,R371,U652,R416,D129,R142,D30,R442,U513,R827,U455,L429,D804,R966,D565,R326,U398,R621,U324,L684,D235,L467,D575,L200,D442,R320,D550,R278,U929,R555,U537,L416,U98,R991,D271,L764,U841,L273,D782,R356,D447,R340,U413,R543,U260,L365,D529,R721,U542,L648,U366,R494,U243,L872,U201,L440,U232,R171,D608,R282,U484,R81,D320,R274,D760,L250,U749,L132,D162,L340,D308,L149,D5,L312,U547,R686,D684,R133,D876,L531,U572,R62,D142,L218,U703,L884,U64,L889,U887,R228,U534,R624,D524,R522,D452,L550,U959,R981,U139,R35,U98,R212"

test1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
test2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

# first_wire_string = test1
# second_wire_string = test2

first_wire = first_wire_string.split(",")
second_wire = second_wire_string.split(",")


def tuppleize(wire):
    tupples = []
    for w in wire:
        direction = w[0]
        steps = int(w[1 : len(w)])
        tupples.append((direction, steps))
    return tupples


first_tupples = tuppleize(first_wire)
second_tupples = tuppleize(second_wire)



# %%
# calculate the max up, min down and max right min left
import math
import numpy as np

def calculateDimensions(tuples):
    current_location = np.array([0, 0])  # (y,x)
    minimums = np.array([math.inf, math.inf])
    maximums = np.array([0,0])

    for t in tuples:
        direction = t[0]
        steps = t[1]
        if direction == "R":
            current_location[1] = current_location[1] + steps
        elif direction == "L":
            current_location[1] = current_location[1] - steps
        elif direction == "U":
            current_location[0] = current_location[0] + steps
        elif direction == "D":
            current_location[0] = current_location[0] - steps

        minimums = np.minimum(current_location, minimums)
        maximums = np.maximum(current_location, maximums)
    return minimums, maximums

first_minimums, first_maximums = calculateDimensions(first_tupples)
second_minimums, second_maximums = calculateDimensions(second_tupples)

print(first_minimums,first_maximums,second_minimums,second_maximums)

# %%
#create a numpy array where both wires can fit

minimums = np.minimum(first_minimums,second_minimums).astype(int) * 2 #for some reason the dimensions are too small still..
maximums = np.maximum(first_maximums,second_maximums).astype(int) * 2 #for some reason the dimensions are too small still..

numpy_dimensions = maximums - minimums
print(numpy_dimensions)

centroid = np.array([0,0]) - minimums
orig_centroid = centroid.copy()
# %%

first_numpy = np.zeros((numpy_dimensions[0],numpy_dimensions[1]))
second_numpy = np.zeros((numpy_dimensions[0],numpy_dimensions[1]))

print(first_numpy.shape) #y,x
print(second_numpy.shape) #y,x

from skimage.draw import line


def drawLine(current_location, new_location, drawing):
    rr, cc = line(current_location[0], current_location[1], new_location[0], new_location[1])
    drawing[rr, cc] = 1
    return drawing

def drawWires(tuples, drawing, centroid):
    current_location = centroid.copy()

    count = 0
    for t in tuples:
        count = count + 1
        direction = t[0]
        steps = t[1]

        y,x = current_location[0],current_location[1]
        y1,x1 = current_location[0],current_location[1]
    
        if direction == "R":
            x1 = x1 + steps
        elif direction == "L":
            x1 = x1 - steps
        elif direction == "U":
            y1 = y1 + steps
        elif direction == "D":
            y1 = y1 - steps
        else:
            raise ValueError("Encountered a weird direction: {}".format(direction))

        
        drawing = drawLine([y,x],[y1,x1],drawing)
        current_location = [y1,x1]

    return drawing    

first_drawing = drawWires(first_tupples,first_numpy,centroid)
second_drawing = drawWires(second_tupples,second_numpy,centroid)



# %%
total = first_drawing + second_drawing

ii = np.where(total == 2)
tpls = tuple(zip(*ii))


# %%
min_dist = math.inf
tpls_cleaned = []
for tpl in tpls:
    location = np.array([tpl[0],tpl[1]])
    distance = abs(location - centroid)

    print(distance)
    #get the smalles non-zero distance
    if distance.sum() > 0:
        min_dist = min(distance.sum(),min_dist)
        print(np.minimum(min_dist,distance))
        tpls_cleaned.append(location)

print("The manhattan dinstance = {}".format(min_dist))
# %%
#part 2
def calculateTotalDistance(tuples, checks, centroid):
    current_location = centroid.copy()  # (y,x)
    minimums = np.array([math.inf, math.inf])
    maximums = np.array([0,0])

    #for part 2
    total_steps = 0
    returned_checks = []

    for t in tuples:
        direction = t[0]
        steps = t[1]

        y,x = current_location[0],current_location[1]
        y1,x1 = current_location[0],current_location[1]

        if direction == "R":
            x1 = x1 + steps
        elif direction == "L":
            x1 = x1 - steps
        elif direction == "U":
            y1 = y1 + steps
        elif direction == "D":
            y1 = y1 - steps  

        print([y,x],[y1,x1])

        for check in checks:
            yc = check[0]
            xc = check[1]
            
            if (x == xc and ((y < yc < y1) or (y > yc > y1))):
                extra_steps = abs(yc- y)
                returned_checks.append((total_steps + extra_steps,check))
            elif (y == yc and ((x < xc < x1) or (x > xc > x1))):
                extra_steps = abs(xc- x)
                returned_checks.append((total_steps + extra_steps,check))

        total_steps = total_steps + steps
        current_location = [y1,x1]
        
        minimums = np.minimum(current_location, minimums)
        maximums = np.maximum(current_location, maximums)
    return minimums, maximums, returned_checks

# %%
print(tpls_cleaned)

_, _, first_returned_checks = calculateTotalDistance(first_tupples,tpls_cleaned,centroid)
_, _, second_returned_checks = calculateTotalDistance(second_tupples,tpls_cleaned,centroid)

print("Result")
print(first_returned_checks)
print(second_returned_checks)

min_dist = math.inf
for t in tpls_cleaned:
    dist = 0
    for f in first_returned_checks:
        cross_over = f[1]
        if np.array_equal(t, cross_over):
            dist += f[0]
    for s in second_returned_checks:
        cross_over = s[1]
        if np.array_equal(t, cross_over):
            dist += s[0]
    min_dist = min(min_dist,dist)
print(min_dist)
# %%
