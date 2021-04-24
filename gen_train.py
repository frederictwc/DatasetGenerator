import glob

path = 'dataset_2/'

def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:
        for jpg_file in glob.glob(image_path + '*.jpg'):
            tf.write(jpg_file + '\n')

generate_train_and_val(path, path + 'train.txt')
#generate_train_and_val(path + 'val_images/', path + 'val.txt')