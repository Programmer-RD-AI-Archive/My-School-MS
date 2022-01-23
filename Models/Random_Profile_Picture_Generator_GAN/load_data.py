from Models.Random_Profile_Picture_Generator_GAN import *


def load_data(directory="./data/", IMG_SIZE=56, transforms=transforms):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    idx = -1
    data = []
    for file in tqdm(os.listdir(directory)):
        file = directory + file
        img = cv2.imread(file, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        data.append(np.array(transforms(np.array(img))))
    return data
    