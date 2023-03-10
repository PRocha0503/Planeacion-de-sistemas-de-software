# Test Plan

Created: March 6, 2023 5:25 PM
Last edited time: March 9, 2023 8:41 PM
Tags: document

# Table of contents

# Document Information

**Version**: 0.0.1

**Status:** DRAFT

### Team

Pablo Rocha Ojeda

Miguel Arriaga Velasco

Jacobo Soffer Levy

# Revision and Sign Off Sheet

## Document History

| Version | Date | Author | Description of Change |
| --- | --- | --- | --- |
| 0.0.1 | 06/03/2023 | Pablo Rocha, Miguel Arriaga, Jacobo Soffer | Initial Commit:
Structure and introduction |
| 0,0.2 | 08/03/2023 | Salvador Salgado | Test Strategy |

## Approvers Lists

| Name | Role | Status | Approval Date | Signature |
| --- | --- | --- | --- | --- |
| Gilberto Echeverria |  |  |  |  |
| Esteban Castillo Juarez |  |  |  |  |
| Eduardo Rubinstein |  |  |  |  |
| Ivan Santiago |  |  |  |  |

### Reference Documents

| Version | Date | Document |
| --- | --- | --- |
|  |  |  |
|  |  |  |

# 1. Introduction

## 1.1 Purpose

The purpose of the testing document  is to outline the various tests that will be conducted to ensure the software is working as intended. This document provides a comprehensive overview of the software testing process, including the test plan, test cases, and expected results. The document will ensure  that all aspects of the software are thoroughly tested and that any potential defects are identified and corrected before release. Additionally, it will serve as a reference guide for future testing and development, providing valuable insights and information for developers and testers to use in future projects. 

In particular it will include:

- 

## 1.2 Project Overview

The project aims to create a website that offers customers the ability to purchase a car entirely online. The website will feature a range of services, including searching for vehicles, making payments, communicating with sellers and dealerships, scheduling test drives, uploading documents, and more.

The project will also include an admin interface. This will allow automobile groups to register in the page, add their different dealerships and corresponding managers. Managers will be able to define the salesmen. From there the salesman and end user will be able to interact.

## 1.3 Audience

This document will serve as a comprehensive guide for team members to ensure that everyone is on the same page regarding the testing requirements for our project. It will be accessible to members of other teams, including approvers who will review and provide feedback on the document. The SCRUM master will rely on the document to plan the sprints in which the testing will occur and ensure that the testing is completed within the established deadlines.

Additionally, the document will be an integral part of our wiki, providing clients with the opportunity to review the testing requirements and ensure that they are being satisfactorily met. The document will contain detailed instructions that developers must follow to write tests or perform manual tests effectively. By using this document, we can ensure that all testing is done uniformly across the entire project, resulting in a higher quality final product. 

In summary:

- This document will be written by team members for them to use, including members of other teams in case that our project gets selected to use for the entire class.
- The approvers will also be able to read and review this document, indicating in case of any comments or areas of opportunities.
- The SCRUM master will use this document to plan the sprints in which the testing will occur, ensuring that the deadlines for the testing are met.
- This document will also be part of our wiki, in case that the clients want to review the document and make sure that the testing requirements are being satisfied.
- The developers must use this document in order to write tests or perform manual tests as it is indicated in this document.

# 2. Test strategy

## 2.1 Test Description

Taking into account the project deadline and complexity of the project the team has decided to create a strategy that focuses on black-box testing and informal testing. 

This was decides as black-box testing is particularly useful when there is limited time for testing.  By focusing on black-box testing and informal testing, the team can will identify any major issues or bugs in the system without spending too much time on testing.

On the other hand as is it is a complex project with many modules, it may be difficult to test each component in isolation. In this case, black-box testing can help the team identify any issues with the system as a whole, rather than focusing on individual components. Similarly, informal testing can help the team get a better understanding of how the system behaves in the real world, which may not be apparent through more formal testing methods.

Finally as we will be working in big team black-box and informal testing will allow all developers to create tests for any part of the system as they will not need to know all the insides of the code.

We will mainly focus on un unit, integration and some end to end testing. This will  ensure that the system is thoroughly tested at all levels. By testing each component in isolation, as well as how different components work together and the system as a whole, the team can identify and address any issues or bugs early in the development process, before they become more difficult and costly to fix.

- Unit testing is  automated and can be run quickly, making it an efficient way to identify and address issues early in the development process.
- Integration testing is important for our complex systems with many interconnected components, where it can be difficult to identify issues through other types of testing..
- End-to-end testing simulates real-world scenarios and user interactions, and can help the team identify any issues or bugs that may arise in the system.

