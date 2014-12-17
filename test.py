#U of T bookstore data fetch
from selenium import webdriver

url = "http://uoftbookstore.com/buy_courselisting.asp"

driver = webdriver.Firefox()
driver.get(url)

term = driver.find_element_by_id("fTerm")
for option in term.find_elements_by_tag_name('option'):
	if option.text == "ST GEORGE - 20149STG": option.click() 

dept = driver.find_element_by_id("fDept")
course = driver.find_element_by_id("fCourse")
section = driver.find_element_by_id("fSection")
for dept_option in dept.find_elements_by_tag_name('option'):
	print dept_option
	current_dept_text = dept_option.text
	dept_option.click()
	driver.implicitly_wait(0.2) 
	while "Loading..." in current_dept_text:
		print 1
		try: current_dept_text = dept_option.text
		except: break
	for course_option in course.find_elements_by_tag_name('option'): 
		current_course_text = course_option.text
		course_option.click()
		driver.implicitly_wait(0.2) 
		while "Loading..." in current_course_text:
			print 2
			try: current_course_text = course_option.text
			except: break
		for section_option in section.find_elements_by_tag_name('option'):
			try: current_section_text = section_option.text
			except: pass
			section_option.click()
			driver.implicitly_wait(0.2) 
			
# driver.quit()