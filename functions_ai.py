mean, std = 0.11728907, 0.3424749
def custom_preprocessing(img): #implemntation in ImageDataGenerator 
    return (img - mean) / std
