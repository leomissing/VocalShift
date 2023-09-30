# ML System Design Doc 
# ML System Design Doc - VocalShift
## 1. Objectives and Background
### 1.1. Why engage in product development?

- **Business Objective:** The primary goal of this project is to create a chatbot that can generate AI song cues using a neural network, thereby revolutionizing the music industry by offering personalized music experiences to users.

- **Improvement over Current State:** This project aims to provide a significant improvement over the current state by enabling users to replace the artist's voice in any song while maintaining audio quality and emotional authenticity.

- **Success Criteria:** Success for this project, from a business perspective, will be measured by the achievement of key performance indicators (KPIs), including an increase in user engagement, an increase in premium subscriptions, and a 95% customer satisfaction rating.


### 1.2 Business Requirements and Constraints

- **Brief Description of Business Requirements:** Detailed business requirements have been provided by the Product Owner, including the need for real-time AI song cue generation, integration with popular music streaming platforms, and scalability to handle millions of concurrent users.

- **Business Constraints:** The project must adhere to a budget of $0 and must be launched within 3-4 months to align with market demand.

- **Iteration Success Criteria:** Each iteration must meet specific success criteria defined by the Product Owner, such as achieving a minimum user adoption rate of 5% for new features.

- **Pilot Business Process:** During the pilot phase, the AI song cues will be integrated into telegram chat with the ability for the user to select unique voices for songs and share them with their contacts.

- **Successful Pilot:** The pilot will be considered successful if user engagement increases within three months of deployment, with a retention rate of 90%. Potential paths for project expansion include exploring partnerships with major record labels.


### 1.3. Project Scope

- **In-Scope for Current Iteration:** The current iteration will focus on implementing specific business requirements outlined in the documentation provided by the Product Owner.
- **Out-of-Scope for Current Iteration:** Certain features or requirements may not be addressed in the current iteration.
- **Code Quality and Reproducibility:** The Data Scientist will ensure code quality and the reproducibility of the solution.
- **Technical Debt:** A description of any technical debt that may be incurred during the project and what will be deferred for future productization.

- **In-Scope for Current Iteration:** The current iteration will focus on creating a basic MVP with the ability to load any melody and select a new performer’s voice for it from the list of available ones.

- **Out-of-Scope for Current Iteration:** Advanced features like emotion customization and internationalization will not be addressed in the current iteration.

- **Code Quality and Reproducibility:** The Data Scientist will ensure code quality by following industry best practices and ensuring that the code is well-documented and version-controlled. Reproducibility will be achieved by sharing code, model weights, and data sources.

- **Technical Debt:** Technical debt will be minimized, but certain optimizations may be deferred for future iterations to meet the project timeline.


### 1.4. Solution Assumptions

- **General Solution Assumptions:** The system will rely on certain assumptions related to data sources, forecast horizon, model granularity, and other factors, as justified by business requirements.

- **Data Blocks:** The system relies on data blocks such as audio recordings, lyrics, and emotion metadata to train and generate AI song cues.

- **Forecast Horizon:** The model's forecast horizon aligns with the real-time requirements, ensuring a seamless user experience.

- **Granularity of Model:** The model's granularity aligns with the requirements defined by the Product Owner, capturing subtle nuances in the music.


## 2. Methodology 
### 2.1. Problem statement
The task of extracting vocals from a song and converting it into another vocal voice while maintaining pitch and intonation.

### 2.2. Block diagram of the solution 

### 2.3. Stages of solving the problem
#### 2.3.1. Choosing metrics

#### 2.3.2. Object and target
Object is a song with the original vocal track.

Target variable is a song with a vocal track replaced by different artist

#### 2.3.3. Data

#### 2.3.4. Data preparation

## 4. Realization
