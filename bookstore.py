from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

AIM = "MEDICAL"
URL = "http://uoftbookstore.com/buy_courselisting.asp"
LOADING = "Loading"

driver = webdriver.Firefox()
driver.get(URL)

term = driver.find_element_by_id("fTerm")
for option in term.find_elements_by_tag_name('option'):
	if AIM in option.text: option.click()

dept = driver.find_element_by_id("fDept")
course = driver.find_element_by_id("fCourse")
section = driver.find_element_by_id("fSection")
books = driver.find_element_by_id("course-bookdisplay")

def safe_click(cur_option):
	#driver.implicitly_wait(0.1)  
	cur_option.click()
	#driver.implicitly_wait(0.1)

def get_option_elements(section):
	#driver.implicitly_wait(0.1)
	cur_list = section.find_elements_by_tag_name('option')
	while len(cur_list)< 2:
		try:
			if LOADING not in cur_list[0].text:
				break
		except:
			pass
		cur_list = section.find_elements_by_tag_name('option')
	print len(cur_list)
	return cur_list
	
for dept_option in get_option_elements(dept):
	print "a"
	safe_click(dept_option)  
	for course_option in get_option_elements(course):
		print "b"
		safe_click(course_option)
		for section_option in get_option_elements(section):
			print "c"
			safe_click(section_option)
			driver.implicitly_wait(2)
			try:
				print driver.find_element_by_xpath('//div[@id="course-bookdisplay"]//span[@class="book-title"]').text;
				print driver.find_element_by_xpath('//div[@id="course-bookdisplay"]//td[@class="book-cover"]/a/img[@src]').text;
			except:
				pass
			


 
