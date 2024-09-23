"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons.



Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 90%
Display report for all universities that have a total price for in-state students living off campus over $60,000



"""

import json

infile = open('school_data.json', 'r')

schools = json.load(infile)

print(type(schools))

conference_schools = [372,108,107,130]

#Display only those schools that are part of the ACC, Big 12, Big Ten, and SEC divisons.
for school in schools:
    if 'NCAA' in school:
        if school['NCAA'].get('NAIA conference number football (IC2020)') in conference_schools:
            print(school['instnm'])

#report 1 - graduation rate for women
for school in schools:
    if 'Graduation rate  women (DRVGR2020)' in school and school['Graduation rate  women (DRVGR2020)'] is not None:
        if school['Graduation rate  women (DRVGR2020)'] > 90:
            print(f"University: {school['instnm']}")
            print(f"Graduation rate for women: {school['Graduation rate  women (DRVGR2020)']}%\n")
    







#report 2 - off campus cost
for school in schools:
    if 'Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)' in school:
        if school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] is not None:
            if school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] > 60000:
                print(f"University: {school['instnm']}")
                print(f"Total price for in-state students living off campus cost: ${school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']}\n")
