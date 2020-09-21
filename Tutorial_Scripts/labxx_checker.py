import mosspy

# sesuaikan dengan userid anda
userid = 000000000

m = mosspy.Moss(userid, "python")

# sesuaikan dengan penamaan berkas. 
# jika tidak menggunakan template, silahkan block comment potongan kode ini
# template_filename = 'template_labxx/TemplateXX.py'
# m.addBaseFile(template_filename)

# sesuaikan dengan penamaan berkas
submission_patternname = 'submission_labxx/LabXX_*.py'
m.addFilesByWildcard(submission_patternname)

url = m.send()
print()

# akses hasil checker lewat URL ini
print ("Report URL: " + url)