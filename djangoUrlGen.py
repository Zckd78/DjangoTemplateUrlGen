# Importing OS to move around in the system and get file names
import os

# DTO - Data Transfer Object - Used to store data about the links we generate
class Link:
    fileName = ""
    urlFunc = ""
    urlPattern = ""
    fileType = ""

""" ////////!!!!!! FILL THESE FIELDS IN !!!!!!!///////// """

# Fill in your folder
os.chdir("C:\\Users\\Zenko\\Desktop\\Stuff\\Coding\\PythonProjects\\mysite\\index\\templates\\index\\js")
# Name of the django app, do not insert5
appName = "index"
# Once inside the app dir, this would be any additional folders
remPath = "js"
# This is the file extension that we want to import
fileExt = ["js"]

"""  //////// Below is the functional code - Run once above is filled in /////////   """

dir = os.listdir()
urlScaffolds = []
defScaffolds = []
srcScaffolds = []
urlPrefix = appName + "/" + remPath + "/"

for file in dir:

    link = Link()
    link.fileName = file
    pieces = str(file).replace('-','').split('.')

    funcName = ""
    for bit in pieces:
        for ext in fileExt:
            if(bit == ext):
                link.urlFunc = funcName
                link.urlPattern = urlPrefix + file
                link.fileType = ext

                if(bit == "js"):
                    srcScaffold = "<script src='" + link.urlPattern + "'> </script>"
                    srcScaffolds.append(srcScaffold)
                elif(bit == "css"):
                    srcScaffold = "<style rel='stylesheet' type='text/css' href='" + link.urlPattern + "'> </script>"
                    srcScaffolds.append(srcScaffold)

                break
        funcName += bit

    urlScaffold = "url(r'^" + link.urlPattern + "', views." + link.urlFunc +", name='"+ link.urlFunc +"'),"
    defScaffold = "def " + link.urlFunc + "(request): \n"
    defScaffold += "    return render(request, '"+ urlPrefix + link.fileName + "')"
    # This could be a Switch stub, but I don't know the Syntax at the moment of writing this in front of TapEx


    urlScaffolds.append(urlScaffold)
    defScaffolds.append(defScaffold)

# Print out the results, copy these into the files it mentions
print("\n")
print("<------- Add these to the app url.py file ------->")
for item in urlScaffolds:
    print(item)
print("\n")
print("<------- Add these to the app views.py file ------->")
for item in defScaffolds:
    print(item)
print("\n")

# HTML Files will not generate a src section of output.
srclen = len(srcScaffolds)
if(srclen > 0):
    print("<------- Add these to the your html file ------->")
    for item in srcScaffolds:
        print(item)
    print("\n")