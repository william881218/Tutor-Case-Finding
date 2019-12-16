## Tutor Case Finding Tool

### Usage
It's a tool to select tutor cases with ideal age, time, location...etc. from http://teaching.com.tw/member/case-list.php.
(Because this website doesn't support selection.)


### How to use
```./tutor_finding_tool.py [-arguments]```
Please make sure you have your python3 installed.
arguments:

    -h, --help: Show this tutorial.
	-i, --id=: Find the cases with specified case ids.
	-a, --age=: Find the cases with specified students ages.
	-c, --city=: Find the case at specified cities.
	-l, --location=: Find the city at specified location.
	-s, --subject=: Find the case with specified subjects.
	-t, --time=: Find the case with specified time. (morning, afternoon and night)
	-u, --url=: Assign specified website.
	-d, --day=: Find the case with specified day.
	-f, --frequent: Find the case in specified frequency.
