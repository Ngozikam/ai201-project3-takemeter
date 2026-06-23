# AI201 Project 3 - TakeMeter

## Milestone 1: Choose Your Community and Define Your Labels

### Community

Community Name:
r/FPGA

Reason for Choosing

- Active FPGA engineering community
- Rich technical discussions
- Career advice
- RTL debugging
- FPGA hardware selection
- Learning resources

---

## Recurring Discussion Themesgit diff planning.md

After reviewing discussions from the r/FPGA community, the following recurring themes were identified:

1. FPGA Career and Industry
2. FPGA Hardware and Board Selection
3. RTL Design and Debugging
4. FPGA Learning and Personal Projects

These recurring themes were used to develop the label taxonomy below. The taxonomy is designed to be mutually exclusive, representative of the FPGA community, and suitable for supervised text classification.

---


## Label Taxonomy

### Label 1 — Career & Industry

Definition

Discussion related to FPGA careers, interviews, hiring, salaries, industry outlook, and job preparation.

Examples

- What is your outlook on the FPGA industry over the next 20 years?
- New grad freaking out about FPGA interviews.

Borderline Example

Should I learn ASIC or FPGA?

Decision Rule

If the discussion mainly concerns career planning or employment, classify it as Career & Industry.

---

### Label 2 — Hardware & Boards

Definition

Discussion focused on FPGA boards, vendors, hardware selection, purchasing decisions, or comparing devices.

Examples

- Need help buying an FPGA.
- Best FPGA board for beginners.

Borderline Example

Should I buy a Zynq board for AI projects?

Decision Rule

If the primary purpose is choosing hardware, classify it as Hardware & Boards.

---

### Label 3 — Design & Debugging

Definition

Discussion related to RTL development, Verilog/VHDL, synthesis, timing, implementation, simulation, and debugging.

Examples

- RTL works in simulation but fails on hardware.
- Timing closure issue in Vivado.

Borderline Example

Verilog syntax question.

Decision Rule

If the discussion centers on solving implementation or coding issues, classify it as Design & Debugging.

---

### Label 4 — Learning & Projects

Definition

Discussion about learning FPGA, educational resources, tutorials, beginner questions, or personal FPGA projects.

Examples

- Best FPGA books.
- First FPGA project recommendations.

Borderline Example

Should I learn Verilog before SystemVerilog?

Decision Rule

If the discussion primarily concerns education or learning, classify it as Learning & Projects.

---

## Hardest Edge Case

Example

I'm a beginner. Which FPGA board should I buy to prepare for FPGA interviews?

Possible Labels

- Hardware & Boards
- Career & Industry

Decision Rule

If the post mainly seeks advice on selecting hardware, classify it as Hardware & Boards.
If the post mainly seeks career preparation advice, classify it as Career & Industry.

---

## Community Description

The Reddit r/FPGA community consists of FPGA engineers, researchers, students, and industry professionals discussing programmable hardware design, RTL development, FPGA hardware, career opportunities, debugging, and learning resources. These four labels capture the major types of discussions that members regularly participate in. Distinguishing between career advice, hardware selection, technical debugging, and learning resources enables the classifier to recognize the intent of each discussion and reflects how members naturally organize conversations within the FPGA community.

## Data Collection Plan

### Data Source

The dataset will be collected from the Reddit r/FPGA community, which contains discussions on FPGA design, debugging, hardware selection, learning, and career development.

### Target Dataset Size

The project aims to annotate approximately 200 Reddit posts.

### Target Label Distribution

- Career & Industry: 50 posts
- Hardware & Boards: 50 posts
- Design & Debugging: 50 posts
- Learning & Projects: 50 posts

### Handling Class Imbalance

If one label contains fewer than 50 examples after collecting 200 posts, additional posts will be collected using subreddit keyword searches (e.g., "career", "board", "Vivado", "Verilog", "beginner") until a balanced dataset is achieved. If balancing is not possible, class weighting or stratified evaluation will be considered during model training.

## Evaluation Metrics

The classifier will be evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Accuracy measures overall correctness but can be misleading when class distributions are uneven. Precision measures how often predicted labels are correct, while Recall measures how well the classifier identifies all examples of each class. The F1-score balances Precision and Recall, making it appropriate for evaluating multiclass classification performance. The Confusion Matrix will help identify which discussion categories are most frequently confused.

## Definition of Success

The classifier will be considered successful if it achieves:

- Overall Accuracy of at least 85%
- Macro F1-score of at least 0.80
- No label has an F1-score below 0.75
- Most misclassifications occur only between naturally related categories (for example, Career & Industry versus Hardware & Boards)

