import PyPDF2

def parser(file):
  charts = open(file, 'rb')
  parsed = PyPDF2.PdfFileReader(charts)
  chart = parsed.getPage(0)

  employees = []
  times = []
  numbers = '1234567890'
  txt = chart.extractText()
  lines = txt.splitlines()

  for line in lines:
    if "Total" in line:
      break
    if len(line) > 3:
      if line == "Raquel ":
        employees.append("Raquel Sutherland")
        continue
      if line == "Sutherland":
        continue
      if line[0] in numbers:
        times.append(line)
      else:
        employees.append(line)
  return(employees[4:], times)
