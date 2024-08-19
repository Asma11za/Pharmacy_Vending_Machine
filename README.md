<h1> Vending Pharamcay Machine </h1>
<h2> About </h2>

this project proposes a design for a vending machine using Finite State Machines, which will be presented in markets, restaurants, universities, and other places where people gather. The vending machine will sell medical products such as wound plasters, cotton, headache pills, and others for use when the user is suffering from an injury, or wound, or feeling unwell and cannot reach a pharmacy or hospital. Also, products related to skincare and oral care. This project involves the construction of a finite automaton that contains three main sectors which are: medicines, skincare, and oral care.

<h2> Vending Machine State Table </h2>

| Description | State |
| --- | --- |
| Select options | Q0 |
| Select the skin care section | Q1 |
| Select the medicine section | Q2 |
| Select nail polish product | Q4 |
| Select makeup remover product | Q5 |
| Select sunscreen product | Q6 |
| Select Panadol product | Q7 |
| Select plaster product | Q8 |
| Select alcohol pads product | Q9 |
| Check availability for alcohol pads | Q19 |
| Check availability for plaster | Q18 |
| Check availability for Panadol | Q17 |
| Check availability for sunscreen | Q15 |
| Check availability for nail polish | Q13 |
| Check availability for makeup remover | Q14 |
| Product is not available. | Q32 |
| Select payment option | Q23 |
| Product purchase successful | Q3 |
| Product purchase not successful | Q34 |
| Select card payment option | Q26 |
| Select cash payment option | Q27 |
| Select payment option | Q24 |
| Product purchase not successful | Q37 |
| Select card payment option | Q28 |
| Select cash payment option | Q29 |
| Select payment option | Q25 |
| Product purchase not successful | Q40 |
| Select card payment option | Q30 |
| Select cash payment option | Q31 |
| Product is not available. | Q45 |
| Select payment option | Q42 |
| Product purchase successful | Q3 |
| Product purchase not successful | Q50 |
| Select card payment option | Q46 |
| Select cash payment option | Q47 |
| Select payment option | Q43 |
| Product purchase not successful | Q54 |
| Select card payment option | Q16 |
| Select cash payment option | Q52 |
| Select payment option | Q44 |
| Product purchase not successful | Q59 |
| Select card payment option | Q56 |
| Select cash payment option | Q57 |

<h2> Vending Machine Strings Table </h2>

| String | Abbreviation | Description |
| --- | --- | --- |
| The skincare sector is selected by the user. | Op1 | The skincare sector is selected by the user. |
| The medicine sector is selected by the user. | Op2 | The medicine sector is selected by the user. |
| The user selects Nail polish. | SelNP | The user selects Nail polish. |
| The user selects Makeup remover. | SelMR | The user selects Makeup remover. |
| The user selects SPF. | SelSPF | The user selects SPF. |
| The user selects Panadol. | SelPn | The user selects Panadol. |
| The user selects Plaster. | SelPl | The user selects Plaster. |
| The user selects Alcohol pads. | SelC | The user selects Alcohol pads. |
| To check whether the product is inside the machine or not. | CheckAv | To check whether the product is inside the machine or not. |
| The product is not inside the machine. | NotAv | The product is not inside the machine. |
| The user will go back to the start state if the product was not inside the machine which is “q0” | Pnot | The user will go back to the start state if the product was not inside the machine which is “q0” |
| The product is inside the machine. | Av | The product is inside the machine. |
| The cost of the selected product | 10 | The cost of the selected product |
| The cost of the selected product | 15 | The cost of the selected product |
| The cost of the selected product | 5 | The cost of the selected product |
| Successfully completed, the selected product has been delivered to the user. | Succ | Successfully completed, the selected product has been delivered to the user. |
| User has not received the selected product due to an unsuccessful completion. | Nots | User has not received the selected product due to an unsuccessful completion. |

<h2> Finite Automata </h2>

Continuing in the previous section, here's a drawing of the finite automata after all that has been explained, all the states and strings that are going to be involved.

<img width="1000" src="https://github.com/user-attachments/assets/5d441db6-ada4-428b-8a86-c0fa9fbc1bcf">