Such performance would make the classifier useful for automatically organizing FPGA discussions within the Reddit community.

## AI Tool Plan

### Label Stress-Testing

ChatGPT will be used to generate ambiguous FPGA discussion posts that fall between two labels. These examples will be used to refine the label definitions before annotation begins.

### Annotation Assistance

ChatGPT may be used to suggest initial labels for collected Reddit posts. Every suggested label will be manually reviewed and corrected before inclusion in the final dataset. AI-assisted annotations will be documented in the project report.

### Failure Analysis

After model evaluation, ChatGPT will be used to analyze incorrectly classified examples and identify common error patterns. All suggested explanations will be verified manually against the original dataset and confusion matrix.

## Review of Success Criteria

The selected evaluation metrics and performance thresholds provide objective measures for determining whether the classifier is suitable for practical use. These criteria allow the final model to be evaluated consistently and compared with future improvements.

# Milestone 3 – Dataset Collection and Annotation

## Dataset Source

The dataset was collected from **public posts** in the Reddit **r/FPGA** community. Only publicly accessible posts were used, satisfying the project requirements. No private forums, authenticated content, or personal data were collected.

---

## Dataset Summary

* **Community:** Reddit (r/FPGA)
* **Dataset size:** 222 labeled posts
* **Annotation method:** Manual annotation
* **File format:** CSV
* **Dataset file:** `FPGA_Reddit_Dataset_1_222.csv`

The dataset contains the following columns:

| Column | Description                              |
| ------ | ---------------------------------------- |
| text   | Reddit post title or content             |
| label  | One of the four classification labels    |
| notes  | Short explanation or annotation comments |
| No     | Dataset index (optional)                 |

The dataset is stored as a **single CSV file**, as required by the project. The dataset has **not** been pre-split into training, validation, or testing sets because the project notebook automatically performs the **70% / 15% / 15%** split.

---

# Label Definitions

The Reddit posts were categorized into four mutually exclusive classes.

## 1. Career & Industry

Posts related to:

* Career advice
* FPGA job opportunities
* Hiring
* Salaries
* Interviews
* Certifications
* Industry outlook
* Internships
* Professional development
* Career transitions

Examples:

* Looking to hire FPGA Engineers
* FPGA Careers — What's It Like Day-to-Day?
* How common are layoffs of FPGA Engineers?

---

## 2. Learning & Projects

Posts focused on:

* Learning FPGA development
* Tutorials
* Educational resources
* Student questions
* Personal FPGA projects
* Final-year projects
* Research projects
* FPGA applications
* Project recommendations

Examples:

* FPGA Starter Projects
* Final year FPGA project
* Ideas for interesting FPGA projects

---

## 3. Hardware & Boards

Posts primarily discussing:

* FPGA development boards
* RFSoC platforms
* PYNQ boards
* Versal boards
* Basys
* Nexys
* Zynq
* Tang Nano
* Altera
* Intel
* AMD/Xilinx hardware
* Purchasing recommendations
* Hardware selection

Examples:

* Which FPGA board should I buy?
* Cheap FPGA dev board
* Looking for an FPGA board under $600

---

## 4. Design & Debugging

Posts involving FPGA implementation, including:

* RTL design
* Verilog
* VHDL
* Vivado
* Quartus
* Vitis
* Timing analysis
* CDC
* Simulation
* Verification
* Synthesis
* Hardware debugging
* AXI
* PCIe
* MIPI
* Ethernet
* Clocking
* FPGA implementation issues

Examples:

* What is wrong with this Verilog?
* Design works in Vivado but not after packaging as IP
* Our generated RTL simulated perfectly but failed on hardware

---

# Dataset Statistics

A total of **222** Reddit posts were manually labeled.

## Final Label Distribution

| Label               | Percentage |
| ------------------- | ---------: |
| Learning & Projects |     27.03% |
| Career & Industry   |     25.23% |
| Design & Debugging  |     25.23% |
| Hardware & Boards   |     22.52% |

No label exceeds **70%** of the dataset.

Therefore, the dataset satisfies the class balance requirement specified in the project instructions.

---

# Annotation Process

Each Reddit post was read individually before assigning a label.

Whenever a post appeared to belong to multiple categories, the label was assigned according to the **primary intent** of the post rather than secondary topics.

Posts were **not** labeled in bulk or by keyword matching. Every example received an individual review before the final annotation was assigned.

---

# Hard Edge Cases

## Edge Case 1

### Post

> What kind of hardware DV project actually gets a recruiter's attention?

