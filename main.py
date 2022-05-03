import time
from selenium import webdriver
import Info
import pandas as pd

web = webdriver.Chrome()
web.get(Info.url)
time.sleep(3)

login = web.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()
time.sleep(3)

web.find_element_by_xpath("//*[@id='username']").send_keys(Info.email)
web.find_element_by_xpath("//*[@id='password']").send_keys(Info.password)
time.sleep(3)
web.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button").click()
time.sleep(3)

web.find_element_by_xpath("//*[@id='ember19']").click()
time.sleep(3)

web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(3)



jobs = web.find_elements_by_class_name("artdeco-entity-lockup__title")
time.sleep(3)

companies = web.find_elements_by_class_name("artdeco-entity-lockup__subtitle")
time.sleep(3)

company = []

for comp in companies:
    company.append(comp.text)

job = []

for jb in jobs:
    job.append(jb.text)


liste = pd.DataFrame(                        # Pandas kütüphanesi yardımıyla şirketleri ve işleri dataframe haline getiriyoruz.
    {
        "Şirket Adı:": pd.Series(company),
        "İş:": pd.Series(job)
    }
)

print(liste)