<h2> Scenario </h2> 

Starting from the initial state (Q0) The user has 3 sector options to choose from:
1. (Q1) Makeup Section
2. (Q2) Pharmacy Section
3. (Q3) Oral care Section
Each section has exactly 3 products with different prices, if the user selects (Q1) it will take them to the makeup section (Q1) which has 3 products to choose from:
(Q4) nail polish, (Q5) makeup remover, (Q6) SPF. So, when the user selects (Q6) for example, the machine will check first the availability of the product in the state (Q15). The availability has two cases:

• If the product is available, the user will move to state (Q25). Then the user will have two payment methods either by credit card (Q30) or cash (Q31). The process of the two methods is the same for the two states. So, if the user selects pay by credit card (Q30) the process is either successful (Q39) which is the final state, or not successful which is state (Q40) which is also a final state.

• If the product is not available, the state of the product will go back to the initial state and start the machine process. The scenario applies the same for each product in the automata.

<h2> Biuld NFA </h2>
<img width="1000" src="https://github.com/user-attachments/assets/7779096d-84fc-480d-8087-70e432a5a34a">

<h2> NFA Transition State Table </h2>

| **σ** | Op1 | Op2 | SelNP | SelMR | SelSPF | SelPn | SelPl | SelC | CheckAv | Av  | NotAv | Pnot | 10      | 15      | 55      | 5       | Nots | Succ |
| ----- | --- | --- | ----- | ----- | ------ | ----- | ----- | ---- | ------- | --- | ----- | ---- | ------- | ------- | ------- | ------- | ---- | ---- |
| Q0    | Q1  | Q2  | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q1    | Φ   | Φ   | Q4    | Q5    | Q6     | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q2    | Φ   | Φ   | Φ     | Φ     | Φ      | Q7    | Q8    | Q9   | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q4    | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Q13     | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q5    | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Q14     | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q6    | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Q15     | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q7    | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Q17     | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q8    | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Q18     | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q9    | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Q19     | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q13   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Q23 | Q32   | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q14   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Q24 | Q32   | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q15   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Q25 | Q32   | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q16   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q54  | Q3   |
| Q17   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Q42 | Q45   | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q18   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Q43 | Q45   | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q19   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Q44 | Q45   | Φ    | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q23   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Q26,Q27 | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q24   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Q28,Q29 | Φ       | Φ       | Φ    | Φ    |
| Q25   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Q30,Q31 | Φ       | Φ    | Φ    |
| Q26   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q34  | Q3   |
| Q27   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q34  | Q3   |
| Q28   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q37  | Q3   |
| Q29   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q37  | Q3   |
| Q30   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q40  | Q3   |
| Q31   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q40  | Q3   |
| Q32   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Q0   | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q42   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Q46,Q47 | Φ    | Φ    |
| Q43   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Q16,Q52 | Φ       | Φ       | Φ    | Φ    |
| Q44   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Q56,Q57 | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q45   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Q0   | Φ       | Φ       | Φ       | Φ       | Φ    | Φ    |
| Q46   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q50  | Q3   |
| Q47   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q50  | Q3   |
| Q52   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q54  | Q3   |
| Q56   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q59  | Q3   |
| Q57   | Φ   | Φ   | Φ     | Φ     | Φ      | Φ     | Φ     | Φ    | Φ       | Φ   | Φ     | Φ    | Φ       | Φ       | Φ       | Φ       | Q59  | Q3   |

<h2> DFA Transition State Table </h2>

