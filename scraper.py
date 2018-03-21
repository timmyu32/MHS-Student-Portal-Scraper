from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import functools





options = webdriver.ChromeOptions()

options.add_argument("-headless")
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.mms669.org/MMSGB45/default.aspx?ReturnUrl=%2fMMSGB45%2fstudent')
uname = driver.find_element_by_name('LoginControl1$txtUsername')
password = driver.find_element_by_name('LoginControl1$txtPassword')
login_btn = driver.find_element_by_name('LoginControl1$btnLogin')

q = input('Are you Tim U? [y/n]')
if q.startswith('y'):
    uname.send_keys('Tuzoegbu')
    password.send_keys('Cheeze10')
    login_btn.click()
else:
    q2 = input('Student Portal username...')
    q3 = input('Student Portal passworrd...')
    uname.send_keys(q2)
    password.send_keys(q3)
    login_btn.click()


timeout = 3
WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='rgMasterTable rgClipCells']")))

class_names1 = driver.find_elements_by_xpath("//tr[@class='rgRow']")
evens = [x.text for x in class_names1]

class_names2 = driver.find_elements_by_xpath("//tr[@class='rgAltRow']")
odds = [x.text for x in class_names2]

all_class_codes = driver.find_elements_by_xpath("//td[@style='background-color:White;width:95px;']")
class_codes = [x.text for x in all_class_codes]

denominator = []

try:
    class1 = evens[0]
    class1_g = class1.split(",")
    class1_grade = float(class1_g[1].split(')')[0].split('(')[1]) 
    denominator.append(class1_grade)
    data_file = open("C:\\Users\\Tim\\PP\\one.txt", "a")
    data_file.write(str(class1_grade) +',')    
    data_file.close()    
except:
   pass
try:
    class2 = odds[0]
    class2_g = class2.split(",")
    class2_grade = float(class2_g[1].split(')')[0].split('(')[1])
    denominator.append(class2_grade)
    data_file = open("C:\\Users\\Tim\\PP\\two.txt", "a")
    data_file.write(str(class2_grade) +',')
    data_file.close()          
except:
    pass
try:
    class3 = evens[1]
    class3_g = class3.split(",")
    class3_grade = float(class3_g[1].split(')')[0].split('(')[1])    
    denominator.append(class3_grade) 
    data_file = open("C:\\Users\\Tim\\PP\\three.txt", "a")
    data_file.write(str(class3_grade) +',')
    data_file.close()  
except:
    pass
try:
    class4 = odds[1]
    class4_g = class4.split(",")
    class4_grade = float(class4_g[1].split(')')[0].split('(')[1])    
    denominator.append(class4_grade) 
    data_file = open("C:\\Users\\Tim\\PP\\four.txt", "a")
    data_file.write(str(class4_grade) +',')
    data_file.close()  
except:
    pass
try:
    class5 = evens[2]
    class5_g = class5.split(",")
    class5_grade = float(class5_g[1].split(')')[0].split('(')[1])    
    denominator.append(class5_grade)  
    data_file = open("C:\\Users\\Tim\\PP\\five.txt", "a")
    data_file.write(str(class5_grade) +',')
    data_file.close() 
except:
    pass
try:
    class6 = odds[2]
    class6_g = class6.split(",")
    class6_grade = float(class6_g[1].split(')')[0].split('(')[1])    
    denominator.append(class6_grade)  
    data_file = open("C:\\Users\\Tim\\PP\\six.txt", "a")
    data_file.write(str(class6_grade) +',')
    data_file.close() 
except:
    pass
try:
    class7 = evens[3]
    class7_g = class7.split(",")
    class7_grade = float(class7_g[1].split(')')[0].split('(')[1])    
    denominator.append(class7_grade)  
    data_file = open("C:\\Users\\Tim\\PP\\seven.txt", "a")
    data_file.write(str(class7_grade) +',')
    data_file.close() 
except:
    pass
try:
    class8 = odds[3]
    class8_g = class8.split(",")
    class8_grade = float(class8_g[1].split(')')[0].split('(')[1])   
    denominator.append(class8_grade)  
except:
    pass
try:
    class9 = evens[4]
    class9_g = class9.split(",")
    class9_grade = float(class9_g[1].split(')')[0].split('(')[1])    
    denominator.append(class9_grade)  
except:
    pass
