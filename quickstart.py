from ganalytics import client
import os

# set the environment variables
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secrets/google-analytics-key.json'
os.environ['GA_PROPERTY_ID'] = '450165182'


client = client.ReportClient()

# get the report
report = client.pull_report_snapshot(report_name='traffic_overview',
                            date_range={
                                'start_date': '2024-07-01',
                                'end_date': '2024-07-31'
                            })

# convert report to table format
table = client.convert_report(report)

print(table)