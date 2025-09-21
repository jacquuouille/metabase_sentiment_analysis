# Metabase Project: Customer Sentiment Analysis Dashboard

### 📖 Overview
Providing a comprehensive view of reviews to uncover patterns in satisfaction, motivations and frustrations, with a focus on subjectivity to helps separate between factual and opinion-driven sentiment.

![Customer Experience Dashboard](screenshots/dash_cust_exp.png)

### 📁 Data Model

To download directly from [Kaggle](https://www.kaggle.com/datasets/thedevastator/booking-com-hotel-reviews/data) → `hotels_reviews.csv` 

| Column            | Type        | Description                          |
|------------------|------------|--------------------------------------|
| index             | integer    | Unique identifier for each review    |
| review_title      | text       | Title of the review                  |
| reviewed_at       | datetime   | Date when the review was written     |
| reviewed_by       | text       | Name of the reviewer                 |
| images            | list/url   | Images attached to the review        |
| crawled_at        | datetime   | Date when the review was crawled     |
| url               | url        | Link to the review                   |
| hotel_name        | text       | Name of the hotel                     |
| hotel_url         | url        | Link to the hotel                     |
| avg_rating        | float      | Average rating of the hotel          |
| nationality       | text       | Nationality of the reviewer          |
| rating            | integer    | Rating given by the reviewer         |
| review_text       | text       | Cleaned review text                  |
| raw_review_text   | text       | Original review text                  |
| tags              | list/text  | Tags or keywords from the review     |
| meta              | json/text  | Additional metadata                   |





### 🛠️ Technology Stack
- **Docker →** for running Metabase locally or on a server (open-source)
- **VS Code →** for writting Python scripts to connect to data sources
- **PostgreSQL →** for storing and manipulating data
- **Python →** for performing statistical analysis
- **Metabase →** for creating interactive dashboards and analyzing data
- **Github →** for hosting and sharing portfolio projects
