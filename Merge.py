from PyPDF2 import PdfMerger, PdfReader, PdfWriter

merger = PdfMerger()

p1 = input("1st PDF : ")
p2 = input("2nd PDF : ")

for pdf in [p1, p2]:
    merger.append(pdf)

merger.write("Final.pdf")

reader = PdfReader("Final.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

auth = input("Who's the Author : ")
writer.add_metadata(
    {
        "/Author": auth,
    }
)

with open("Final.pdf", "wb") as f:
    writer.write(f)

merger.close()
