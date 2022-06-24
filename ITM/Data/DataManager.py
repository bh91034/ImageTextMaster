import glob

ext = ['png', 'jpg', 'gif']    # Add image formats here
class DataManager:
    images = None
    target_folder = None
    target_files = []
    def __init__(self, target_folder='./images'):
        print ('[DataManager.__init__] created')
        self.target_folder = target_folder
        self.reset(target_folder)
        DataManager.target_folder = target_folder
    
    @classmethod
    def reset(cls, target_folder='./images'):
        print ('[DataManager.reset] reset, target=', target_folder)
        cls.target_folder = target_folder
        cls.__loadImages(target_folder)
    
    @classmethod
    def __loadImages(cls, target_folder):
        print ('[DataManager.__loadImages] load images, from ', target_folder)
        cls.target_files = []
        [cls.target_files.extend(glob.glob(target_folder + '/' + '*.' + e)) for e in ext]
        print ('[DataManager.__loadImages] num images : ', len(cls.target_files))
