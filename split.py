import splitfolders

# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio("input_folder", output="output", seed=1337, 
ratio=(.8, .2), group_prefix=None) # default values