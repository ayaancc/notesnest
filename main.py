from readpdf import readpdf
import openai


filepath = input("Enter the file path: ")
text = readpdf(filepath)
print(text)
