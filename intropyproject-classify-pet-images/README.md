\# Image Classification for a City Dog Show



This project uses pretrained Convolutional Neural Networks (CNNs) to classify pet images and identify whether the images contain dogs or other animals. For dog images, the project also evaluates the predicted dog breed.



\## Project Objective



The main objectives of this project are:



\- Identify whether a pet image contains a dog or a non-dog.

\- Classify the breed of dogs in the images.

\- Compare the performance of different pretrained CNN architectures.

\- Analyze classification accuracy and runtime.



\## CNN Architectures Tested



The following pretrained CNN models were tested:



\- VGG

\- AlexNet

\- ResNet



\## Dataset



The project uses a set of 40 pet images:



\- 30 dog images

\- 10 non-dog images



\## Results



| Metric | VGG | AlexNet | ResNet |

|---|---:|---:|---:|

| Total Images | 40 | 40 | 40 |

| Dog Images | 30 | 30 | 30 |

| Not-Dog Images | 10 | 10 | 10 |

| Correct Dog Classification | 100.0% | 100.0% | 100.0% |

| Correct Not-Dog Classification | 100.0% | 100.0% | 90.0% |

| Correct Breed Classification | 93.3% | 80.0% | 90.0% |

| Runtime | \~3 sec | <1 sec | \~1 sec |



\## ResNet Results



The ResNet model produced the following results:



\- Overall classification: 97.5%

\- Correct dog classification: 100.0%

\- Correct non-dog classification: 90.0%

\- Correct breed classification: 90.0%

\- Runtime: approximately 1 second



\### Incorrect Dog Breed Classifications



| Actual Breed | Predicted Breed |

|---|---|

| Beagle | Walker Hound / Walker Foxhound |

| Golden Retriever | Leonberg |

| Great Pyrenees | Kuvasz |



The ResNet model also incorrectly classified one non-dog image:



\- Actual: Cat

\- Predicted: Norwegian Elkhound / Elkhound



\## Project Structure



```text

Image-Classification-City-Dog-Show/

│

├── pet\_images/

├── check\_images.py

├── classifier.py

├── classify\_images.py

├── get\_input\_args.py

├── get\_pet\_labels.py

├── adjust\_results4\_isadog.py

├── calculates\_results\_stats.py

├── print\_results.py

├── dognames.txt

├── print\_functions\_for\_lab\_checks.py

├── README.md

└── ...

