# Solution
def max_duffel_bag_value(cake_tuples, weight_capacity):
    # we make a list to hold the maximum possible value at every duffel bag weight capacity from 0 to weight_capacity
    # starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in range(weight_capacity + 1):
        current_max_value = 0
        for cake_weight, cake_value in cake_tuples:
            # if a cake weighs 0 and has a positive value the value of our duffel bag is infinite!
            if (cake_weight == 0 and cake_value != 0):
                return float('inf')

            # if we use the cake, the most kilograms we can include in addition to the cake we're adding is the
            # current capacity minus the cake's weight.
            if (cake_weight <= current_capacity):
                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]

                # now we see if it's worth taking the cake. How's value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake, current_max_value)

        # add each capacity's max value to our list so we can use them  when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value
        print('capacity {}: {}'.format(current_capacity, max_values_at_capacities))

    return max_values_at_capacities[weight_capacity]


def max_duffel_bag_value(cake_tuples, weight_capacity):
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in range(weight_capacity + 1):
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples:
            if (cake_weight == 0 and cake_value != 0):
                return float('inf')
            if (cake_weight <= current_capacity):
                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]
                current_max_value = max(max_value_using_cake, current_max_value)

        max_values_at_capacities[current_capacity] = current_max_value
        print('capacity {}: {}'.format(current_capacity, max_values_at_capacities))

    return max_values_at_capacities[weight_capacity]

"""
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20
print(max_duffel_bag_value(cake_tuples, capacity))
# returns 555 (6 of the middle type of cake and 1 of the last type of cake)

Solution:
1) Take best ratio until not possible... but this suboptimizes

2) Greedy... if we have 1 kg what is the best answer? 
Figure out best we can do at each kg bottom up
"""

def best_profit(cake_tuples, capacity):
    best_at_kg = [0] * (capacity+1)

    for cur_kg in range(len(best_at_kg)):
        # Find max val at each kg
        max_profit_at_kg = 0

        for cake_kg, cake_val in cake_tuples:
            if cake_kg <= cur_kg:
                # if we can take it calc the best payoff
                # e.g. if kg = 10 and we take a 4 kg cake, then our profit is the 4kg cake + best we did at 6kg
                profit_w_cur_cake = cake_val + best_at_kg[cur_kg - cake_kg]
                max_profit_at_kg = max(max_profit_at_kg, profit_w_cur_cake)

        best_at_kg[cur_kg] = max_profit_at_kg

        print(best_at_kg)

    return best_at_kg[-1]

print(best_profit([(7, 160), (3, 90), (2, 15)], 20))


"""
Notes:
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20


max so far
1 kg... ans = C    find the best 1kg cake
2 kg... ans = C2   
	at each cake...
	   if cake weights 2...	take it and done
	   if cakes weights 1...	take it and 1kg left *** we know 1kg's best ans
           how's this answer compared to prev max?

	cake1 cake2 cake3...
    max  x      y     z
         calc x y z by doing  max of prev max or take cake + best_at[current kg - cake.weight] 

3 kg... ans =      find best 3kg cake
	if cake weights 3...	take it and done
	if cake weights 2...	take it and 2kg left *** we know 2kg's best ans
	if cake weights 1...	take it and 1kg left *** we know 1kg's best ans
.
.
.


best_val_at_kg = [_, _, _, _, ...]
best_val_at_kg = [x0,x1,x2,..,]

for k in kg:
	cur max = -inf
	
	# Find the best after considering each cake
	for cur_cake.cake in cake_shop:
		cur
		option1 = best_val_at_kg[k - cur_cake.weight] + cur_cake.value
		best_you_can_do = max(current)

"""