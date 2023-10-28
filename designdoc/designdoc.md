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
The task of extracting vocals from a song and converting it into another vocal voice while maintaining pitch and intonation utilizing artificial intelligence.

### 2.2. Block diagram of the solution 

### 2.3. Stages of solving the problem

#### 2.3.1 Metrics Selection
Offline metrics are measures that evaluate the quality of vocal track generation based on historical data and expert assessments.

- **MOS (Mean Opinion Score):** The average quality rating of vocal track generation on a five-point scale, obtained from experts or users.

- **WER (Word Error Rate):** The percentage of errors in recognizing words in the generated track compared to the original song lyrics.

- **F0 RMSE (Fundamental Frequency Root Mean Square Error):** The root mean square error in determining the fundamental frequency of sound in the generated track compared to the original.

- **MFCC (Mel-Frequency Cepstral Coefficients) Distance:** The distance between the spectral characteristics of sound in the generated and target tracks.

Online metrics are measures that can be obtained while the system is in operation.

- **CSAT (Customer Satisfaction Score):** The percentage of users who rated their experience with the chatbot as positive.

- **NPS (Net Promoter Score):** The percentage of users willing to recommend the chatbot to their friends or acquaintances.

- **Retention Rate:** The percentage of users who return to using the chatbot after their initial interaction.

- **Conversion Rate:** The percentage of users who switch to the paid version of the chatbot after using the free version.

Technical metrics are related to the system's performance and speed.

- **Latency:** The time the system takes to process a user's request and generate a response.

- **Throughput:** The number of requests the system can process per unit of time.

- **Availability:** The percentage of time when the system is available and functioning correctly.

- **Error Rate:** The percentage of requests that the system couldn't process or processed incorrectly.

The selection of these metrics allows us to assess the system's effectiveness from various angles, including generation quality, user satisfaction, and system performance. This will enable us to make more informed decisions and enhance the chatbot in line with project requirements and business objectives.

#### 2.3.2. Object and target
Object is a song with the original vocal track.

Target variable is a song with a vocal track replaced by different artist

#### 2.3.3. Data
The data are blocks linking audio tracks annotated with song lyrics and emotion metadata.

#### 2.3.4. Data preparation

## 4. Realization
