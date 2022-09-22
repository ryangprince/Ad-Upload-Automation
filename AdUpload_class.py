import pandas as pd
import csv


class AdUpload:
    
    ad_type_dict = {
        'Display': ['300px;height:250px', 'width:320px;height:50px', 'width:300px;height:50px','width:728px;height:90px',
        'w=300&h=250', 'w=320&h=50', 'w=300&h=50', 'w=728&h=90', '300x250', '320x50', '300x50', '728x90', '300X250', '320X50', '300X50', '728X90'],
        'Rich Media': ['width:320px;height:480px', 'width:480px;height:320px', 'w=320&h=480', 'w=480&h=320', '320x480', '480x320', '320X480', '480X320'],
        'Video': ['6s', '06s', '15s', '30s']
    }
    
    ad_unit_dict = {
        'Medium': ['300px;height:250px', 'w=300&h=250', '300x250', '300X250'],
        'Banner': ['width:320px;height:50px', 'w=320&h=50', '320x50', '320X50'],
        'Smaller Banner': ['width:300px;height:50px', 'w=300&h=50', '300x50', '300X50'],
        'Leaderboard': ['width:728px;height:90px', 'w=728&h=90', '728x90', '728X90'],
        'Vertical Interstitial': ['width:320px;height:480px', 'w=320&h=480', '320x480', '320X480'],
        'Horizontal Interstitial': ['width:480px;height:320px', 'w=480&h=320', '480x320', '480X320'],
        'Pre-Roll 6 Seconds': ['6s', '06s'],
        'Pre-Roll 15 Seconds': ['15s'],
        'Pre-Roll 30 Seconds': ['30s']
    }

    ad_dimensions_dict = {
        '300x250': ['300px;height:250px', 'w=300&h=250', '300x250', '300X250'],
        '320x50': ['width:320px;height:50px', 'w=320&h=50', '320x50', '320X50'],
        '300x50': ['width:300px;height:50px', 'w=300&h=50', '300x50', '300X50'],
        '728x90': ['width:728px;height:90px', 'w=728&h=90', '728x90', '728X90'],
        '320x480': ['width:320px;height:480px', 'w=320&h=480', '320x480', '320X480'],
        '480x320': ['width:480px;height:320px', 'w=480&h=320', '480x320', '480X320']
    }

    header_names = ['Ad Name', 'Ad Type', 'Ad Unit', 'Ad Dimension', 'Creative Name', 'Ad Serving', 'Click Tracker URLs', 'Impression Tracker URLs', 'Ad Domains', 'Script Type', 'Script Tag', 'Append HTML', 'Vast Tracking Events Started', 'Vast Tracking Events First Quartile', 'Vast Tracking Events Midpoint', 'Vast Tracking Events Third Quartile', 'Vast Tracking Events Complete', 'Third Party IDs']

    def __init__(self, file_path, ad_domain, sheet_type):
        self.file_path = file_path
        self.df = None
        self.dict_list = None  #self.df.to_dict('records')
        self.sheet_type = sheet_type
        self.csv_dict = []
        self.ad_domain = ad_domain
        self.tag_type = None
        self.ad_name = None
        self.creative_name = None
        self.ad_serving = None
        self.click_tracker_urls = None
        self.impression_tracker_urls = None
        self.script_type = None
        self.script_tag = None
        self.third_party_ids = None
        self.dict_key = None
        
        # takes user inputted sheet type to identify the field program should look at to determine ad type, ad unit, and ad dimensions 
        if self.sheet_type == 'dcm display tags':
            self.df = pd.read_excel(self.file_path, skiprows=12)
            self.dict_key = 'Script Tag'
        elif self.sheet_type == 'dcm dv display tags':
            self.df = pd.read_excel(self.file_path, skiprows=17)
            self.dict_key = 'Script Tag'
        elif self.sheet_type == 'sizmek display tags':
            self.df = pd.read_excel(self.file_path, skiprows=17)
            self.dict_key = 'Script Tag'
        elif self.sheet_type == 'sizmek dv display tags':
            self.df = pd.read_excel(self.file_path, skiprows=17)
            self.dict_key = 'Script Tag'      
        elif self.sheet_type == 'dcm display tracking pixels':
            self.df = pd.read_excel(self.file_path, skiprows=10)
            self.dict_key = 'Ad Name'
        elif self.sheet_type == 'dcm video tracking pixels':
            self.df = pd.read_excel(self.file_path, skiprows=10)
            self.dict_key = 'Ad Name'


        # creates dictionary with column headers as keys and stores in dict_list
        self.dict_list = self.df.to_dict('records')
        # print(self.dict_list)

        # set fields where data will be same for every placement by confirming tag sheet type using column headers
        # unique to each type of tag sheet
        for dict in self.dict_list:

            if 'JavaScript Tag' in dict:
                self.tag_type = 'standard DCM display tags'
                self.ad_name = 'Placement Name'
                self.ad_serving = 'DCM'
                self.script_type = 'dcm-ins-2'
                self.script_tag = 'JavaScript Tag'
                self.third_party_ids = 'Placement ID'
                break

            elif 'Blocking Javascript Tag' in dict:
                self.tag_type = 'DV wrapped DCM display tags'
                self.ad_name = 'Placement Name'
                self.ad_serving = 'DCM-DV'
                self.script_type = 'dcm-ins-2'
                self.script_tag = 'Blocking Javascript Tag'
                self.third_party_ids = 'Placement ID'
                break

            elif 'Script | SECURED' in dict:
                self.tag_type = 'standard Sizmek display tags'
                self.ad_name = 'PLACEMENT NAME'
                self.ad_serving = 'Sizmek'
                self.script_type = 'sizmek_default'
                self.script_tag = 'Script | SECURED'
                self.third_party_ids = 'PLACEMENT ID'
                break

            elif 'Display Blocking Script | SECURED' in dict:
                self.tag_type = 'DV wrapped Sizmek display tags'
                self.ad_name = 'Placement Name'
                self.ad_serving = 'Sizmek'
                self.script_type = 'sizmek_default'
                self.script_tag = 'Display Blocking Script | SECURED'
                self.third_party_ids = 'Placement ID'
                break

            elif 'Impression Tag (image)' in dict:
                self.tag_type = 'standard DCM tracking tags'
                self.ad_name = 'Placement Name'
                self.creative_name = 'Creative Name'
                self.ad_serving = 'Cluep'
                self.click_tracker_urls = 'Click Tag'
                self.impression_tracker_urls = 'Impression Tag (image)'
                self.script_tag = 'Display Blocking Script | SECURED'
                self.third_party_ids = 'Placement ID'
                break

        # creates array of dictionaries from dict_list, populating specific fields with data that is the same for every
        # placement using column headers that are unique to each type of tag sheet
        for dict in self.dict_list:
            if 'JavaScript Tag' in dict or 'Blocking Javascript Tag' in dict or 'Script | SECURED' in dict or 'Display Blocking Script | SECURED' in dict:
                self.csv_dict.append({
                    'Ad Name': dict[self.ad_name],
                    'Ad Type': '',
                    'Ad Unit': '',
                    'Ad Dimension': '',
                    'Creative Name': '',
                    'Ad Serving': self.ad_serving,
                    'Ad Domains': self.ad_domain,
                    'Script Type': self.script_type,
                    'Script Tag': dict[self.script_tag],
                    'Third Party IDs': dict[self.third_party_ids]
                    })

            elif 'Impression Tag (image)' in dict:
                self.csv_dict.append({
                    'Ad Name': dict[self.ad_name],
                    'Ad Type': '',
                    'Ad Unit': '',
                    'Ad Dimension': '',
                    'Creative Name': dict[self.creative_name],
                    'Ad Serving': 'Cluep',
                    'Click Tracker URLs': dict[self.click_tracker_urls],
                    'Impression Tracker URLs': dict[self.impression_tracker_urls],
                    'Ad Domains': self.ad_domain,
                    'Script Type': '',
                    'Script Tag': '',
                    'Append HTML': '',
                    'Third Party IDs': dict[self.third_party_ids]
                    })

    # removes GDPR macro from display tags
    def remove_gdpr_macro_dcm_js_tag(self):
        for dict in self.csv_dict:

            if """    data-dcm-gdpr-applies='gdpr=${GDPR}'
    data-dcm-gdpr-consent='gdpr_consent=${GDPR_CONSENT_755}'
    data-dcm-addtl-consent='addtl_consent=${ADDTL_CONSENT}'""" in dict['Script Tag']:
                tag_minus_gdpr = dict['Script Tag'].replace("""    data-dcm-gdpr-applies='gdpr=${GDPR}'
    data-dcm-gdpr-consent='gdpr_consent=${GDPR_CONSENT_755}'
    data-dcm-addtl-consent='addtl_consent=${ADDTL_CONSENT}'""", "")
                dict['Script Tag'] = tag_minus_gdpr

    # moves IAS code that comes with some 1x1 trackers to 'Append HTML' field if found
    def move_ias_trackers(self):
        for row in self.csv_dict:
            
            if '<SCRIPT TYPE="application/javascript" SRC="https://pixel.adsafeprotected.com' in row['Impression Tracker URLs']:
                tag_minus_ias = row['Impression Tracker URLs'].replace('<SCRIPT TYPE="application/javascript" SRC="https://pixel.adsafeprotected.com', '!<SCRIPT TYPE="application/javascript" SRC="https://pixel.adsafeprotected.com')
                list_tags = tag_minus_ias.split('!')
                row['Impression Tracker URLs'] = list_tags[0]
                row['Append HTML'] = list_tags[1]

    # removes GDPR macro from impression trackers
    def remove_gdpr_macro_dcm_imp_tag(self):
        for row in self.csv_dict:

            if ";gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755}" in row['Impression Tracker URLs']:
                tag_minus_gdpr = row['Impression Tracker URLs'].replace(";gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755}", "")
                row['Impression Tracker URLs'] = tag_minus_gdpr

    # removes the img tag wrapper from impression trackers
    def remove_img_wrapper_dcm_imp_tag(self):
        for row in self.csv_dict:
            
            if '<IMG SRC="' in row['Impression Tracker URLs']:
                tag_minus_start_img_wrapper = row['Impression Tracker URLs'].replace('<IMG SRC="', '')
                row['Impression Tracker URLs'] = tag_minus_start_img_wrapper

            if '" BORDER="0" HEIGHT="1" WIDTH="1" ALT="Advertisement">' in row['Impression Tracker URLs']:
                tag_minus_end_img_wrapper = row['Impression Tracker URLs'].replace('" BORDER="0" HEIGHT="1" WIDTH="1" ALT="Advertisement">', '')
                row['Impression Tracker URLs'] = tag_minus_end_img_wrapper

     # set 'Ad Type' based on dimension in 'Script Tag'
    def assign_ad_type(self):
        for ad_type in self.ad_type_dict:
            for dimensions in self.ad_type_dict[ad_type]:
                for row in self.csv_dict:
                    if dimensions in row[self.dict_key]:
                        row['Ad Type'] = ad_type

    # set 'Ad Unit' based dimension in 'Script Tag'
    def assign_ad_unit(self):
        for ad_unit in self.ad_unit_dict:
            for dimensions in self.ad_unit_dict[ad_unit]:
                for row in self.csv_dict:
                    if dimensions in row[self.dict_key]:
                        row['Ad Unit'] = ad_unit

    # set 'Ad Dimensions' based dimension in 'Script Tag'
    def assign_ad_dimensions(self):
        if self.sheet_type == 'dcm video tracking pixels':
            return
        else:
            for ad_dimensions in self.ad_dimensions_dict:
                for dimensions in self.ad_dimensions_dict[ad_dimensions]:
                    for row in self.csv_dict:
                        if dimensions in row[self.dict_key]:
                            row['Ad Dimension'] = ad_dimensions

    # input creative names and returns list of creative names
    def input_creative_names(self):
        creative_names = input("Enter names of creatives separated by a comma and a space (e.g. ', '). Names must include ad dimensions!\nEnter creative names here: ")
        creative_names_list = creative_names.split(', ')
        return creative_names_list

    # set 'Creative Name' based on 'Ad Dimensions' for display tags and returns nothing for 1x1 tags
    def assign_creative_name(self):
        for row in self.csv_dict:
            if row['Creative Name'] != '':
                break
        
            else:
                creative_list = []
                creative_list = self.input_creative_names()

                for row in self.csv_dict:
                    
                    if row['Ad Dimension'] == '320x50':
                        for creative in creative_list:
                            if creative.find('320x50') != -1:
                                row['Creative Name'] = creative
                    
                    elif row['Ad Dimension'] == '300x250':
                        for creative in creative_list:
                            if creative.find('300x250') != -1:
                                row['Creative Name'] = creative
                    
                    elif row['Ad Dimension'] == '728x90':
                        for creative in creative_list:
                            if creative.find('728x90') != -1:
                                row['Creative Name'] = creative
                    
                    elif row['Ad Dimension'] == '300x50':
                        for creative in creative_list:
                            if creative.find('300x50') != -1:
                                row['Creative Name'] = creative

                    elif row['Ad Dimension'] == '320x480':
                        for creative in creative_list:
                            if creative.find('320x480') != -1:
                                row['Creative Name'] = creative

                    elif row['Ad Dimension'] == '480x320':
                        for creative in creative_list:
                            if creative.find('480x320') != -1:
                                row['Creative Name'] = creative

    # create new csv that appears in same folder in as tag sheet with naming convention of 
    # tag_sheet_name_Ad_Upload.csv
    def create_new_csv(self):
        directory = self.file_path + '_Ad_Upload.csv'  
        with open(directory, 'w', newline='') as new_csv:  # include newline='' prevents empty rows after each dict is written        

            new_csv_writer = csv.DictWriter(new_csv, fieldnames=self.header_names)
            new_csv_writer.writeheader()
            for row in self.csv_dict:
                new_csv_writer.writerow(row)