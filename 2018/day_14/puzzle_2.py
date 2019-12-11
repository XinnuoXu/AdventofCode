#coding=utf8

recipes = [3, 7]
input = [0, 4, 7, 8, 0, 1]
#input = [0, 4, 7, 8, 0]
#input = [5,9,4,1,4]

def elvf_move(recipes, elvf, len_recipes):
    score = recipes[elvf]
    steps = score + 1 + elvf
    elvf = steps % len_recipes
    return elvf

if __name__ == '__main__':
    elvfs = [i for i in range(2)]; len_elvf = len(elvfs)
    len_recipes = len(recipes)
    len_input = len(input)
    
    while len_recipes < len(input):
        # create new recipes
        new_recipe = sum([recipes[elvf] for elvf in elvfs])
        if new_recipe >= 10:
            recipes.append(new_recipe / 10)
            recipes.append(new_recipe - (new_recipe / 10) * 10)
            len_recipes += 2
        else:
            recipes.append(new_recipe)
            len_recipes += 1
        # elves move
        for i in range(len_elvf):
            elvfs[i] = elvf_move(recipes, elvfs[i], len_recipes)
    while 1:
        # create new recipes
        new_recipe = sum([recipes[elvf] for elvf in elvfs])
        if new_recipe >= 10:
            recipes.append(new_recipe / 10)
            len_recipes += 1
            if recipes[-len_input:] == input:
                break
            recipes.append(new_recipe - (new_recipe / 10) * 10)
            len_recipes += 1
            if recipes[-len_input:] == input:
                break
        else:
            recipes.append(new_recipe)
            if recipes[-len_input:] == input:
                break
            len_recipes += 1
        # elves move
        for i in range(len_elvf):
            elvfs[i] = elvf_move(recipes, elvfs[i], len_recipes)
    print len_recipes - len(input)
