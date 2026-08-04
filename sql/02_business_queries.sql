-- ==========================================================
-- HR Analytics SQL Business Queries
-- Table Name: hr_data
-- ==========================================================

-- 1. Total Number of Employees
SELECT COUNT(*) AS total_employees
FROM hr_data;

-------------------------------------------------------------

-- 2. Overall Attrition Rate
SELECT
    ROUND(AVG(attrition_flag) * 100, 2) AS attrition_rate_percent
FROM hr_data;

-------------------------------------------------------------

-- 3. Total Employees Left
SELECT
    SUM(attrition_flag) AS employees_left
FROM hr_data;

-------------------------------------------------------------

-- 4. Employee Count by Department
SELECT
    department,
    COUNT(*) AS employee_count
FROM hr_data
GROUP BY department
ORDER BY employee_count DESC;

-------------------------------------------------------------

-- 5. Attrition Rate by Department
SELECT
    department,
    COUNT(*) AS total_employees,
    SUM(attrition_flag) AS attrition_count,
    ROUND(AVG(attrition_flag) * 100, 2) AS attrition_rate
FROM hr_data
GROUP BY department
ORDER BY attrition_rate DESC;

-------------------------------------------------------------

-- 6. Employee Count by Job Role
SELECT
    job_role,
    COUNT(*) AS employee_count
FROM hr_data
GROUP BY job_role
ORDER BY employee_count DESC;

-------------------------------------------------------------

-- 7. Attrition Rate by Job Role
SELECT
    job_role,
    COUNT(*) AS total_employees,
    SUM(attrition_flag) AS attrition_count,
    ROUND(AVG(attrition_flag) * 100, 2) AS attrition_rate
FROM hr_data
GROUP BY job_role
ORDER BY attrition_rate DESC;

-------------------------------------------------------------

-- 8. Average Monthly Income by Department
SELECT
    department,
    ROUND(AVG(monthly_income),2) AS avg_salary
FROM hr_data
GROUP BY department
ORDER BY avg_salary DESC;

-------------------------------------------------------------

-- 9. Average Monthly Income by Job Role
SELECT
    job_role,
    ROUND(AVG(monthly_income),2) AS avg_salary
FROM hr_data
GROUP BY job_role
ORDER BY avg_salary DESC;

-------------------------------------------------------------

-- 10. Overtime vs Attrition
SELECT
    over_time,
    COUNT(*) AS employees,
    SUM(attrition_flag) AS attrition_count,
    ROUND(AVG(attrition_flag)*100,2) AS attrition_rate
FROM hr_data
GROUP BY over_time;

-------------------------------------------------------------

-- 11. Gender Distribution
SELECT
    gender,
    COUNT(*) AS employee_count
FROM hr_data
GROUP BY gender;

-------------------------------------------------------------

-- 12. Attrition by Gender
SELECT
    gender,
    COUNT(*) AS employees,
    SUM(attrition_flag) AS attrition_count,
    ROUND(AVG(attrition_flag)*100,2) AS attrition_rate
FROM hr_data
GROUP BY gender;

-------------------------------------------------------------

-- 13. Marital Status Distribution
SELECT
    marital_status,
    COUNT(*) AS employees
FROM hr_data
GROUP BY marital_status
ORDER BY employees DESC;

-------------------------------------------------------------

-- 14. Attrition by Marital Status
SELECT
    marital_status,
    COUNT(*) AS employees,
    SUM(attrition_flag) AS attrition_count,
    ROUND(AVG(attrition_flag)*100,2) AS attrition_rate
FROM hr_data
GROUP BY marital_status
ORDER BY attrition_rate DESC;

-------------------------------------------------------------

-- 15. Average Age by Department
SELECT
    department,
    ROUND(AVG(age),1) AS average_age
FROM hr_data
GROUP BY department
ORDER BY average_age DESC;

-------------------------------------------------------------

-- 16. Average Years at Company by Department
SELECT
    department,
    ROUND(AVG(years_at_company),2) AS avg_years
FROM hr_data
GROUP BY department
ORDER BY avg_years DESC;

-------------------------------------------------------------

-- 17. Business Travel vs Attrition
SELECT
    business_travel,
    COUNT(*) AS employees,
    SUM(attrition_flag) AS attrition_count,
    ROUND(AVG(attrition_flag)*100,2) AS attrition_rate
FROM hr_data
GROUP BY business_travel
ORDER BY attrition_rate DESC;

-------------------------------------------------------------

-- 18. Job Satisfaction vs Attrition
SELECT
    job_satisfaction,
    COUNT(*) AS employees,
    ROUND(AVG(attrition_flag)*100,2) AS attrition_rate
FROM hr_data
GROUP BY job_satisfaction
ORDER BY job_satisfaction;

-------------------------------------------------------------

-- 19. Environment Satisfaction vs Attrition
SELECT
    environment_satisfaction,
    COUNT(*) AS employees,
    ROUND(AVG(attrition_flag)*100,2) AS attrition_rate
FROM hr_data
GROUP BY environment_satisfaction
ORDER BY environment_satisfaction;

-------------------------------------------------------------

-- 20. Work Life Balance vs Attrition
SELECT
    work_life_balance,
    COUNT(*) AS employees,
    ROUND(AVG(attrition_flag)*100,2) AS attrition_rate
FROM hr_data
GROUP BY work_life_balance
ORDER BY work_life_balance;

-------------------------------------------------------------

-- 21. Top 10 Highest Paid Employees
SELECT
    age,
    gender,
    department,
    job_role,
    monthly_income
FROM hr_data
ORDER BY monthly_income DESC
LIMIT 10;

-------------------------------------------------------------

-- 22. Average Salary by Education Field
SELECT
    education_field,
    ROUND(AVG(monthly_income),2) AS avg_salary
FROM hr_data
GROUP BY education_field
ORDER BY avg_salary DESC;

-------------------------------------------------------------

-- 23. Attrition by Education Field
SELECT
    education_field,
    COUNT(*) AS employees,
    ROUND(AVG(attrition_flag)*100,2) AS attrition_rate
FROM hr_data
GROUP BY education_field
ORDER BY attrition_rate DESC;

-------------------------------------------------------------

-- 24. Department-wise Salary Statistics
SELECT
    department,
    MIN(monthly_income) AS minimum_salary,
    MAX(monthly_income) AS maximum_salary,
    ROUND(AVG(monthly_income),2) AS average_salary
FROM hr_data
GROUP BY department;

-------------------------------------------------------------

-- 25. HR Summary View
CREATE OR REPLACE VIEW hr_summary AS
SELECT
    department,
    COUNT(*) AS total_employees,
    SUM(attrition_flag) AS attrition_count,
    ROUND(AVG(attrition_flag)*100,2) AS attrition_rate,
    ROUND(AVG(monthly_income),2) AS average_salary,
    ROUND(AVG(job_satisfaction),2) AS avg_job_satisfaction,
    ROUND(AVG(work_life_balance),2) AS avg_work_life_balance
FROM hr_data
GROUP BY department;

-- View Result
SELECT *
FROM hr_summary;