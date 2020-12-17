#coding=utf8

def load_data(filename):
    with open(filename, 'r') as f:
        output = f.read().strip()
    flist = output.split('\n\n')
    rules = flist[0].split('\n')
    my_ticket = flist[1].split('\n')[1]
    nearby_tickets = flist[2].split('\n')[1:]
    rule_mapping = {}
    for rule in rules:
        rlist = rule.split(': ')
        field = rlist[0]
        values = rlist[1].split(' or ')
        constrains = []
        for value in values:
            for v in value.split('-'):
                constrains.append(int(v))
        rule_mapping[field] = constrains
    my_ticket = [int(code) for code in my_ticket.split(',')]
    nearby_tickets_list = []
    for ticket in nearby_tickets:
        nearby_tickets_list.append([int(code) for code in ticket.split(',')])
    return rule_mapping, my_ticket, nearby_tickets_list

def quiz_one(rules, nearby_tickets):
    qualified_numbers = set()
    for field in rules:
        rule = rules[field]
        qualified_numbers |= set(range(rule[0], rule[1]+1)) | set(range(rule[2], rule[3]+1))
    err_rate = 0; qualified_tickes = []
    for ticket in nearby_tickets:
        qualified = True
        for number in ticket:
            if number not in qualified_numbers:
                err_rate += number
                qualified = False
        if qualified:
            qualified_tickes.append(ticket)
    return err_rate, qualified_tickes

def quiz_two(rules, my_ticket, nearby_tickets):
    nearby_tickets = np.array(nearby_tickets)
    rules_mapping = {}
    for field in rules:
        rule = rules[field]
        rule = set(range(rule[0], rule[1]+1)) | set(range(rule[2], rule[3]+1))
        rules_mapping[field] = rule
    fields_cands = []
    for i in range(nearby_tickets.shape[1]):
        field_data = set(nearby_tickets[:,i])
        found_field = ''
        f_fields = []
        for field in rules_mapping:
            if len(field_data - rules_mapping[field]) == 0:
                f_fields.append(field)
        fields_cands.append(f_fields)

    fields = ['' for i in range(len(fields_cands))]
    while ('' in fields):
        for i, f in enumerate(fields_cands):
            if len(f) > 1:
                continue
            elif len(f) == 0:
                continue
            remove_value = f[0]
            for j in range(len(fields_cands)):
                if remove_value in fields_cands[j]:
                    fields_cands[j].remove(remove_value)
            fields[i] = remove_value
                
    multip = 1
    for i, field in enumerate(fields):
        if field.startswith('departure'):
            multip *= my_ticket[i]
    return multip

if __name__ == '__main__':
    import numpy as np
    rules, my_ticket, nearby_tickets = load_data('day_16.txt')
    res_1, qualified_tickes = quiz_one(rules, nearby_tickets)
    print (res_1)
    res_2 = quiz_two(rules, my_ticket, qualified_tickes)
    print (res_2)
