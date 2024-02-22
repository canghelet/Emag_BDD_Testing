This is the Emag BDD Automation Framework project.

Site tested: emag.ro
Design pattern used: page object model
Methodology: behavior driven development

Libraries to install:
- pip install -U selenium
- pip install behave
- pip install behave-html-formatter
- pip install webdriver-manager

Run tests:
- behave -f html -o behave-report.html --tags=emag
- behave -f html -o behave-report.html --tags=search
- behave -f html -o behave-report.html --tags=login1
- behave -f html -o behave-report.html --tags=login2
