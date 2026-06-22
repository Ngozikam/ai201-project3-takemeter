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

