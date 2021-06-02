import glob

path = 'DIRT_4.1/'

def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'a+') as tf:
        for jpg_file in glob.glob('DIRT_4.1/' + '*train*.jpg'):
            print(jpg_file)
            tf.write(jpg_file + '\n')

generate_train_and_val(path, path + 'train.txt')
#generate_train_and_val(path + 'val_images/', path + 'val.txt')
