import sys, os
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
LIPNET_PATH = os.path.join(CURRENT_PATH,'..','Training')
sys.path.insert(0, LIPNET_PATH)

os.environ['KMP_DUPLICATE_LIB_OK']='True'

from lipnet.videos import Video
from lipnet.visualization import show_video_subtitle
from lipnet.decoders import Decoder
from lipnet.helpers import labels_to_text
from lipnet.spell import Spell
from lipnet.model import LipNet
from keras.optimizers import Adam
from keras import backend as K
import numpy as np

np.random.seed(55)

VIDEO_PATH = os.path.join(CURRENT_PATH,'PredictVideo','sbwe5n.mpg')
WEIGHTS_PATH = os.path.join(CURRENT_PATH,'lipnet_weight.h5')

FACE_PREDICTOR_PATH = os.path.join(CURRENT_PATH,'..','MouthExtract','shape_predictor_68_face_landmarks.dat')

PREDICT_GREEDY      = False
PREDICT_BEAM_WIDTH  = 200
PREDICT_DICTIONARY  = os.path.join(CURRENT_PATH,'..','Training','dictionaries','grid.txt')

def predict(weight_path, video_path, absolute_max_string_len=32, output_size=28):
    print ("\nLoading data from disk...")
    video = Video(vtype='face', face_predictor_path=FACE_PREDICTOR_PATH)
    if os.path.isfile(video_path):
        video.from_video(video_path)
    else:
        video.from_frames(video_path)
    print ("Data loaded.\n")

    if K.image_data_format() == 'channels_first':
        img_c, frames_n, img_w, img_h = video.data.shape
    else:
        frames_n, img_w, img_h, img_c = video.data.shape


    lipnet = LipNet(img_c=img_c, img_w=img_w, img_h=img_h, frames_n=frames_n,
                    absolute_max_string_len=absolute_max_string_len, output_size=output_size)

    adam = Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

    lipnet.model.compile(loss={'ctc': lambda y_true, y_pred: y_pred}, optimizer=adam)
    lipnet.model.load_weights(weight_path)

    print("Loaded Weights")

    spell = Spell(path=PREDICT_DICTIONARY)
    decoder = Decoder(greedy=PREDICT_GREEDY, beam_width=PREDICT_BEAM_WIDTH,
                      postprocessors=[labels_to_text, spell.sentence])

    X_data       = np.array([video.data]).astype(np.float32) / 255   # Normalize
    input_length = np.array([len(video.data)])

    y_pred         = lipnet.predict(X_data)
    result         = decoder.decode(y_pred, input_length)[0]

    return (video, result)

if __name__ == '__main__':
    print("*****Lip to Speech Project****")
    video, result = predict(WEIGHTS_PATH, VIDEO_PATH)
    print("[ THE PERSON SAID ] > | {} |".format(result))
