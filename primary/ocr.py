import json
import shutil


def ocr(image_path):

  # Provide your username and license code
  UserName = 'thisiscool'
  LicenseCode=  'FB8729C2-2D75-44A4-8D20-7BBB6A48892A'
  try:
    import requests

  except ImportError:
    print("You need the requests library to be installed in order to use this sample.")
    print("Run 'pip install requests' to fix it.")
    exit()

  # Extract text with English language by default
  RequestUrl = "http://www.ocrwebservice.com/restservices/processDocument?gettext=true&outputformat=txt&language=english&newline=1&tobw=true"

  #Full path to uploaded document
  FilePath = image_path
  with open(FilePath, 'rb') as image_file:
      image_data = image_file.read()
  r = requests.post(RequestUrl, data=image_data, auth=(UserName,LicenseCode))

  if r.status_code == 401:
      #Please provide valid username and license code
      print("Unauthorized request")
      exit()

  # Decode Output response
  jobj = json.loads(r.content)


  ocrError = str(jobj["ErrorMessage"])
  download_url = str(jobj["OutputFileUrl"])


  if ocrError != '':
          #Error occurs during recognition
          print ("Recognition Error: " + ocrError)
          exit()

  # Processed pages 
  # print("Processed Pages:" + str(jobj["ProcessedPages"]))

  # Extracted text from first or single page
  # print("Extracted Text:" + str(jobj["OCRText"][0][0]))

  return str(jobj["OCRText"][0][0]), str(jobj["ProcessedPages"]), download_url, ocrError







