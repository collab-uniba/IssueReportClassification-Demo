from models import MODELS
from interface import IssueClassifier

IssueClassifier(MODELS, share=True).run()