try:
    class10 = odds[4]
    class10_g = class10.split(",")
    class10_grade = float(class10_g[1].split(')')[0].split('(')[1])  
    denominator.append(class10_grade)  
except:
    pass








try:
    class1_code = class_codes[0]
    class1_name = class1.split(class1_code)[0]
except:
    pass
try:
    class2_code = class_codes[1]
    class2_name = class2.split(class2_code)[0]
except:
    pass
try:
    class3_code = class_codes[2]
    class3_name = class3.split(class3_code)[0]
except:
    pass
try:
    class4_code = class_codes[3]
    class4_name = class4.split(class4_code)[0]
except:
    pass
try:
    class5_code = class_codes[4]
    class5_name = class5.split(class5_code)[0]
except:
    pass
try:
    class6_code = class_codes[5]
    class6_name = class6.split(class6_code)[0]
except:
    pass
try:
    class7_code = class_codes[6]
    class7_name = class7.split(class7_code)[0]
except:
    pass
try:
    class8_code = class_codes[7]
    class8_name = class8.split(class8_code)[0]
except:
    pass
try:
    class9_code = class_code[8]
    class9_name = class9.split(class9_code)[0]
except:
    pass
try:
    class10_code = class_codes[9]
    class10_name = class10.split(class10_code)[0]
except:
    pass

try:        
    d = len(denominator)
    n = functools.reduce(lambda x,y: x+y, denominator)
except:
    pass

try:
    average = round(n/d, 2)
except:
    pass


data_1 = open("C:\\Users\\Tim\\PP\\one.txt", "r")
data11 = float(data_1.read().split(',')[-3])
data_1.close()

data_2 = open("C:\\Users\\Tim\\PP\\two.txt", "r")
data22 = float(data_2.read().split(',')[-3])
data_2.close()

data_3 = open("C:\\Users\\Tim\\PP\\three.txt", "r")
data33 = float(data_3.read().split(',')[-3])
data_3.close()

data_4 = open("C:\\Users\\Tim\\PP\\four.txt", "r")
data44 = float(data_4.read().split(',')[-3])
data_4.close()

data_5 = open("C:\\Users\\Tim\\PP\\five.txt", "r")
data55 = float(data_5.read().split(',')[-3])
data_5.close()

data_6 = open("C:\\Users\\Tim\\PP\\six.txt", "r")
data66 = float(data_6.read().split(',')[-3])
data_6.close()

data_7 = open("C:\\Users\\Tim\\PP\\seven.txt", "r")
data77 = float(data_7.read().split(',')[-3])
data_7.close()

data_file = open("C:\\Users\\Tim\\PP\\avg.txt", "a")
data_file.write(str(average))
data_file.close()
avg_data = open("C:\\Users\\Tim\\PP\\avg.txt", "r")
avg_data1 = float(avg_data.read().split(',')[-3])
avg_data.close()


def good_bad(last_grade, current_grade):
    if last_grade == current_grade:
        print('+0')
    elif current_grade > last_grade:
        print('+', str(current_grade - last_grade))
    elif current_grade < last_grade:
        print('-', str(last_grade - current_grade))



space = '       '
print(space)
print(class1_name, space,'(', round(class1_grade, 0), ')', class1_grade)
good_bad(data11, class1_grade)
print(class2_name, space,'(', round(class2_grade, 0), ')', class2_grade)
good_bad(data22, class2_grade)
print(class3_name, space,'(', round(class3_grade, 0), ')', class3_grade)
good_bad(data33, class3_grade)
print(class4_name, space,'(', round(class4_grade, 0), ')', class4_grade)
good_bad(data44, class4_grade)
print(class5_name, space,'(', round(class5_grade, 0), ')', class5_grade)
good_bad(data55, class5_grade)
print(class6_name, space,'(', round(class6_grade, 0), ')', class6_grade)
good_bad(data66, class6_grade)
print(class7_name, space,'(', round(class7_grade, 0), ')', class7_grade)
good_bad(data77, class7_grade)
try:
    print(class8_name, space, class8_grade,)
except:
    pass
try:
    print(class9_name, space, class9_grade)
except:
    pass
try:
    print(class10_name, space, class10_grade)
except:
    pass
print(space)
print('Average =', space, '(', round(average, 0), ')', average)
good_bad(avg_data1, average)

driver.close()
