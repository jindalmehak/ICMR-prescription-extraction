# utils/evaluation.py
from sklearn.metrics import f1_score
import re

def simple_text_clean(text):
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def evaluate_extraction(ground_truth_list, predicted_list):
    y_true = []
    y_pred = []

    for gt, pred in zip(ground_truth_list, predicted_list):
        for key in gt.keys():
            y_true.append(simple_text_clean(str(gt[key])))
            y_pred.append(simple_text_clean(str(pred.get(key, ''))))

    f1 = f1_score(y_true, y_pred, average='micro')
    return f1