## 2.2 Test Objectives

The goal of testing is to ensure that the functional and non-functional requirements of the web application are being met. As well as ensuring that the application is stable, bug-free, scalable and fast.

Some of the requirements that we will be testing are the following: 

- The clients are able to make their payments online to the agency, using existing payment services: Stripe
- The client is able to select from a variety of payment types: Down payment, Financing, Upfront payment
- Car dealership can perform CRUD operations on cars through admin dashboard
- The salesman is able to manage driving tests for users.
- The manager of a car agency can define the payment plans that they offer.
- The user will be able to create and use their credentials to log in to the app.

The complete list of requirements can be found in:

- [Functional Requirements](https://github.com/PRocha0503/Planeacion-de-sistemas-de-software/blob/main/wiki/Functional%20requirements.md)
- [Non Functional Requirements](https://github.com/PRocha0503/Planeacion-de-sistemas-de-software/blob/main/wiki/Non%20Functional%20requirements.md)

## 2.3 Test Assumptions

### 2.3.1 Key assumptions

1.  Software is being run on a compatible environment with all dependencies installed.
2. All tests are being run on the same environment.
3. Due to time and budget constraints, only functional tests will be performed.
4. Black box tests will be performed first.
5. For the same inputs, the tests should always produce the same outputs.
6. White box testing will be reserved as a fallback option in case the black box tests fail.
7. Test and their results will be documented.
8. Tests will be a collaborative effort between developers, development leads and project manager.
9. The project manager will review all tests deliverables.

### 2.3.2 General

1. Most of the testing will be used for the functional requirements
2. Every test should always return the same outcome
3. All critical priority functionalities need to be tested 
4. It is important to follow the step-by-step testing for every function (informal testing, black box testing, integration testing)
5. Every test will require documentation
6. All test must have all the inputs necessary to ensure it is working correctly as well as the outputs expected.
7. For every test there must a standard template that allows better structure.
8. In order to conclude a test it has to be approved by PM.
9. Before the test execution, the Business Analyst has to review and approve the test cases.

## 2.4 Test Objects

1. Test the login 
2. Test the signup
3. Test the search
4. Test role assignment
5. Test car uploads
6. Test the payment
7. Test the costumer dashboard view
8. Test the agency dashboard view

## 2.5 Scope

The web functionality that will be tested includes:

- User authentication
- Role management
- Search feature
- Consumer Dashboard
- Admin Dashboard
- Car and dealership upload
- Payments
- Data Visualization

### 2.5.1 User authentication

- Users are able to log in through the UI:
    - If the right credentials are entered, they will be redirected to the home page or previous page.
    - If the wrong credentials are entered, an error message alerts the user of their mistake.
- Users are able to access the backend and retrieve information (if they have permission) using their access token:
    - Access tokens have enough information to identify and authorize any given user.
    - The backend recognizes access tokens.
    - Expired or invalid access tokens are rejected.
    - Revoked refresh tokens are rejected.
    - Users can fetch a fresh access token through their refresh token.
    - Unauthenticated users are rejected.
    - Requests from users with missing permissions are rejected

### 2.5.2 Role management

- Admin users are able to assign roles to other users through the UI
    - There is a list of roles that can be selected to assign the user
    - Only one role can be assigned at a time
    - Any user should always have a role assigned
    - Roles are scoped to a tenant

### 2.5.3 Search feature

- Natural Language Search:
    - Key terms can be extracted from a prompt, mainly filters compatible with the search system such as make, model, seats, colors, year, type of car, etc. [Link to full list when available].
    - Full text search will be applied for some fields, observations, descriptions, etc
- Users can share a url containing the applied filters
    - If user reloads the url it should not change
- Users can modify the search results by applying filters.
- As the user scrolls down results are paginated
- A search known to yield results will always yield results.
- Search results are ranked through a score based on relevance.
- If no results are found, the user is presented with a helpful error message / related searches.

### 2.5.4 Consumer Dashboard

- Consumers are able to observe all their current purchasing status in their Dashboard
- They will be able to select any of them and inspect more details (Driving Test Date, Procede to payment, current document status)
- In case the purchasing status is yet to be payed, a consumer will be able to cancel the process.
- In case the user is not a Consumer, this information will not be displayed

### 2.5.5 Admin Dashboard

- Admin will be able to visualize information depending on their role in the system (current deals processes, agency sales, vendors information, etc)
- Admin will be able to analyze the data shown for a better review
- If the user is not an admin, there will have a completely different dashboard

### 2.5.6 Car and dealership upload

- A automobile group owner is able to register a new dealership
    - Dealership data can be added
    - Dealerships documents can be uploaded
    - The automobile group owner can add a dealership manager
    - The automobile group owner can NOT add a dealership to another group
    - With incorrect information dealership is not added
- A salesman or dealership manager is able to manage  dealership cars
    - The car data can be added
    - Car addons can be added
    - Car spec sheet can be added
    - Car can be removed
    - Car data can be edited
    - With  incorrect data car ca not be added

### 2.5.7 Payments

- A user is able to pay to the agency through the UI
    - If payment succeeds/fails user should receive a notification
    - User can select their payment method
    - User can save their preferred payment method

### 2.5.8 Data Visualization

- Agency Users are able view graphs of how much each vendor is selling
- Agency Users are able to view a graph with MRR, expected MRR for next month

## 2.6 Levels of Testing

### 2.6.1 Unit testing

**PURPOSE**: The purpose of unit testing is to comprehensively test each section of the software and determine whether the software satisfies the requirements.

**SCOPE**: Unit testing will be conducted on all important sections(priority Medium or High in functional requirements).

**TESTERS**: The testing team will be responsible for conducting unit tests.

**METHOD**: The unit testing process will employ user stories, use cases, and input-output sections. In the event that the testing results in failure, white box testing will be implemented.

**TIMING**: Unit testing will be conducted at the start of each cycle.

### 2.6.2 Integration testing

**************PURPOSE**************: Integration testing will allow us to verify different components in the system work together as intended. This includes third party systems such as a payment processor.

************SCOPE:************ Main component interactions (Priority High in functional requirements)

[**Functional requirements**](/wiki/Functional%20requirements.md)

****************TESTERS:**************** Testing team, preferably one developer for each component that is being tested.

****************METHOD:**************** Integration testing will draw on user stories and functional requirements. In case of failure white box testing will be used, extending to the individual components being tested if needed and possible.

****************TIMING:**************** Integration testing will be conducted after two or more components are integrated, the components involved change their public interfaces or at the end of each cycle.

### 2.6.3 End to end testing

**PURPOSE**: E2E tests will allow us to ensure the platform is working as expected from the point of view of a user.
**SCOPE**:  Main user interactions with the platform
**TESTERS**: Testing team would be in charge of creating integration tests, ideally the team responsible for each system.
**METHOD**: E2E testing will be based on main user stories from each service. This will be a type of black box testing where we only care about user actions and the expected output.
**TIMING**: when completing the service e2e tests will be created

## 2.7 Test acceptance criteria

### 2.7.1 Unit testing

****************************Authentication****************************

Front:

- Emails and passwords should be validated before being sent to the server.
- During a loading state, the user should not be able to modify their input.
- If a success response is received:
    - If the user was on a page before logging in, the user should be redirected to said page.
    - Else, the user should be redirected to the homepage.
    - In all cases the authentication token should be stored in a cookie to be retrieved when needed.
- If an error response is received:
    - A clear error message should be displayed to inform the user.

Back:

- The backend should recognize access tokens in requests:
    - It can validate that the token is valid.
        - If the token is valid it should be stored in a request context.
        - Else the request should be aborted.
    - It can identify the user id and role from the token, if it can’t the token is invalid.
    - If the token is expired it is treated as an invalid token.
    - It authorizes requests depending on the user’s role.
- If a token is missing on a protected route the request is aborted immediately.
- Users can request a fresh authentication token using a refresh token
    - If a refresh token is expired, the request is aborted.
    - If a refresh token is revoked the request is aborted.
- Users can invalidate their refresh tokens (in case of a sign out/password change).

******************************Role and User Management******************************

Front and Back (tested in isolation):

- Managers can list the users in their dealership.
- Managers can add users to their dealership tenant.
- Managers can delete users from their dealership tenant.
- Managers assign roles to users and can only assign one of the roles recognized by the system.
- Every user must have one and only one role assigned.
- Roles are scoped to a tenant.

Front End only

- In case of a success response to any request a success message is displayed and the interface accordingly.
- In case of an error response to any request an error message is displayed.

**********Search Functionality**********

- Users can see and apply filters from the UI.
- If no results are found, the user is presented with a helpful error message / related searches.

### 2.7.2 Integration testing

> Nota: Para search hacer integration test the natural language y del url. Casi todo lo de search es un integration test.
> 

**Payments functionality:**

- At the end of the month the user should recieve an email with the total usage, it should be automatically charged to the preferred method
- Track usage of created listings in stripe
- Transferring money to destination account from user, and getting a commision to NDS account.

**Search functionality:**

- When creating a new listing data should be available in elastic search, we then should be able to use the search service to view it.
- Do a natural language search from the frontend and see extracted keywords in the frontend as well as relevant results
- User can pay to have priority in the search system, and when searching have the listing at the top

**Chat functionality:**

- Users can send a message through a chat interface in the frontend, and an agent from the agency should be able to reply through the admin dashboard. Only vendors are able to use the chat system to reply.

**Admin Dashboard:**

- Salesmans should only be able to create new cars, car variants and new listings
- Admins should be able to create agencies
- Managers should not be able to see other agencies

**Metrics System:**

- Depending on a rol you can see different metrics
- Logs are being generated after creating a subscription

**Devops:**

- After a merge to production containers are deployed to cloud enviorment with k8s

### 2.7.3 End to end testing

- 
- 

## 2.8 Test Deliverables

| No. | Name | Author | Reviewer |
| --- | --- | --- | --- |
| 1 | Test Plan | Team | Esteban Castillo |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |

## 2.9 Milestone List

|  | Test Type | Test Example (SUT) | Dependency (DOC) |
| --- | --- | --- | --- |
| 1 | Unit testing | Login functionality test. | Login front end page, login endpoint, database created. |
| 2 | Unit testing | Buy a car functionality | Buy a car endpoint, database, interface, stripe integration. |
| 3 | Unit testing | Search test | Elastic setup for search, database, filters | natural language |
| 4 | Integration testing | Backend connection to stripe | Database created, buy a car endpoint |
| 5 | Integration testing | Natural language test | ChatGPT integration with backend, database created, search functionality done, database populated. |
| 6 | End to end testing | UI test from production environment. | Users will test the applications functionalities from a production environment. |

## 2.10 Test Effort Estimate

| Main functionality |  |
| --- | --- |
| Log in & sign up |  |
| Landing page |  |
| Search |  |
| Natural language |  |
| Buy a car |  |
| Chats |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

# 3. Execution strategy

## 3.1 Entry and Exit Criteria

# 4. Test Management Process

## 4.1 Test Execution Process

## 4.2 Test Risks and Mitigation Factors

## 4.3 Communications Plan and Team Roster

### 4.3.1 Role Expectations

| No. | Role | Description |
| --- | --- | --- |
| 1 | Project Manager | The person responsible for leading and managing a project from start to finish. They plan, organize, monitor, and control all aspects of the project to ensure it meets its goals and objectives. |
| 2 | Architect Lead | The person responsible for designing the overall structure and organization of a software system or application. They identify the key components and interactions needed to achieve the desired functionality and ensure the system is scalable, maintainable, and meets the requirements of the stakeholders. |
| 3 | Backend Lead | The person responsible for leading the development and maintenance of the backend system of a software application. They work closely with the Architect Lead to ensure the backend system is designed to meet the needs of the application, and oversee the backend developers who implement the design. |
| 4 | Frontend Lead | The person responsible for leading the development and maintenance of the frontend system of a software application. They work closely with the Architect Lead to ensure the frontend system is designed to meet the needs of the application, and oversee the frontend developers who implement the design. |
| 5 | Backend Developer | A software developer who specializes in implementing the server-side logic, data storage, and APIs that enable the frontend to communicate with the backend. They ensure the backend system is performant, reliable, and scalable. |
| 6 | Frontend Developer | A software developer who specializes in implementing the user interface and client-side logic of a software application. They write code in programming languages such as HTML, CSS, and JavaScript, and ensure the frontend system is responsive, accessible, and user-friendly. |
| 7 | Test Lead | The person responsible for managing the testing process of a software application. They work with the Project Manager and other leads to plan and organize the testing effort, and oversee the testing team to ensure the application is thoroughly tested and meets the quality standards. |
| 8 | Test Developer | A software developer who specializes in writing automated tests for a software application. They write code in testing frameworks and ensure the application is thoroughly tested and free of bugs. They work closely with the Test Lead to plan and execute the testing effort. |

### 4.3.2 Project Management

### 4.3.3 Test Planning (Test Lead)

### 4.3.4 Test Team

### 4.3.5 Test Lead

### 4.3.6 Development Team

### 4.3.7 Activities Schedule

# 5. Test Environment

# 6. Tests

# 7. Conclusion