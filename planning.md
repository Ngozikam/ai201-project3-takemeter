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

## Recurring Discussion Themes



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

