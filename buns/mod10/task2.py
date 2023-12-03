# Импортировать модуль re (регулярные выражения) и модуль requests.
import re
import requests

# Получить содержимое веб-страницы:
url = 'http://www.columbia.edu/~fdc/sample.html' 
response = requests.get(url)                     
content = response.text                          

# Извлекать подзаголовки с помощью регулярных выражений в содержимом веб-страницы и сохранить их в список subheadings.
subheadings = re.findall(r'<h3 id=".*?">(.*?)</h3>', content)

# Вывести список подзаголовков на экран
print(subheadings)




"""
вывод:

['CONTENTS', '1. Creating a Web Page', '2. HTML Syntax', '3. Special Characters', '4. Converting Plain Text to HTML', '5. Effects', '6. Lists', '7. Links', '8. Tables', '9. Viewing Your Web Page', '10. Installing Your Web Page on the Internet', '11. Where to go from here', '12. Postscript: Cell Phones']

Process finished with exit code 0


"""
