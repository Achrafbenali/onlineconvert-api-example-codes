
#
# This file is released under the MIT License.
#
# This is an basic example of "API of www.online-convert.com", how to use in your application/website to convert
# your file to your desire file format.
#
# Link:: http://api.online-convert.com this file is available here to download.
#

__date__ ="$Sep 4, 2014 12:36:41 PM$"

import imp

ocModule = imp.load_source('OnlineConvert', 'OnlineConvert.py')

oc=ocModule.OnlineConvert("ENTER YOUR APIKEY HERE", True, "convert-to-png");


print "Inserting job in server...\n\n";
print oc.convert("convert-to-jpg",ocModule.OnlineConvert.SOURCE_TYPE_FILE_PATH,"./spjobs.jpg","spjobs.png");
print "\n\nJob Inserted in server...\n\n\n\n";

print "Getting inserted job status on server...\n\n";
print oc.getProgress();
print "\n\nStatus of inserted job on server is above...\n\n\n\n";

print "===================================================\n";
print "HASH :-"+ oc.hash;
print "Download URL  :- "+ oc.downloadUrl;
print "===================================================\n\n";


print "\n\nNow deleting the file  from server...\n\n";
print oc.deleteFile();
print "The file has been deleted from server...\n\n\n\n";
