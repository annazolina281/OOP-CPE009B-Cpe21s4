from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter
from TextFileReaderWriter import TextFileReaderWriter 
                                                
# Test the default class
df = FileReaderWriter()
df.read()
df.write()

# Test the polymorphed objects
c = CSVFileReaderWriter()
c.read("sample.csv")
c.write(filepath="sample2.csv", data=["Hello, World"])

j = JSONFileReaderWriter()
j.read("sample.json")
j.write(data=['foo', {'bar': ('baz' ,None, 1, 0, )}], filepath="sample2.json")

tf = TextFileReaderWriter()
tf.read("TextFileReaderWriter.txt")
tf.write(filepath = "New File.txt", data = ("This is the data"))