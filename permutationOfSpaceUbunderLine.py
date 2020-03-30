def supply():
    result = {'($millions)':'_', '($m)†':'_', '($m)':'_', '$(m)':'_', '&':'_', '-':'_', '%':'_'}
    # BASE = {'rank in':'',  \
    #     'preparation rank':'preparation', \
    #     'programme design rank':'programme_design', \
    #     'programme design':'programme_design', \
    #     'teaching methods materials':'teaching_materials', \
    #     'teaching methods':'teaching_materials', \
    #     'teaching materials':'teaching_materials', \
    #     'teaching methods materials rank':'teachingmaterials', \
    #     'faculty rank':'faculty', \
    #     'new skills learning rank':'new_skills_learning', \
    #     'follow up rank':'follow_up', \
    #     'aims achieved rank':'aims_achieved', \
    #     'facilities rank':'facilities', \
    #     'value for money rank':'value_for_money', \
    #     'future use rank':'future_use', \
    #     'over seas programmes rank':'overseas_programmes', \
    #     'faculty diversity rank':'faculty_diversity', \
    #     'food accommodation rank':'food_accommodation', \
    #     'international participants rank':'international_participants', \
    #     'repeat business growth rank':'repeat_business_growth', \
    #     'international location rank':'international_location', \
    #     'partner schools rank':'partner_schools'}
    # BASE = {'rank in':'',  \
    #         'preparation rank':'preparation', \
    #         'programme design':'programme_design', \
    #         'teaching methods':'teaching_materials', \
    #         'teaching materials':'teaching_materials', \
    #         'faculty rank':'faculty', \
    #         'facilities rank':'facilities'}
    BASE = {'programme design rank':'programme_design', \
            'programme design':'programme_design'}
    for key,value in BASE.items():
        result.update(permutate(key, value))
    return result

def permutate(data1, data2=None):
    value = data1.replace(' ', '_')
    if data2 is not None:
        value = data2
    lists = []
    helper(data1, lists)
    result = {}
    for ele in lists:
        result[ele] = value
    print("------------")
    print(result)
    print("------------")
    return result

def helper(data1, data2):
    index = data1.find(' ')
    if index < 0:
        data2.append(data1)
        return
    else:
        data1L = list(data1)
        data1L[index] = ''
        helper(''.join(data1L), data2)
        data1L[index] = '_'
        helper(''.join(data1L), data2)
    return

print(supply())