# Snippet of code to convert .pbm (portable bitmap format) to .bin files by stripping out headers

file_name=input("Filename (no extension):")
print("Converting ",file_name,".pbm to ",file_name,".bin")

file=open(file_name+".pbm","rb")
file.readline()
file.readline()
file.readline()
data = bytearray(file.read())
file.close()


file2=open(file_name+".bin","wb")
file2.write(data)
file2.close()
print("Done")



