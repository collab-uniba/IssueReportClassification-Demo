# IssueReportClassification-Demo
This repository contains an interface for Issue Report Classification Models.
The interface allows users to input title and body of an issue report and receive a prediction of the category or type of issue report.
You can also input a GitHub link to classify your issues.

## Requirements
- Python3.8+
- ``` pip install -r requirements.txt ```

## Structure
The project contains the following files and folders:

  `src`: contains the source code for the interface and the machine learning models
    `models.py`: contains the model wrappers used by the interface. 
    `main.py`: runs the interface.
    `preprocessing.py`: contains the code for preprocessing text data, using ekphrasis and regex.
    `utils.py`: contains utility functions used to retrieve the title and body of an issue from GitHub.
    `interface.py`: contains the code for the Gradio interface.
    
## Cite
```
@inproceedings{Colavito-2022,
	title        = {Issue Report Classification Using Pre-trained Language Models},
	author       = {Colavito, Giuseppe and Lanubile, Filippo and Novielli, Nicole},
	year         = 2022,
	month        = may,
	booktitle    = {2022 IEEE/ACM 1st International Workshop on Natural Language-Based Software Engineering (NLBSE)},
	pages        = {29--32},
	doi          = {10.1145/3528588.3528659},
	abstract     = {This paper describes our participation in the tool competition organized in the scope of the 1st International Workshop on Natural Language-based Software Engineering. We propose a supervised approach relying on fine-tuned BERT-based language models for the automatic classification of GitHub issues. We experimented with different pre-trained models, achieving the best performance with fine-tuned RoBERTa (F1 = .8591).},
	keywords     = {Issue classification, BERT, deep learning, labeling unstructured data, software maintenance and evolution}
}
```

```
@dataset{colavito_dataset_2023,
	title        = {Few-Shot Learning for Issue Report Classification},
	author       = {Colavito, Giuseppe and Lanubile, Filippo and Novielli, Nicole},
	year         = 2023,
	publisher    = {Zenodo},
	doi          = {10.5281/zenodo.7628150},
	url          = {https://doi.org/10.5281/zenodo.7628150}
}
```
```
@software{Giuseppe_Issue-Report-Classification-Using-RoBERTa_2022,
	title        = {{Issue-Report-Classification-Using-RoBERTa}},
	author       = {Giuseppe, Colavito and Filippo, Lanubile and Nicole, Novielli},
	year         = 2022,
	month        = 3,
	url          = {https://github.com/collab-uniba/Issue-Report-Classification-Using-RoBERTa},
	version      = {1.0.0}
}
```
```
@software{colavito_code_2023,
	title        = {{Few-Shot Learning for Issue Report Classification}},
	author       = {Colavito, Giuseppe and Lanubile, Filippo and Novielli, Nicole},
	year         = 2023,
	url          = {https://github.com/collab-uniba/Issue-Report-Classification-NLBSE2023},
	version      = {1.0.0}
}
```

