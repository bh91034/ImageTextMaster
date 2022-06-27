import glob, os
import easyocr

ext = ['png', 'jpg', 'gif']    # Add image formats here
class DataManager:
    # need to reset, reload
    target_folder = None
    target_files = []
    target_texts = []

    # no need to reset, reload
    easyocr_reader = None

    def __init__(self, target_folder='./images'):
        print ('[DataManager.__init__] created')
        DataManager.easyocr_reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
        self.resetWorkFolder(target_folder)
    
    @classmethod
    def getBorderInfoOfText(cls, img_file, list_idx):
        print ('[DataManager] getBorderInfoOfText() called!!...')
        file_idx = cls.getImageIndex(img_file)
        return cls.target_texts[file_idx][list_idx][0][0], cls.target_texts[file_idx][list_idx][0][2]

    @classmethod
    def getExistingTextsInImage(cls, img_file):
        print ('[DataManager] getExistingTextsInImage() called!!...')
        i = cls.getImageIndex(img_file)
        if cls.target_texts[i] != None:
            texts = [t[1] for t in cls.target_texts[i]]
            return texts
        return None
    
    @classmethod
    def readTextsInImageAgain(cls, img_file):
        print ('[DataManager] readTextsInImageAgain() called!!...')
        texts_info = cls.easyocr_reader.readtext(img_file)
        if texts_info == None:
            return None
        cls.__setTargetTexts(img_file, texts_info)
        texts = [t[1] for t in texts_info]
        return texts

    @classmethod
    def __setTargetTexts(cls, img_file, texts_info):
        print ('[DataManager] setTargetTexts() called!!...')
        i = cls.getImageIndex(img_file)
        if i < 0:
            return False
        else:
            print('[DataManager] setTargetTexts() : saved texts info, i=', i, ', texts_info=', texts_info)
            cls.target_texts[i] = texts_info

    @classmethod
    def getImageIndex(cls, img_file):
        print ('[DataManager] getImageIndex() called!!...')
        for i in range(len(cls.target_files)):
            if cls.target_files[i] == img_file:
                return i
        return -1

    @classmethod
    def getNextImageFile(cls, img_file):
        print ('[DataManager] getNextImageFile() called!!...')
        for i in range(len(cls.target_files)):
            print ('[DataManager] getNextImageFile() i=', i, ', curr_file=', img_file, ', compare=',cls.target_files[i])
            if cls.target_files[i] == img_file:
                if (i+1) < len(cls.target_files):
                    print ('[DataManager] getNextImageFile() - image found : ', cls.target_files[i+1])
                    return cls.target_files[i+1]
                else:
                    break
        print ('[DataManager] getNextImageFile() - image not found!!')
        return None
    
    @classmethod
    def getPrevImageFile(cls, img_file):
        print ('[DataManager] getPrevImageFile() called!!...')
        for i in range(len(cls.target_files)):
            print ('[DataManager] getPrevImageFile() i=', i, ', curr_file=', img_file, ', compare=',cls.target_files[i])
            if cls.target_files[i] == img_file:
                if i != 0:
                    print ('[DataManager] getPrevImageFile() - image found : ', cls.target_files[i-1])
                    return cls.target_files[i-1]
                else:
                    break
        print ('[DataManager] getPrevImageFile() - image not found!!')
        return None
    
    @classmethod
    def resetWorkFolder(cls, target_folder='./images'):
        print ('[DataManager.reset] reset, target=', target_folder)
        cls.target_folder = os.path.abspath(target_folder)
        cls.__loadImages(cls.target_folder)
        
        # init __OUTPUT_FILES__ folder
        cls.__initOutputFiles()

    @classmethod
    def __loadImages(cls, target_folder):
        print ('[DataManager.__loadImages] load images, from ', target_folder)
        cls.target_files = []
        [cls.target_files.extend(glob.glob(target_folder + '/' + '*.' + e)) for e in ext]
        print ('[DataManager.__loadImages] num images : ', len(cls.target_files))
        cls.target_texts = [None] * len(cls.target_files)

    # -----------------> from here <-------------------------------------------
    #ifdef __OUTPUT_FILES__
    @classmethod
    def saveOutputFile(cls, src_file, out_image):
        print ('[DataManager] saveOutputFile() called...')
        
        if out_image is None:
            print ('[DataManager] saveOutputFile() : image is None, it can not be saved!')
        
        out_file = cls.getOutputFile(src_file)
        print ('[DataManager] saveOutputFile() : src_file=', src_file)
        print ('[DataManager] saveOutputFile() : out_file=', out_file)
        
        if out_file is not None:
            out_image.save(out_file)
            return True
        return False

    @classmethod
    def getOutputFile(cls, src_file):
        from pathlib import Path
        import shutil
        print ('[DataManager] getOutputFile() called...')
        src_file_name = Path(src_file).name
        out_file = os.path.abspath(cls.target_folder + '/' + '__OUTPUT_FILES__' + '/' + src_file_name)
        print ('[DataManager] getOutputFile() : src_file=', src_file)
        print ('[DataManager] getOutputFile() : out_file=', out_file)
        return out_file

    @classmethod
    def __initOutputFiles(cls):
        print ('[DataManager] initOutputFiles() called...')
        output_folder = os.path.abspath(cls.target_folder + '/' + '__OUTPUT_FILES__')
        print ('[DataManager] initOutputFiles() : output_folder = ', output_folder)

        # create output folder if not exist
        if os.path.isdir(output_folder) == False:
            os.makedirs(output_folder)
            print ('[DataManager] initOutputFiles() : outpput_folder newly created!')
        
        if cls.target_files == None or len(cls.target_files) == 0:
            print ('[DataManager] initOutputFiles() : no source files!')
            return
        
        # copy files to output folder if source image file doesn't exist in output folder
        from pathlib import Path
        import shutil
        for src_file in cls.target_files:
            src_file_name = Path(src_file).name
            out_file = os.path.abspath(cls.target_folder + '/' + '__OUTPUT_FILES__' + '/' + src_file_name)
            if not os.path.isfile(out_file):
                shutil.copy(src_file, out_file)
    #endif // __OUTPUT_FILES__
    # -----------------> to   here <-------------------------------------------
