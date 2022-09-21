
# Ad-Upload-Automation

Auto generate a csv file that can be uploaded to the dash to create ads.

## FAQ

#### What do I need to do before generating the csv file?

This depends on the type of tag sheet you're using to buid the csv file. Below are the steps you need to take before generating the csv file depending on the generic file type.

Tag sheets with display tags: 
- Test tags to make sure creative is rendering and redirecting to client's site when clicked.
- Taking screenshots of creatives to use as backup creatives.
- Uploading backup creatives with a naming convention that includes the dimensions of the backup creatives to the dash.
Tag sheets with 1x1 tracking tags: 
- Test click trackers to make sure they are clicking out to client's site.
- If the trackers are for display placements make sure the dimensions of each placement are included in the Placement Name in the tag sheet, even if you add them yourself and remove them later. If the trackers are for video placements include the video duration in the Placmenet Name using one of the following options: 6s, 06s, 15s, 30s.

#### What values to I need to assign the three variables before running the program?

Variable: file_path
- For this variable you should use the global file path including the name of the tag sheet. Example: /Users/username/Downloads/sub-directory_where_file_is_located/file_name.extension
Variable: ad_domain
- This should be the ad domain of the site you are redirected to when testing the display tags or the click tags. Example: walmart.com
Variable: sheet_type
- There are six values to choose from, and it depends on the type of tag sheet you're using to gnerate the csv file. This depends on the vendor, if the tags are display tags or 1x1 tracking tags, if the tags are DV wrapped tags (for display only), and if the tags are for dipslay or video placements (for 1x1s only). The options are below and their use is self evident:
- 'dcm display tags'
- 'dcm dv display tags'
- 'sizmek display tags'
- 'sizmek dv display tags'
- 'dcm display tracking pixels'
- 'dcm video tracking pixels'

### When generating a csv file from a sheet with display tags what do I enter when prompted to enter creatives?

- If you're using backup creatives then simply enter all backup creatives, with each separated by a comma and a single space.
- If you're not using backup creatives then you should enter one creative for each dimension and update the csv file manually after it has been generated. REMEMBER: when you upload the csv file it will map the creative files in the sheet to the file names in the dash so they must be identical, including the file extension.

### When generating a csv file from a sheet with 1x1 tags why does the 'Creative Name' column is populated with the creative name as found in the 3rd party tag sheet? 

Because you're not currently able to enter the creatives as found in the dash the program uses the creative names found in the 'Creative Name' column in the tag sheet to make it easier to identify which creative names you should use when manually updating the csv file.

### When generating a csv file from a sheet with 1x1 tags why are the 'Ad Type', 'Ad Unit' and 'Ad Dimensions' columns empty?

These columns are empty when the dimensions of the ad (for display only) or the duration of the video (for video only) are not included in the Placement Name in the tag sheet. Currently the program looks in the Placement Name column for this information when generating a csv file from a sheet with 1x1 tags.

### I want to update the tag sheet to remove certain placements or modify the placement names before generating the csv file but I do not want these changes to be permanent. What can I do? 

Duplicate the tag sheet. Once you duplicate the tag sheet you can update the duplicate version as much as you like and then generate the csv file from the modified duplciate version.

### There are multiple tag sheets in the directory where the tag sheet I want to generate a csv file from is located. How can I identify the csv file once it's generated?

The csv file name will include the name of the tag sheet (including the file extension) followed by '_Ad_Upload.csv'. 
- Example: if you have a tag sheet named 'bees_knees-butter-pecan-pie.xls' then the csv file you generate will be named 'bees_knees-butter-pecan-pie.xls_Ad_Upload.csv'. 

### When I generate a new csv file where can I find it? 

All new csv files will appear in the same directory as the tag sheet you generated the csv file from. 
- It is recommended that for all campaigns you create a unique directory where you can store all files and assets. When the csv file is generated it will appear in this directory.

### Once I generate a csv file can I upload to the dash immediately? 

The short answer is yes. You can upload it immediately as long as there are no updates that you need to make to the file, such as adding the creative names in the case of a csv file generated from tag sheets with 1x1 tags. HOWEVER, it is highly recommended that you always open the csv file before uploading it to the dash in order to ensure that the information that populated is correct and any changes such as the remove of the GDPR macros has taken place.

### Why isn't there an option to generate a csv file from a sheet with Flashtalking tags? 

The problem is not related to the program, rather the issue is that when a csv file with Flashtalking tags is uploaded to the dash the tags are not correctly mapped to the Script Tag field and some parts of the tag populate in the fields under VAST Tracking Events. 



