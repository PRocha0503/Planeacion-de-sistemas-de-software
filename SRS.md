# Software Requirements Specification

## TC3004B.102 - Team 3 "Blueprint"

## Tecnológico de Monterrey - Campus Campus Santa Fe

---

Version 0.1

Prepared by **Salvador Salgado Normandia**

---

## Participants

- Pablo Rocha - A01028638

- Miguel Arriaga - A01028570

- Stephan Guingor - A01029421

- Salvador Salgado - A01422874

- Jacobo Soffer

---

_3/01/2023_

---

# Table of Contents

- [Software Requirements Specification](#software-requirements-specification)
  - [TC3004B.102 - Team 3 "Blueprint"](#tc3004b102---team-3-blueprint)
  - [Tecnológico de Monterrey - Campus Campus Santa Fe](#tecnológico-de-monterrey---campus-campus-santa-fe)
  - [Participants](#participants)
- [Table of Contents](#table-of-contents)
  - [Revision History](#revision-history)
  - [1. Introduction](#1-introduction)
    - [1.1 Document Purpose](#11-document-purpose)
    - [1.2 Product Scope](#12-product-scope)
    - [1.3 Definitions, Acronyms and Abbreviations](#13-definitions-acronyms-and-abbreviations)
    - [1.4 References](#14-references)
    - [1.5 Document Overview](#15-document-overview)
  - [2. Product Overview](#2-product-overview)
    - [2.1 Product Perspective](#21-product-perspective)
    - [2.2 Product Functions](#22-product-functions)
    - [2.3 Product Constraints](#23-product-constraints)
    - [2.4 User Characteristics](#24-user-characteristics)
    - [2.5 Assumptions and Dependencies](#25-assumptions-and-dependencies)
    - [2.6 Apportioning of Requirements](#26-apportioning-of-requirements)
  - [3. Requirements](#3-requirements)
    - [3.1 External Interfaces](#31-external-interfaces)
      - [3.1.1 User interfaces](#311-user-interfaces)
      - [3.1.2 Hardware interfaces](#312-hardware-interfaces)
      - [3.1.3 Software interfaces](#313-software-interfaces)
    - [3.2 Functional](#32-functional)
    - [3.3 Quality of Service](#33-quality-of-service)
      - [3.3.1 Performance](#331-performance)
      - [3.3.2 Security](#332-security)
      - [3.3.3 Reliability](#333-reliability)
      - [3.3.4 Availability](#334-availability)
    - [3.4 Compliance](#34-compliance)
    - [3.5 Design and Implementation](#35-design-and-implementation)
      - [3.5.1 Installation](#351-installation)
      - [3.5.2 Distribution](#352-distribution)
      - [3.5.3 Maintainability](#353-maintainability)
      - [3.5.4 Reusability](#354-reusability)
      - [3.5.5 Portability](#355-portability)
      - [3.5.6 Cost](#356-cost)
      - [3.5.7 Deadline](#357-deadline)
      - [3.5.8 Proof of Concept](#358-proof-of-concept)
  - [4. Verification](#4-verification)
  - [5. Appendixes](#5-appendixes)

## Revision History

| Name             | Date    | Reason For Changes | Version |
| ---------------- | ------- | ------------------ | ------- |
| Salvador Salgado | 3/01/23 | Document Creation  | v1.0    |
|                  |         |                    |         |
|                  |         |                    |         |

## 1. Introduction

### 1.1 Document Purpose

This is s a comprehensive document that outlines the requirements and specifications for the software project. It serves as a roadmap for the development team, providing a clear understanding of what is expected of the software and how it will be designed, developed, tested, and deployed.

It will define the scope of the software project, including its goals, objectives, features, and functions. It provides a clear description of the software's behavior, user interactions, and performance requirements. It identifies any constraints or limitations that may affect the software's design and development.

In addition to serving as a guide for the development team, it will serve as a communication tool for stakeholders, such as project managers, clients, and end-users. It helps ensure that all parties have a clear understanding of the software's requirements and expectations, reducing the risk of miscommunication and misunderstandings.

### 1.2 Product Scope

The product scope for this project entails the development of a web page that enables efficient and seamless communication between car agencies and their clients. Our collaboration with NDS Cognitive Labs has prompted the identification of key objectives and requirements for the software, including the need for a user-friendly interface that simplifies the online process for both salespersons and clients.

To achieve this goal, it is essential to design a web page that provides clear and concise information regarding the current stage of the purchasing process. The user interface should be intuitive and straightforward, allowing clients to search for their desired vehicle without encountering technical barriers or complex filters.

In order to ensure the success of the project, it is important to understand the needs and preferences of both the car agencies and their clients. This includes conducting thorough market research and analysis to identify common pain points and concerns related to the purchasing process.

Furthermore, the software should be designed with scalability in mind to accommodate future growth and expansion. As such, the product scope must also include provisions for future updates and improvements to enhance the user experience and maintain the software's competitiveness in the marketplace.

In summary, the product scope for this project is to develop a web page that facilitates smooth and intuitive communication between car agencies and their clients, with a focus on providing an easy-to-use service that simplifies the online purchasing process for all parties involved.

### 1.3 Definitions, Acronyms and Abbreviations

<br>

- AWS - Amazon Web Services
- Amazon EC2 - Amazon Elastic Compute Cloud
- Amazon RDS - Amazon Relational Database Service
- Amazon ELB - Amazon Elastic Load Balancer

<br>

### 1.4 References

### 1.5 Document Overview

This document is divided into 5 sections. The first section is the introduction, which will explain the purpose of the document, the scope of the project, and the definitions, acronyms and abbreviations that will be used throughout the document. The second section will be the product overview, which will explain the context and origin of the product being specified in this SRS. The third section will be the requirements, which will explain the functional, non-functional, and design requirements of the product. The fourth section will be the verification, which will explain the verification and validation of the product.

The rest of the document will explain the various elements that define how the application is expected to work based on the user characteristics ( vendors and customers), the specific needs of the product owner, as well as the architecture proposal.

## 2. Product Overview

### 2.1 Product Perspective

The product being specified in this SRS is a new, self-contained web page that enables simple and intuitive communication between car agencies and their clients. This project is a collaboration between the development team and NDS Cognitive Labs, with the aim of creating an online platform that facilitates a smooth purchasing process for both the car agencies and their clients.

The main objective of the project is to provide an easy-to-use service that allows salespersons and clients to have a clear understanding of the current stage of the purchasing process. The web page will also feature an intuitive search option without any technical filters.

The product is a standalone software component that will serve as the interface between car agencies and their clients. It is not a follow-on member of a product family, nor is it a replacement for any existing systems. The web page will be the primary means of communication between the two parties and will be built from scratch.

The larger system that this product will be a component of is the car sales process. The product's functionality will directly impact the smoothness and efficiency of this process. The external interfaces of the product will include the car agency's website and the clients' devices, such as smartphones and laptops.

### 2.2 Product Functions

Thanks to various meetings that we had with NDS, we were able to identify crucial components that were necessary for the final product.

<br>

**Facilitate Car Search for non Technical Clients**

The system will be able to allow car searches without the help of advanced filters.

_ex: “Big red car for 6 people”_

<br>

**Facilitate Acquisition process**

Both clients and vendors will be able to observe the current status of the purchasing process in real time. (Documents approvals, Drive Testing, Payment Verification)

<br>

**Data Analysis**

Automotive Groups, Agencies, Manager and Vendors will be able to get data insights depending on its roles for futures actions.

_ex: Manager will have insight of the number of sells per Vendor, Automotive Groups will be able to preview the top sell Agencies and average reviews from vendors._

<br>

**Online Payment**

The system will allow clients to make the payments online payments directly to the agencies.

<br>

**Agency Catalog/Services Upload**

The various Agencies will be able to upload their various car catalogs, payments options as well as assurance services.

<br>

The full users stories can be found in [User stories](wiki/User%20Stories.md)

Some potential product constraints for this project could include:

Interfaces: The web application will need to have a user-friendly interface that allows users to easily search for cars and dealerships. It will also need to have an interface for dealerships to upload their inventory and manage orders. Additionally, the application may need to integrate with other third-party applications or services, such as payment processors or shipping providers.
Quality of service: The web application should be reliable, fast, and secure. Users should be able to access the site at all times, and their data should be protected from unauthorized access or data breaches. The application should also be scalable to handle increased traffic as more users and dealerships sign up.
Standards compliance: The application should comply with any relevant industry standards, such as those around data privacy or online sales. It should also adhere to any relevant laws or regulations, such as those governing the sale of vehicles.
Design and implementation: The application should be designed to be accessible to users with disabilities, and should be optimized for mobile devices as well as desktop computers. The developers may also need to choose a suitable technology stack for the project, taking into account factors such as cost, ease of use, and compatibility with existing systems. Finally, the application should be easy to maintain and update over time.

### 2.4 User Characteristics

Identify the various user classes that you anticipate will use this product. User classes may be differentiated based on frequency of use, subset of product functions used, technical expertise, security or privilege levels, educational level, or experience. Describe the pertinent characteristics of each user class. Certain requirements may pertain only to certain user classes. Distinguish the most important user classes for this product from those who are less important to satisfy.

There are going to be four types of users in the web application:

#### Regular Users (Car buyers)

- Regular users are able to sign up for a user level account.

- User will be able able to create an account in the app.

- The user will be able to use their credentials to log in to the app.

- A regular user can see cars.

- A regular user can do all the process of buying cars

#### Super Admins (Application manager)

- The super admin can approve or deny a automobile group

- The super admin can remove a automobile group.

- The super admin can update a automobile group.

- Super admins can view: Dashboard to manage automobile groups.

- A super admin can validate the documents of an automobile group.

#### Admins (Car group owner)

- Only car group owner can preform the following actions: Add dealerships, Remove Dealerships, Modify dealerships.

- Only car group owner can preform the following actions: Add a manager, Remove a manager, Modify a manager

#### Managers (Car dealership manager)

- Only dealership manager can preform the following actions: Add a salesman, Remove a salesman, Modify a salesman

#### Salesman (Car dealership salesman)

- Only a salesman or manager can perform: Add a car, Remove a car, Modify a car

- A salesman can approve or deny user documents.

### 2.5 Assumptions and Dependencies

List any assumed factors (as opposed to known facts) that could affect the requirements stated in the SRS. These could include third-party or commercial components that you plan to use, issues around the development or operating environment, or constraints. The project could be affected if these assumptions are incorrect, are not shared, or change. Also identify any dependencies the project has on external factors, such as software components that you intend to reuse from another project, unless they are already documented elsewhere (for example, in the vision and scope document or the project plan).

### 2.6 Apportioning of Requirements

Apportion the software requirements to software elements. For requirements that will require implementation over multiple software elements, or when allocation to a software element is initially undefined, this should be so stated. A cross reference table by function and software element should be used to summarize the apportioning.

Identify requirements that may be delayed until future versions of the system (e.g., blocks and/or increments).

## 3. Requirements

> This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.

> The specific requirements should:

- Be uniquely identifiable.
- State the subject of the requirement (e.g., system, software, etc.) and what shall be done.
- Optionally state the conditions and constraints, if any.
- Describe every input (stimulus) into the software system, every output (response) from the software system, and all functions performed by the software system in response to an input or in support of an output.
- Be verifiable (e.g., the requirement realization can be proven to the customer's satisfaction)
- Conform to agreed upon syntax, keywords, and terms.

### 3.1 External Interfaces

> This subsection defines all the inputs into and outputs requirements of the software system. Each interface defined may include the following content:

- Name of item
- Source of input or destination of output
- Valid range, accuracy, and/or tolerance
- Units of measure
- Timing
- Relationships to other inputs/outputs
- Screen formats/organization
- Window formats/organization
- Data formats
- Command formats
- End messages

#### 3.1.1 User interfaces

Define the software components for which a user interface is needed. Describe the logical characteristics of each interface between the software product and the users. This may include sample screen images, any GUI standards or product family style guides that are to be followed, screen layout constraints, standard buttons and functions (e.g., help) that will appear on every screen, keyboard shortcuts, error message display standards, and so on. Details of the user interface design should be documented in a separate user interface specification.

Could be further divided into Usability and Convenience requirements.

#### 3.1.2 Hardware interfaces

Describe the logical and physical characteristics of each interface between the software product and the hardware components of the system. This may include the supported device types, the nature of the data and control interactions between the software and the hardware, and communication protocols to be used.

#### 3.1.3 Software interfaces

Describe the connections between this product and other specific software components (name and version), including databases, operating systems, tools, libraries, and integrated commercial components. Identify the data items or messages coming into the system and going out and describe the purpose of each. Describe the services needed and the nature of communications. Refer to documents that describe detailed application programming interface protocols. Identify data that will be shared across software components. If the data sharing mechanism must be implemented in a specific way (for example, use of a global data area in a multitasking operating system), specify this as an implementation constraint.

### 3.2 Functional

> This section specifies the requirements of functional effects that the software-to-be is to have on its environment.

### 3.3 Quality of Service

> This section states additional, quality-related property requirements that the functional effects of the software should present.

#### 3.3.1 Performance

If there are performance requirements for the product under various circumstances, state them here and explain their rationale, to help the developers understand the intent and make suitable design choices. Specify the timing relationships for real time systems. Make such requirements as specific as possible. You may need to state performance requirements for individual functional requirements or features.

#### 3.3.2 Security

Specify any requirements regarding security or privacy issues surrounding use of the product or protection of the data used or created by the product. Define any user identity authentication requirements. Refer to any external policies or regulations containing security issues that affect the product. Define any security or privacy certifications that must be satisfied.

#### 3.3.3 Reliability

Specify the factors required to establish the required reliability of the software system at time of delivery.

#### 3.3.4 Availability

Specify the factors required to guarantee a defined availability level for the entire system such as checkpoint, recovery, and restart.

### 3.4 Compliance

Specify the requirements derived from existing standards or regulations, including:

- Report format
- Data naming
- Accounting procedures
- Audit tracing

For example, this could specify the requirement for software to trace processing activity. Such traces are needed for some applications to meet minimum regulatory or financial standards. An audit trace requirement may, for example, state that all changes to a payroll database shall be recorded in a trace file with before and after values.

### 3.5 Design and Implementation

#### 3.5.1 Installation

Constraints to ensure that the software-to-be will run smoothly on the target implementation platform.

#### 3.5.2 Distribution

Constraints on software components to fit the geographically distributed structure of the host organization, the distribution of data to be processed, or the distribution of devices to be controlled.

#### 3.5.3 Maintainability

Specify attributes of software that relate to the ease of maintenance of the software itself. These may include requirements for certain modularity, interfaces, or complexity limitation. Requirements should not be placed here just because they are thought to be good design practices.

#### 3.5.4 Reusability

<!-- TODO: come up with a description -->

#### 3.5.5 Portability

Specify attributes of software that relate to the ease of porting the software to other host machines and/or operating systems.

#### 3.5.6 Cost

Specify monetary cost of the software product.

#### 3.5.7 Deadline

Specify schedule for delivery of the software product.

#### 3.5.8 Proof of Concept

<!-- TODO: come up with a description -->

## 4. Verification

> This section provides the verification approaches and methods planned to qualify the software. The information items for verification are recommended to be given in a parallel manner with the requirement items in Section 3. The purpose of the verification process is to provide objective evidence that a system or system element fulfills its specified requirements and characteristics.

<!-- TODO: give more guidance, similar to section 3 -->
<!-- ieee 15288:2015 -->

## 5. Appendixes
