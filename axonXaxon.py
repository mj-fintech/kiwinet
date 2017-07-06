from flask import Flask
from flask import jsonify
from flask import request
from ann_input_screen import ann_input, ann_class_name
from keras.models import load_model
import glob
import pickle
from TRAIN import TRAIN
import pandas as pd
import os
from flask import redirect, url_for
from werkzeug.utils import secure_filename
from entity_parser import entity_parser

UPLOAD_FOLDER = '/home/minjun/projects/pypestream'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Currently we only support svc_clf.pickle
def load_classifier(name):

    # names of classifiers pickle or h5 files in the directory #
    # Consider not deploying 'rf_clf' if execution takes too much time #
    if name in ['svc_clf','sgd_clf','rf_clf','lr_clf','gs_nb_clf','dt_clf']:
        try:

            with open('{}.pickle'.format(name), 'rb') as f:
                classifier = pickle.loads(f.read())
            return classifier
        except Exception as e:
            print (str(e))

    elif name == 'ann_clf':
        try:

            classifier = load_model('ann_clf.h5')
            return classifier
        except Exception as e:
            print (str(e))

    else:
        pass

def classify(classifier_name, user_input):

    if classifier_name in ['svc_clf','sgd_clf','rf_clf','lr_clf','dt_clf']:
        try:

            classifier = load_classifier(classifier_name)
            return classifier.predict([user_input])[0], classifier_name
        except Exception as e:
            print (str(e))

    elif classifier_name == 'ann_clf':
        try:

            classifier = load_classifier(classifier_name)
            return ann_class_name(classifier.predict_classes(ann_input(user_input))[0]), classifier_name
        except Exception as e:
            print (str(e))


    elif classifier_name == 'gs_nb_clf':
        try:

            classifier = load_classifier(classifier_name)
            return classifier.predict(ann_input(user_input))[0], classifier_name
        except Exception as e:
            print (str(e))

    else:
        pass

@app.route("/", methods=["GET"])
def get():
    json = request.get_json()
    response = [glob.glob('*.pickle')[i].split('.')[0] for i in range(len(glob.glob('*.pickle')))] + [glob.glob('*.h5')[s].split('.')[0] for s in range(len(glob.glob('*.h5')))]
    return jsonify(available_classifiers=response)


@app.route("/", methods=["POST"])
def post():
    clf_list = ['svc_clf','sgd_clf','gs_nb_clf','ann_clf','lr_clf','dt_clf']
    json = request.get_json()
    if json.get('classifier'):
        response = classify(json['classifier'], json['input'])
        response_2 = entity_parser(json['input'])
        return jsonify(data=[response], entity=[response_2])
    else:
        response = []
        for clf in clf_list:
            response.append(classify('{}'.format(clf), json['input']))
        return jsonify(all_matches=response,entity=entity_parser(json['input']))


# Upload csv file --> train classifier --> return Accuracy and actual/predicted DataFrame
@app.route("/upload", methods=["POST"])
def openfile():
    openfile = request.files['file']
    #import pdb; pdb.set_trace()
    classifier = request.args.get('classifier')
    filename = secure_filename(openfile.filename)
    openfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    dataframe, accuracy = TRAIN(os.path.join(app.config['UPLOAD_FOLDER'], filename),classifier)

    print(dataframe.to_dict())
    data_dict = {str(key): str(value)
                 for key, value in dataframe.to_dict().items()}
    return jsonify(accuracy=str(accuracy), data=data_dict)
    #df = pd.DataFrame(openfile)
    #return df
    #filename = secure_filename(file.filename)
    #file.save(os.path.join('home/', filename))
