# Project:pyseltask3_Rahulshettywebpage
# Author:Vijaykumar Sambanni (798705)
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

start_time = time.time()
# Set up driver and access web page https://www.rahulshettyacademy.com/AutomationPractice/
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\hi\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Select radio button 2 and assert

truevalue = True

driver.find_element_by_xpath("//input[@value='radio2']").click()

try:
    assert truevalue == driver.find_element_by_xpath("//input[@value='radio2']").is_selected()
    print("Radio 2 button is selected")
except:
    print("Radio 2 button is not selected")

# Select Indonesia from suggestion drop down and assert ---------------------------------------------
countryelement = driver.find_element_by_xpath("//input[@id='autocomplete']")
countryelement.send_keys("In")
time.sleep(3)
values = driver.find_elements_by_xpath("//li/div[@class='ui-menu-item-wrapper']")
country_selected = "None"

for n in values:
    if n.text == "Indonesia":
        country_selected = n.text
        n.click()
        break
time.sleep(3)
print(country_selected)

try:
    assert country_selected == "Indonesia"
    print("Indonesia Selected")
except:
    print("Indonesia not selected")

# print(driver.execute_script('return document.getElementById("autocomplete").innerText'))

# Select option 2 from static option drop down and assert
dropdownelement = driver.find_element_by_xpath("//select[@id='dropdown-class-example']")
staticdropdown = Select(dropdownelement)
staticdropdown.select_by_visible_text('Option2')

selected_option = staticdropdown.first_selected_option
selectedvalue = selected_option.text

try:
    assert selectedvalue == "Option2"
    print("Option 2 is selected")
except:
    print("Option 2 is not selected")

# Select check box 1,3 and assert
checkbox1 = driver.find_element_by_xpath("//input[@id='checkBoxOption1']")
checkbox3 = driver.find_element_by_xpath("//input[@id='checkBoxOption3']")
checkbox1.click()
checkbox3.click()

try:
    assert truevalue == checkbox1.is_selected()
    assert truevalue == checkbox3.is_selected()
except:
    print("Checkbox 1 and 2 are not selected")
time.sleep(3)

# Click on open window button, and switch to new window (child window) and assert title.
# Then switch back to original window.
driver.find_element_by_xpath("//button[@id='openwindow']").click()
Parentwindow = driver.window_handles[0]
Childwindow = driver.window_handles[1]
driver.switch_to.window(Childwindow)
print(driver.title)
time.sleep(3)

try:
    assert driver.title == "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy"
    print("Control is @ChildWindow")
except:
    print("Control is @ParentWindow")

driver.switch_to.window(Parentwindow)
print(driver.title)

# Click on open tab button, and switch to new tab(child window) and assert title.
# Then switch back to original window.

driver.find_element_by_xpath("//a[@id='opentab']").click()
ParentTab = driver.window_handles[0]
ChildTab = driver.window_handles[2]

driver.switch_to.window(ChildTab)
print(driver.title)
time.sleep(3)

try:
    assert driver.title == "Rahul Shetty Academy"
    print("COntrol is @ ChildTab")
except:
    print("Control is @ ParentTab")

driver.switch_to.window(ParentTab)
print(driver.title)

# Enter your name in text box(under Switch To Alert Example)
# Click alert button and assert alert message should have your name in alert message.
# Then accept alert box.

driver.find_element_by_xpath("//input[@id='name']").send_keys("Vijaykumar")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='alertbtn']").click()
time.sleep(3)

alert = driver.switch_to.alert
alertmessage = alert.text
if (alertmessage.find("Vijaykumar") >= 0):
    print("Alert message has the name")
    alert.accept()
    print("Alert accepted")
else:
    print("Alert message don't have the name")
    raise NameError

# Enter your name in text box(under Switch To Alert Example)
# Click confirm button and assert alert message should have your name in alert message.
# Then cancel alert box

driver.find_element_by_xpath("//input[@id='name']").send_keys("Vijaykumar")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='confirmbtn']").click()
time.sleep(3)

alert = driver.switch_to.alert
alertmessage = alert.text
if (alertmessage.find("Vijaykumar") >= 0):
    print("Alert message has the name")
    alert.dismiss()
    print("Alert dismissed")
else:
    print("Alert message don't have the name")
    raise NameError

# Enter your name in text box under 'Element Displayed Example'.
# Click Hide button and assert the text box is not shown
# Click Show button and assert the text box is shown and assert text value with value that we entered.

textbox = driver.find_element_by_xpath("//input[@id='displayed-text']")
name = "Vijaykumar"
textbox.send_keys(name)
time.sleep(3)
driver.find_element_by_xpath("//input[@id='hide-textbox']").click()
time.sleep(3)

try:
    assert truevalue != textbox.is_displayed()
    print("Text box is hidden")
except:
    print("Text box is not hidden")

driver.find_element_by_xpath("//input[@id='show-textbox']").click()
time.sleep(3)

try:
    assert truevalue == textbox.is_displayed()
    print("Text box is not hidden")
    if textbox.text == name:
        print("Name is correct")
    else:
        print("Name is not correct")
        print("GLITCH")
except:
    print("Text box is hidden")

# Interrogate the web table and get the rows which has 'selenium' in it.
# Get the count of courses having ‘selenium’ as substring.

rowpointer = len(driver.find_elements_by_xpath('//table/tbody/tr'))
columnpointer = len(driver.find_elements_by_xpath('//table/tbody/tr[2]/td'))
wordcount = 0

for r in range(2, rowpointer, 1):
    for c in range(1, columnpointer, 1):
        substring = driver.find_element_by_xpath('//table/tbody/tr[' + str(r) + ']/td[' + str(c) + ']').text
        index = substring.find("Selenium")
        if index < 0:
            pass
        else:
            wordcount = wordcount + 1
print(wordcount)

# Mouse hover the 'Mouse hover' button get the all the options and log in console.
moveto = driver.find_element_by_xpath("//button[@id='mousehover']")

action = ActionChains(driver)
action.move_to_element(moveto).perform()

mousehovervalues = driver.find_elements_by_xpath("//div[@class='mouse-hover']/div/a")
for v in mousehovervalues:
    print(v.text)

# Get the total count of iframe/frame/frameset present in current page.
farmescount = len(driver.find_elements_by_xpath("//iframe"))
print("Frame count is " + str(farmescount))

# Switch to first iframe and get all list of urls in iframe and switch back to main window.
driver.switch_to.frame('iframe-name')

for u in driver.find_elements_by_xpath("//a"):
    print(u.get_attribute('href'))

driver.switch_to.default_content()
print(driver.title)

# Close the main windows and all child windows.
driver.close()
driver.quit()

# time taken for execution
print("Execution time -- %s seconds --" % (time.time() - start_time))
print('time in seconds{0:.2f}'.format((time.time() - start_time)))