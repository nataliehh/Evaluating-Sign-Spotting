# Distractor-based Evaluation of Sign Spotting
## By Natalie Hollain, Martha Larson and Floris Roelofsen
### 2022-2023

---

## Setup 

- Please use `requirements.txt` to install the dependencies for the code. 
- Unzip CNGT_data.zip to get the CNGT_data folder, which contains (most of) the required files you will need to run the model. Note that some folders and files are not provided because they were privately shared with us. See the next step for more details.
- Acquire data from [Corpus NGT](https://www.corpusngt.nl/) and [NGT Signbank](https://signbank.cls.ru.nl/). Please contact the authors of these data to gain access. The data we use are:
	- Corpus NGT videos and annotation files in the format `Sxxx_CNGTyyyy.mpg`, `Sxxx_CNGTyyyy.eaf`
	- [All gloss information](https://signbank.cls.ru.nl/signs/show_all/) and the [minimal pairs](https://signbank.cls.ru.nl/analysis/minimalpairs/) from NGT Signbank
- The Corpus NGT videos require extracting landmarks. This can be done by running `mediapipe_processing.ipynb` (remove the break in the for-loop to process all videos). We warn that this takes several days to run even when done in parallel. 
Additionally, features still need to be extracted (which is done in the next step). This takes less time, about 30-60 minutes.
	- To skip the extraction of the landmarks and features, download and unzip [features_data.zip](https://drive.google.com/file/d/1YB7UNfd4jKrOU2KJWOPGiczehOAWXNaP/view?usp=share_link) and put the unzipped file in the CNGT_data folder. This file contains the extracted features from the Mediapipe landmarks.
- Run sign_spotting_dataset_creation.ipynb to create the datasets.
- Now, run sign_spotting.ipynb to train the model and get the evaluation.

### Unable to access Corpus NGT and NGT Signbank

- Download [CNGT_dataset.zip](https://drive.google.com/file/d/1oUyE-Jd1jS77F5-7r2cY6aBl3pg2IHXg/view?usp=share_link) and put the resulting files in the CNGT_data folder.
- Run `sign_spotting.ipynb` to train the model. You will be able to run up until (but excluding) the section called *Sliding window example*.