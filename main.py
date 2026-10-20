from pyscript import document, display

set_1 = {'Fries', 'Burger'}
set_2 = {'Fries', 'Burger', 'Coke', 'Apple Pie'}

display((set_2 > set_1), target = "div1")

subjects = ['Math', 'Science', 'Filipino', 'ICT']
subjects_converted = frozenset(subjects)

display(subjects_converted, target = "div2")
display(subjects, target = "div2")
