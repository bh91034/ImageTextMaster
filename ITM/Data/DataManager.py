import glob

from matplotlib.pyplot import cla

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
    def getNextImageFile(cls, curr_file):
        print ('[DataManager] getNextImageFile() called!!...')
        for i in range(len(cls.target_files)):
            print ('[DataManager] getNextImageFile() i=', i, ', curr_file=', curr_file, ', compare=',cls.target_files[i])
            if cls.target_files[i] == curr_file:
                if (i+1) < len(cls.target_files):
                    print ('[DataManager] getNextImageFile() - image found : ', cls.target_files[i+1])
                    return cls.target_files[i+1]
                else:
                    break
        print ('[DataManager] getNextImageFile() - image not found!!')
        return None
    
    @classmethod
    def getPrevImageFile(cls, curr_file):
        print ('[DataManager] getPrevImageFile() called!!...')
        for i in range(len(cls.target_files)):
            print ('[DataManager] getPrevImageFile() i=', i, ', curr_file=', curr_file, ', compare=',cls.target_files[i])
            if cls.target_files[i] == curr_file:
                if i != 0:
                    print ('[DataManager] getPrevImageFile() - image found : ', cls.target_files[i-1])
                    return cls.target_files[i-1]
                else:
                    break
        print ('[DataManager] getPrevImageFile() - image not found!!')
        return None
    
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
