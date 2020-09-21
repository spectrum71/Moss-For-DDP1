import mosspy

# sesuaikan dengan userid anda
userid = 000000000

m = mosspy.Moss(userid, "python")

# sesuaikan dengan penamaan berkas.
# jika tidak menggunakan template, silahkan block comment potongan kode ini
template_filename = "path/to/template_file/[insert filename].py"
m.addBaseFile(template_filename)

# sesuaikan dengan penamaan berkas
submission_patternname = "path/to/submission_file/submission/LabX_*.py"
m.addFilesByWildcard(pattern_name)

url = m.send()
print()

# akses hasil checker lewat URL ini
print ("Report URL: " + url)