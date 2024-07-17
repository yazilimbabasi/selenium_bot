from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Firefox tarayıcısını başlatma
driver = webdriver.Firefox()

# Web sitesine gitme
driver.get('https://marasfenlisesi.meb.k12.tr/icerikler/pusula-roket-takimimiz-calismalarina-son-hiz-devam-ediyor_15175149.html')

# Bekleme süresi ayarı
wait = WebDriverWait(driver, 10)
while True:
# Butonu bulma ve belirli bir süre bekleyerek tıklama
    try:
        for i in range(360):
            # Butonun görünür olmasını bekleyin ve sonra tıklayın
            button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'begen')))
            button.click()
            print(f"{i+1}. kez butona başarıyla tıklandı!")
            # Her tıklamadan sonra kısa bir bekleme süresi ekleyin
            time.sleep(0.5)
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Tarayıcıyı kapatma
driver.quit()