Possible labels:

* Career & Industry
* Learning & Projects

Final label:

**Career & Industry**

Reason:

Although the post discusses FPGA projects, the primary objective is obtaining employment and improving a résumé rather than learning FPGA design itself.

---

## Edge Case 2

### Post

> Looking for an FPGA development board suitable for machine learning.

Possible labels:

* Hardware & Boards
* Learning & Projects

Final label:

**Hardware & Boards**

Reason:

The central question concerns selecting an FPGA board. Machine learning is only the intended application.

---

## Edge Case 3

### Post

> Our generated RTL simulated perfectly but failed on hardware.

Possible labels:

* Design & Debugging
* Learning & Projects

Final label:

**Design & Debugging**

Reason:

The post focuses on diagnosing and correcting implementation problems between simulation and real hardware rather than learning FPGA concepts.

---

# Dataset Validation

The dataset was verified using Python and pandas.

Validation confirmed:

* 222 labeled examples
* Four unique labels
* No missing labels
* No missing text entries
* Balanced label distribution
* Single CSV file suitable for training

---

# AI Usage Disclosure

ChatGPT was used to assist with:

* organizing the Reddit dataset,
* identifying duplicate posts,
* reviewing annotation consistency,
* checking class balance,
* generating CSV and Excel versions of the dataset,
* verifying dataset integrity before training.

Every Reddit post was manually reviewed before assigning its final label. AI-generated suggestions were reviewed and corrected where necessary. Final labeling decisions were made by the project author.

---

# Milestone 4: Zero-Shot Baseline Evaluation

## Baseline Model

**Model:** Groq Llama-3.3-70B-Versatile (Zero-Shot)

**Evaluation Dataset:** Held-out Test Set

**Test Set Size:** 34 Reddit posts

**Classification Labels:**

* Career & Industry
* Learning & Projects
* Hardware & Boards
* Design & Debugging

---

## Baseline Evaluation Results

The zero-shot baseline was evaluated on the held-out test set before any fine-tuning.

### Overall Accuracy

**Baseline Accuracy:** **73.5% (0.735)**

### Parseable Responses

The baseline successfully classified every example in the test set.

* Total test examples: **34**
* Successfully parsed responses: **34**
* Unparseable responses: **0**
* Parse rate: **100%**

Since all responses were successfully parsed, no further prompt revision was required.

---

## Per-Class Performance

| Label               | Precision | Recall | F1-Score | Support |
| ------------------- | --------: | -----: | -------: | ------: |
| Career & Industry   |      1.00 |   0.56 |     0.71 |       9 |
| Learning & Projects |      0.54 |   0.78 |     0.64 |       9 |
| Hardware & Boards   |      0.71 |   0.71 |     0.71 |       7 |
| Design & Debugging  |      0.89 |   0.89 |     0.89 |       9 |

**Overall Accuracy:** **0.74**

**Macro Average**

* Precision: **0.79**
* Recall: **0.73**
* F1-score: **0.74**

**Weighted Average**

* Precision: **0.79**
* Recall: **0.74**
* F1-score: **0.74**

---

## Baseline Reflection

The zero-shot baseline achieved an overall accuracy of **73.5%**, indicating that the large language model was able to correctly classify most FPGA Reddit posts without task-specific training.

Among the four categories, **Design & Debugging** achieved the strongest performance with a precision of **0.89**, recall of **0.89**, and F1-score of **0.89**. This suggests that posts discussing debugging, RTL implementation, synthesis, timing analysis, and FPGA design tools contain distinctive terminology that is easier for the model to recognize.

The **Hardware & Boards** category achieved balanced performance with precision, recall, and F1-score all equal to **0.71**, indicating reasonably consistent classification performance.

The **Career & Industry** category achieved the highest precision (**1.00**), meaning every prediction assigned to this category was correct. However, its recall was only **0.56**, indicating that several Career & Industry posts were classified into other categories.

The **Learning & Projects** category achieved the highest recall (**0.78**), meaning that most true Learning & Projects posts were successfully identified. However, its precision was only **0.54**, indicating that several posts from other categories were incorrectly classified as Learning & Projects.

Overall, the results suggest that the model had greater difficulty distinguishing **Learning & Projects** from other categories than it did identifying **Design & Debugging** posts.

---

## Hypothesis Before Fine-Tuning

Based on the baseline results, I expect the fine-tuned DistilBERT model to improve the overall classification accuracy by learning FPGA-specific terminology and the differences between the four annotation categories.

