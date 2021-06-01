from videos import Video
import os, fnmatch, errno
from skimage import io
import sys

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_PATH)

SOURCE_PATH = 'Videos'
SOURCE_EXTS = '*.mpg'      # Change for different video formats
FACE_PREDICTOR_PATH = 'shape_predictor_68_face_landmarks.dat'
TARGET_PATH = 'TARGET/'

# Recursvive directory creation function - makes all intermediate-level directories needed to contain the leaf directory
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory): # os.walk generates the file names in a directory tree
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):  # Test whether basename matches the pattern string
                filename = os.path.join(root, basename)
                yield filename

if __name__ == '__main__':
    for filepath in find_files(SOURCE_PATH, SOURCE_EXTS):
        print(("Processing: {}".format(filepath)))
        # vtype = face indicates input is a video
        video = Video(vtype='face', face_predictor_path=FACE_PREDICTOR_PATH).from_video(filepath)

        mkdir_p(TARGET_PATH)
        filepath_wo_ext = os.path.splitext(filepath)[0]           # Remove extension from video file name
        target_dir = os.path.join(TARGET_PATH, filepath_wo_ext)    # Name directory to save each processed video
        mkdir_p(target_dir)

        index = 0
        for frame in video.mouth:
            io.imsave(os.path.join(target_dir, "mouth_{0:03d}.png".format(index)), frame)
            index += 1
