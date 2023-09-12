def roll_call_dwarves(dwarves):

    for i in range(len(dwarves)):
        print(f"{i+1}. {dwarves[i]}")
    


def summon_captain_planet(cartoons):
    new_list = [f"{cartoon.title()}!" for cartoon in cartoons]
    return new_list

def long_planeteer_calls(calls):
    call_length = False
    for call in calls:
        if len(call) > 4:
            call_length = True
    return call_length
    



def find_the_cheese(cheese_array):
    cheese_varieties = ["cheddar", "gouda", "camembert"]
    for cheese in cheese_varieties:
        if cheese in cheese_array:
            return cheese
        


