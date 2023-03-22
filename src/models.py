from sentence_transformers.losses import CosineSimilarityLoss
from setfit import SetFitModel
from setfit import SetFitTrainer
import numpy as np

from typing import Dict, List, Tuple

class BaseModel:
    def predict(self, text: str) -> str:
        pass

class BertClassificationModel(BaseModel):
    def __init__(self, model_name: str, model_path: str, tokenizer_path: str, label_mapping: Dict[int, str]):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        self.label_mapping = label_mapping.copy()

    def predict(self, text: str) -> str:
        inputs = self.tokenizer(text, padding=True, truncation=True, return_tensors='pt')
        outputs = self.model(**inputs)
        predicted_class = torch.argmax(outputs.logits).item()
        return self.label_mapping[predicted_class]

class SetFitClassificationModel(BaseModel):
    def __init__(self, model_name: str, model_path: str, label_mapping: Dict[int, str]):
        self.model = SetFitModel.from_pretrained(model_path)
        self.label_mapping = label_mapping.copy()

    def predict(self, text: str) -> str:
        predicted_class = self.model.predict([text])[0]
        return self.label_mapping[(predicted_class)]

MODELS = {
    "ISSUE_REPORT_CLASSIFIER": BertClassificationModel(
        model_name="ISSUE_REPORT_CLASSIFIER",
        model_path="Peppocola/IssueReportClassifier-NLBSE22",
        tokenizer_path="Peppocola/IssueReportClassifier-NLBSE22",
        label_mapping={0: "bug", 1: "enhancement", 2: "question"}
    ),
    "FEW_SHOT_ISSUE_CLASSIFIER": SetFitClassificationModel(
        model_name="FEW_SHOT_ISSUE_CLASSIFIER",
        model_path="PeppoCola/FewShotIssueClassifier-NLBSE23",
        label_mapping={0: "bug", 1: "documentation", 2: "feature", 3: "question"}
    )
}
