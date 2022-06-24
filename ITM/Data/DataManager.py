import glob

ext = ['png', 'jpg', 'gif']    # Add image formats here
class DataManager:
    global images, target_folder
    def __init__(self, target_folder='./images'):
        print ('[DataManager.__init__] created')
        self.target_folder = target_folder
        self.reset(target_folder)
    
    def reset(self, target_folder='./images'):
        print ('[DataManager.reset] reset, target=', target_folder)
        self.__loadImages()
    
    def __loadImages(self):
        print ('[DataManager.__loadImages] load images, from ', self.target_folder)
        target_folder = []
        [target_folder.extend(glob.glob(self.target_folder + '/' + '*.' + e)) for e in ext]
        print ('[DataManager.__loadImages] num images = ', len(target_folder))
