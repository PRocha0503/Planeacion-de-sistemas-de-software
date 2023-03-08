# Margin analysis

Created: February 23, 2023 8:43 PM
Tags: document

https://docs.google.com/spreadsheets/d/1B4pnLQR6o9n3wHE4W2kySKOTJ2633y0_mNqFTItosjU/edit?usp=sharing

## Effort estimate

|                    | Topic                      | Development team | Client | MA (IN MD) | JS (IN MD) | PR JS (IN MD) | SG (IN MD) | SS (IN MD) | Total | With 20% Protection Margin |
| ------------------ | -------------------------- | ---------------- | ------ | ---------- | ---------- | ------------- | ---------- | ---------- | ----- | -------------------------- |
| Project Management | Project Management         | C                | O      | 3          | 3          | 3             | 3          | 3          | 15    | 15                         |
| Definition         | User stories               | O                | S      | 1          | 1          | 1             | 1          | 1          | 5     | 6                          |
|                    | Requirements               | C                | O      | 1          | 1          | 1             | 1          | 1          | 5     | 5                          |
|                    | Architecture               | O                | S      | 1          | 2          | 1             | 3          | 1          | 8     | 9.6                        |
|                    | Wireframes                 | O                | S      | 1          | 0          | 1             | 1          | 1          | 4     | 4.8                        |
| Database           | Table definition           | O                | S      | 2          | 2          | 2             | 2          | 2          | 10    | 12                         |
|                    | Relationship definition    | O                | S      | 0.5        | 0.5        | 0.5           | 0.5        | 0.5        | 2.5   | 3                          |
|                    | Documentation              | O                | S      | 2          | 1          | 0             | 1          | 3          | 7     | 8.4                        |
|                    | DB Configuration           | O                | S      | 1          | 2          | 2             | 2          | 1          | 8     | 9.6                        |
| Backend            | User validation            | O                | S      | 2          | 4          | 4             | 2          | 2          | 14    | 16.8                       |
|                    | Data validation            | O                | S      | 2          | 2          | 2             | 2          | 2          | 10    | 12                         |
|                    | Encrypt data               | O                | S      | 1          | 1          | 1             | 1          | 1          | 5     | 6                          |
|                    | Documentation              | O                | C      | 1          | 1          | 1             | 1          | 4          | 8     | 9.6                        |
|                    | Implementation             | O                | S      | 4          | 9          | 9             | 5          | 3          | 30    | 36                         |
| Frontend           | UI                         | O                | S      | 3          | 0          | 2             | 3          | 3          | 11    | 13.2                       |
|                    | UX                         | O                | S      | 1          | 0          | 2             | 1          | 3          | 7     | 8.4                        |
|                    | Architect Implementation   | O                | S      | 2          | 5          | 1             | 3          | 2          | 13    | 15.6                       |
|                    | Development                | O                | S      | 8          | 9          | 8             | 8          | 8          | 41    | 49.2                       |
| Validation         | Dataflow                   | S                | O      | 2          | 0.5        | 1.5           | 1.5        | 1.5        | 7     | 7                          |
|                    | Control flow               | S                | O      | 2          | 0.5        | 1.5           | 1.5        | 1.5        | 7     | 7                          |
|                    | Integration tests          | S                | O      | 2          | 0.5        | 1.5           | 2          | 1.5        | 7.5   | 7.5                        |
|                    | Unit tests                 | S                | O      | 2          | 1          | 1.5           | 1          | 1.5        | 7     | 7                          |
| Devops             | Deploy frontend            | C                | O      | 0.5        | 0.5        | 0.5           | 0.5        | 0.5        | 2.5   | 2.5                        |
|                    | Implement CI / CD pipeline | C                | O      | 1.5        | 1.5        | 1.5           | 1.5        | 1.5        | 7.5   | 7.5                        |
|                    | Deploy backend             | C                | O      | 0.5        | 0.5        | 0.5           | 0.5        | 0.5        | 2.5   | 2.5                        |
| Total              |                            |                  |        | 47         | 48.5       | 50            | 49         | 50         | 244.5 | 281.2                      |

- S - SUPPORT

- O - OWNER

- C - CONTRIBUTION

## Margin

| Project Duration (months) | 6     |
| ------------------------- | ----- |
| Total effort in MD        | 245   |
| MD + Margin               | 281.2 |

| Total Effort in MD | 281  | %           |
| ------------------ | ---- | ----------- |
| MA                 | 0.19 | 54.05480573 |
| SG                 | 0.20 | 55.7799591  |
| SS                 | 0.20 | 57.50511247 |
| PR                 | 0.20 | 56.35501022 |
| JS                 | 0.20 | 55.7799591  |
|                    |      |             |

| Description              | Cost       |
| ------------------------ | ---------- |
| Salary per MD            | $1,000.00  |
| Cost of service by month | $9,000.00  |
| Salary Total             | $281,200   |
| Total service costs      | $54,000.00 |
| Revenue ($)              | $502,800   |
| Total internal cost ($)  | $335,200   |
| Profit ($)               | $167,600   |
| Margin (%)               | 50%        |
