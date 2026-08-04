-- ==========================================================
-- HR Analytics Database Setup
-- ==========================================================

-- Drop table if it already exists
DROP TABLE IF EXISTS hr_data;

-- Create table
CREATE TABLE hr_data (

    age INT,
    attrition VARCHAR(10),
    business_travel VARCHAR(50),
    daily_rate INT,
    department VARCHAR(50),
    distance_from_home INT,
    education INT,
    education_field VARCHAR(50),
    environment_satisfaction INT,
    gender VARCHAR(20),
    hourly_rate INT,
    job_involvement INT,
    job_level INT,
    job_role VARCHAR(100),
    job_satisfaction INT,
    marital_status VARCHAR(30),
    monthly_income INT,
    monthly_rate INT,
    num_companies_worked INT,
    over_time VARCHAR(10),
    percent_salary_hike INT,
    performance_rating INT,
    relationship_satisfaction INT,
    stock_option_level INT,
    total_working_years INT,
    training_times_last_year INT,
    work_life_balance INT,
    years_at_company INT,
    years_in_current_role INT,
    years_since_last_promotion INT,
    years_with_curr_manager INT,
    attrition_flag INT,
    over_time_flag INT
);
