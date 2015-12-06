wizard_list=['spider legs', 'toe of frog', 'eye of newt','bat wing', 'slug butter', 'snake dandruff']
print(wizard_list)
wizard_list.append('bear bump')
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
#what happens when we delete the first element?
del wizard_list[0]
#what if we want to add an item somewhere in the list besides the end?
wizard_list.insert(0,'toe of frog')
wizard_list.insert(5,'nate')