The largest improvement is expected in the **Learning & Projects** category because it produced the lowest precision in the zero-shot baseline. Fine-tuning should enable the model to better distinguish learning-related discussions from posts about hardware recommendations and career guidance.

---


# Milestone 5: Fine-Tuning DistilBERT

## Objective

The objective of Milestone 5 was to fine-tune **DistilBERT (`distilbert-base-uncased`)** on the manually annotated FPGA Reddit dataset using Google Colab's free T4 GPU, evaluate the fine-tuned classifier on the locked test set, compare its performance with the Milestone 4 zero-shot Groq baseline, investigate the results through error analysis and diagnostics, and export the required evaluation artifacts.

Sections 1, 2, and 5 of the official notebook had already been completed during Milestone 4. Those baseline results were reused during this milestone for comparison.

---

# Fine-Tuning Configuration

The official AI201 notebook was used without modifying any hyperparameters.

**Model:** `distilbert-base-uncased`

### Training Configuration

| Hyperparameter        |               Value |
| --------------------- | ------------------: |
| Epochs                |                   3 |
| Learning Rate         |                2e-5 |
| Training Batch Size   |                  16 |
| Evaluation Batch Size |                  32 |
| Weight Decay          |                0.01 |
| Warmup Steps          |                  50 |
| Evaluation Strategy   |          Each Epoch |
| Save Strategy         |          Each Epoch |
| Best Model Metric     | Validation Accuracy |

No hyperparameters were modified during the official experiment. Any future hyperparameter tuning will be documented separately as additional work and not as part of the official milestone.

---

# Section 3: Fine-Tuning Results

Fine-tuning completed successfully on the Google Colab T4 GPU without runtime errors.

| Epoch | Training Loss | Validation Loss | Validation Accuracy |
| ----: | ------------: | --------------: | ------------------: |
|     1 |      1.391242 |        1.389532 |            0.242424 |
|     2 |      1.382427 |        1.378397 |            0.363636 |
|     3 |      1.358722 |        1.355558 |            0.333333 |

### Training Discussion

The training loss decreased steadily throughout the three epochs, indicating that optimization proceeded normally. Validation accuracy improved from **24.24%** during the first epoch to **36.36%** during the second epoch before slightly decreasing to **33.33%** in the final epoch. Although optimization converged successfully, the validation accuracy suggests that the classifier learned only weak decision boundaries for the four FPGA discussion categories.

---

# Section 4: Fine-Tuned Model Evaluation

The fine-tuned model was evaluated on the locked test set consisting of **34** examples.

## Overall Accuracy

**Fine-tuned Accuracy:** **29.4%**

---

## Per-Class Performance

| Label                | Precision | Recall | F1-score | Support |
| -------------------- | --------: | -----: | -------: | ------: |
| Career & Industry    |      0.29 |   0.22 |     0.25 |       9 |
| Learning & Projects  |      0.36 |   0.44 |     0.40 |       9 |
| Hardware & Boards    |      0.25 |   0.57 |     0.35 |       7 |
| Design & Debugging   |      0.00 |   0.00 |     0.00 |       9 |
| **Accuracy**         |           |        | **0.29** |      34 |
| **Macro Average**    |      0.22 |   0.31 |     0.25 |      34 |
| **Weighted Average** |      0.22 |   0.29 |     0.24 |      34 |

### Interpretation

Following the instructor's evaluation guidelines:

* The classifier partially learned the **Learning & Projects** and **Hardware & Boards** categories.
* **Career & Industry** remained difficult for the model.
* **Design & Debugging** achieved an F1-score of **0.00**, indicating that the classifier failed to learn this decision boundary.
* Overall accuracy (**29.4%**) was substantially below the **73.5%** zero-shot baseline.

---

# Confusion Matrix Analysis

The generated confusion matrix is summarized below.

| True Label          | Predicted Career & Industry | Predicted Learning & Projects | Predicted Hardware & Boards | Predicted Design & Debugging |
| ------------------- | --------------------------: | ----------------------------: | --------------------------: | ---------------------------: |
| Career & Industry   |                           2 |                             4 |                           3 |                            0 |
| Learning & Projects |                           2 |                             4 |                           3 |                            0 |
| Hardware & Boards   |                           1 |                             2 |                           4 |                            0 |
| Design & Debugging  |                           2 |                             1 |                           6 |                            0 |

### Interpretation

The confusion matrix shows that:

* **2 of 9 Career & Industry** posts were correctly classified.
* **4 of 9 Learning & Projects** posts were correctly classified.
* **4 of 7 Hardware & Boards** posts were correctly classified.
* **0 of 9 Design & Debugging** posts were correctly classified.

