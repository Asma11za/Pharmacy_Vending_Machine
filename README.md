<h1> Vending Faramcay Machine </h1>
<h2> About </h2>

this project proposes a design to a vending machine using Finite State Machines, which will be presented in markets, restaurants, universities, and other places where people gather. The vending machine will sell medical products such as wound plasters, cotton, headache pills, and others for use when the user is suffering from an injury, or wound, or feeling unwell and cannot reach a pharmacy or hospital. Also, products related to skincare and oral care. This project involves the construction of a finite automaton that contains three main sectors which are: medicines, skincare, and oral care.

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

