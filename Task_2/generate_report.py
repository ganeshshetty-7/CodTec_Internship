import pandas as pd
from fpdf import FPDF


df = pd.read_csv("employee_data.csv")


#Statistics
avg_tasks = df['Tasks Completed'].mean()
sum_tasks = df['Tasks Completed'].sum()
count_employees = df['Employee'].count()

avg_days = df['Days Present'].mean()
max_tasks = df['Tasks Completed'].max()
min_tasks = df['Tasks Completed'].min()

top_employee = df[df['Tasks Completed'] == max_tasks]['Employee'].values[0]

max_days = df['Days Present'].max()
min_days = df['Days Present'].min()
most_present = df[df['Days Present'] == max_days]['Employee'].tolist()
least_present = df[df['Days Present'] == min_days]['Employee'].tolist()

most_common_dept = df['Department'].mode()[0]
rating_counts = df['Performance Rating'].value_counts()
avg_tasks_by_dept = df.groupby('Department')['Tasks Completed'].mean()

# --------- PDF Report ---------
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="---EMPLOYEE PERFORMANCE REPORT---", ln=True, align='C')


pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Statistical Analysis:", ln=True)
pdf.set_font("Arial", size=11)

pdf.cell(200, 10, txt=f"Total Employees: {count_employees}", ln=True)
pdf.cell(200, 10, txt=f"Total Tasks Completed: {sum_tasks}", ln=True)
pdf.cell(200, 10, txt=f"Average Tasks Completed: {avg_tasks:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Average Days Present: {avg_days:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Top Performer: {top_employee} ({max_tasks} tasks)", ln=True)
pdf.cell(200, 10, txt=f"Most Days Present: {max_days} ({', '.join(most_present)})", ln=True)
pdf.cell(200, 10, txt=f"Least Days Present: {min_days} ({', '.join(least_present)})", ln=True)
pdf.cell(200, 10, txt=f"Most Common Department: {most_common_dept}", ln=True)



# Performance Rating Distribution
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Performance Rating Distribution:", ln=True)
pdf.set_font("Arial", size=11)
for rating, count in rating_counts.items():
    pdf.cell(200, 10, txt=f"- {rating}: {count}", ln=True)



# Average Tasks by Department
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Average Tasks Completed by Department:", ln=True)
pdf.set_font("Arial", size=11)
for dept, avg in avg_tasks_by_dept.items():
    pdf.cell(200, 10, txt=f"- {dept}: {avg:.2f} tasks", ln=True)
 

# Table Header
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, txt="Detailed Employee Data", ln=True, align='C')
pdf.ln(5)



pdf.set_font("Arial", 'B', 11)
headers = ["Employee", "Dept", "Days", "Tasks", "Rating"]
widths = [40, 30, 25, 30, 50]
for header, width in zip(headers, widths):
    pdf.cell(width, 10, header, border=1)
pdf.ln()

# Table Rows
pdf.set_font("Arial", size=10)
for _, row in df.iterrows():
    pdf.cell(40, 10, row["Employee"], border=1)
    pdf.cell(30, 10, row["Department"], border=1)
    pdf.cell(25, 10, str(row["Days Present"]), border=1)
    pdf.cell(30, 10, str(row["Tasks Completed"]), border=1)
    pdf.cell(50, 10, row["Performance Rating"], border=1)
    pdf.ln()

# Save PDF
pdf.output("employee_report.pdf")
print("✅ PDF report generated as 'employee_report.pdf'")
