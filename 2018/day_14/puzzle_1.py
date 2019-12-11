#coding=utf8

#recipes = [0, 4, 7, 8, 0, 1]
recipes = [3, 7]

def elvf_move(recipes, elvf):
    score = recipes[elvf]
    steps = score + 1 + elvf
    elvf = steps % len(recipes)
    return elvf

if __name__ == '__main__':
    begin_length = len(recipes)
    elvfs = [i for i in range(2)]
    while len(recipes) < begin_length + 47801 + 10:
        # create new recipes
        new_recipe = sum([recipes[elvf] for elvf in elvfs])
        if new_recipe >= 10:
            recipes.append(new_recipe / 10)
            recipes.append(new_recipe - (new_recipe / 10) * 10)
        else:
            recipes.append(new_recipe)
        # elves move
        for i in range(len(elvfs)):
            elvfs[i] = elvf_move(recipes, elvfs[i])
    print recipes[47801:]
