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