| **σ** | Op1 | Op2 | selNP | SelMR | SelSPF | SelPn | SelPl | SelC | CheckAv | Av  | NotAv | Pnot | 10      | 15      | 55 | 5       | Nots | Succ |
| ----- | --- | --- | ----- | ----- | ------ | ----- | ----- | ---- | ------- | --- | ----- | ---- | ------- | ------- | -- | ------- | ---- | ---- |
| Q0    | Q1  | Q2  | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q1    | D   | D   | Q4    | Q5    | Q6     | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q2    | D   | D   | D     | D     | D      | Q7    | Q8    | Q9   | D       | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q4    | D   | D   | D     | D     | D      | D     | D     | D    | Q13     | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q5    | D   | D   | D     | D     | D      | D     | D     | D    | Q14     | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q6    | D   | D   | D     | D     | D      | D     | D     | D    | Q15     | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q7    | D   | D   | D     | D     | D      | D     | D     | D    | Q17     | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q8    | D   | D   | D     | D     | D      | D     | D     | D    | Q18     | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q9    | D   | D   | D     | D     | D      | D     | D     | D    | Q19     | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q13   | D   | D   | D     | D     | D      | D     | D     | D    | D       | Q23 | Q32   | D    | D       | D       | D  | D       | D    | D    |
| Q14   | D   | D   | D     | D     | D      | D     | D     | D    | D       | Q24 | Q32   | D    | D       | D       | D  | D       | D    | D    |
| Q15   | D   | D   | D     | D     | D      | D     | D     | D    | D       | Q25 | Q32   | D    | D       | D       | D  | D       | D    | D    |
| Q16   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q54  | Q3   |
| Q17   | D   | D   | D     | D     | D      | D     | D     | D    | D       | Q42 | Q45   | D    | D       | D       | D  | D       | D    | D    |
| Q18   | D   | D   | D     | D     | D      | D     | D     | D    | D       | Q43 | Q45   | D    | D       | D       | D  | D       | D    | D    |
| Q19   | D   | D   | D     | D     | D      | D     | D     | D    | D       | Q44 | Q45   | D    | D       | D       | D  | D       | D    | D    |
| Q23   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | Q26,Q27 | D       | D  | D       | D    | D    |
| Q24   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | Q28,Q29 | D  | D       | D    | D    |
| Q25   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q26   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q34  | Q3   |
| Q27   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q34  | Q3   |
| Q28   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q37  | Q3   |
| Q29   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q37  | Q3   |
| Q30   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q40  | Q3   |
| Q31   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q40  | Q3   |
| Q32   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q42   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | Q46,Q47 | D    | D    |
| Q43   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | Q16,Q52 | D  | D       | D    | D    |
| Q44   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | Q56,Q57 | D       | D  | D       | D    | D    |
| Q45   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | D    | D    |
| Q46   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q50  | Q3   |
| Q47   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q50  | Q3   |
| Q52   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q54  | Q3   |
| Q56   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q59  | Q3   |
| Q57   | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | Q59  | Q3   |
| D     | D   | D   | D     | D     | D      | D     | D     | D    | D       | D   | D     | D    | D       | D       | D  | D       | D    | D    |

<h2> Build DFA </h2>

<img width="1000" src="https://github.com/user-attachments/assets/4956f279-9672-40c3-8fae-ddbb7406b0bc">

<h2> Production Rules for NFA </h2>

q0  → Op1 q1 | Op2 q2

q1  → SelNP q4 | SelMR q5 | SelSPF q6

q2  → SelPn q7 | SelPl q8 | SelC q9

q4  → CheckAv q13

q5  → CheckAv q14

q6  → CheckAv q15

q7  → CheckAv q17

q8  → CheckAv q18

q9  → CheckAv q19

q13 → Av q23 | NotAv q32

q14 → Av q24 | NotAv q32

q15 → Av q25 | NotAv q32

q16 → Nots q54 | Succ q3

q17 → Av q42 | NotAv q45

q18 → Av q43 | NotAv q45

q19 → Av q44 | NotAv q45

q23 → 10 q26, q27

q24 → 15 q28, q29

q25 → 55 q30, q31

q26 → Nots q34 | Succ q3

q27 → Nots q34 | Succ q3

q28 → Nots q37 | Succ q3

q29 → Nots q37 | Succ q3

q30 → Nots q40 | Succ q3

q31 → Nots q40 | Succ q3

q32 → Pnot q0

q42 → 5 q46, q47

q43 → 15 q16, q52

q44 → 10 q56, q57

q45 → Pnot q0

q46 → Nots q50 | Succ q3

q47 → Nots q50 | Succ q3

q52 → Nots q54 | Succ q3

q56 → Nots q59 | Succ q3

q57 → Nots q59 | Succ q3