The largest confusion occurred between **Design & Debugging** and **Hardware & Boards**, indicating that the model struggled to distinguish FPGA debugging discussions from hardware-oriented discussions.

Unlike the earlier interrupted Colab execution, the rerun did not collapse into predicting a single class. Instead, the model distributed predictions across three classes, although the debugging category remained completely unlearned.

---

# Wrong Prediction Review

The notebook reported:

**27 incorrect predictions out of 34 test examples.**

Following the milestone instructions, three representative misclassifications were reviewed.

## Example 1

**Post**

> Technical interview at Graphcore for design position

**True Label:** Career & Industry

**Predicted Label:** Learning & Projects

**Confidence:** 0.27

### Analysis

This post discusses an FPGA employment opportunity and technical interview. The classifier likely associated the word **design** with technical project work rather than employment, leading to an incorrect prediction.

---

## Example 2

**Post**

> I have previously worked with Artix-7. I have to get familiarised with the VPK180 Versal board.

**True Label:** Hardware & Boards

**Predicted Label:** Learning & Projects

**Confidence:** 0.28

### Analysis

The discussion focuses primarily on FPGA hardware platforms. However, the classifier appears to have interpreted the phrase **get familiarised** as a learning activity rather than recognizing the hardware context.

---

## Example 3

**Post**

> What is wrong with this Verilog?

**True Label:** Design & Debugging

**Predicted Label:** Hardware & Boards

### Analysis

This is clearly a debugging question involving Verilog. The classifier confused debugging with FPGA hardware, demonstrating that it failed to learn the distinguishing characteristics of debugging-related discussions.

---

# Diagnostics Performed

Because the fine-tuned model underperformed the baseline, several diagnostic checks were performed before documenting the results.

The following items were verified:

* Dataset size (**222** annotated Reddit posts)
* Balanced class distribution
* Train (155), validation (33), and test (34) splits
* Correct LABEL_MAP and ID_TO_LABEL mappings
* Successful Hugging Face Dataset conversion
* Successful tokenization
* Successful completion of all three training epochs
* Correct model loading
* Correct Transformers installation (version **5.12.0**)

No evidence of data corruption, label mapping errors, tokenization errors, or runtime failures was found.

---

# Diagnostic Interpretation

Inspection of the evaluation metrics, confusion matrix, and prediction outputs indicates that the classifier learned partial decision boundaries for the **Career & Industry**, **Learning & Projects**, and **Hardware & Boards** categories.

However, the classifier completely failed to learn the **Design & Debugging** category, resulting in zero precision, zero recall, and zero F1-score.

The confusion matrix further suggests that many debugging discussions were interpreted as hardware discussions, indicating that the semantic boundary between these categories was not effectively captured by the fine-tuned classifier.

Although the model learned more balanced predictions than the earlier interrupted Colab execution, its overall performance remained substantially below the zero-shot baseline.

---

# Section 6: Baseline vs Fine-Tuned Comparison

The official notebook compared the Milestone 4 baseline with the Milestone 5 fine-tuned model.

| Model                     |  Accuracy |
| ------------------------- | --------: |
| Zero-shot Baseline (Groq) | **0.735** |
| Fine-Tuned DistilBERT     | **0.294** |

### Overall Result

**Fine-tuning Regression:** **0.441**

The fine-tuned DistilBERT model performed **44.1 percentage points worse** than the zero-shot Groq baseline.

---

# Exported Evaluation Files

The notebook successfully generated the required evaluation artifacts.

* `evaluation_results.json`
* `confusion_matrix.png`

Both files were downloaded from Google Colab and added to the project repository.

The confusion matrix image will be included as a supplementary figure, while a markdown version of the confusion matrix will be presented in the Milestone 6 README.

---


# Conclusion

The official DistilBERT fine-tuning experiment completed successfully using the instructor-provided notebook and default hyperparameters. The fine-tuned classifier achieved **29.4%** accuracy on the test set compared with the **73.5%** accuracy achieved by the zero-shot Groq baseline, representing a **44.1 percentage point regression**.

Analysis of the confusion matrix and per-class metrics indicates that the model partially learned the **Career & Industry**, **Learning & Projects**, and **Hardware & Boards** categories but failed to learn the **Design & Debugging** decision boundary. Extensive diagnostics verified that the dataset preparation, label mappings, tokenization, training pipeline, and evaluation process were correctly configured. Therefore, these results are reported exactly as produced by the official notebook.

Future work will investigate hyperparameter tuning, alternative transformer architectures, and training optimization techniques after the completion of the required project milestones.
---