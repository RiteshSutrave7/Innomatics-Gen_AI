# 4: Email Domain Usage Analysis
emails = [
"ravi@gmail.com",
"anita@yahoo.com",
"kiran@gmail.com",
"suresh@gmail.com",
"meena@yahoo.com"
]
# count occurances of each domain
domain_counts={}
for email in emails:
    domain=email.split('@')[1]
    domain_counts[domain]=domain_counts.get(domain,0)+1
# calculate and print  percentages   
total_emails=len(emails)
for domain,count in domain_counts.items():
    percentage=(count/total_emails)*100
    print(f"{domain}:{percentage:.0f}%")