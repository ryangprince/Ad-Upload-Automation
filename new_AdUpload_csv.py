from AdUpload_class import AdUpload

# /Users/username/directory/folder_tags_are_in/tags_sheet_name.xls
# example: '/Users/ryanprince/Downloads/NEW ASSETS_TruFuel March-November 2022/Tags_TRUFUEL010CP_Cluep_Video_1x1s_092022.xls'
file_path = '/Users/ryanprince/Downloads/Kustomer - Test - Q3Q4 22/Tags_KU_2H2022_MAoM P1 Campaign_Cluep.xls'

# domain_name.com OR domain_name.gov OR domain_name.net... etc.
# example: lexus.com
ad_domain = 'kustomer.com'

# standard DCM display tags should be 'dcm display tags'
# DV wrapped DCM dipslay tags should be 'dcm dv display tags'
# standard Sizmek display tags should be 'sizmek display tags'
# DV wrapped Sizmek dipslay tags should be 'sizmek dv display tags'
# DCM 1x1 tracking pixels for display placements should be 'dcm display tracking pixels'
# DCM 1x1 tracking pixels for video placements should be 'dcm video tracking pixels'
sheet_type = 'dcm display tags'


new_AdUpload_csv = AdUpload(file_path, ad_domain, sheet_type)

if sheet_type == 'dcm display tags' or 'dcm dv display tags' or 'sizmek display tags' or 'sizmek dv display tags': 
    new_AdUpload_csv.remove_gdpr_macro_dcm_js_tag()
    new_AdUpload_csv.assign_ad_type()
    new_AdUpload_csv.assign_ad_unit()
    new_AdUpload_csv.assign_ad_dimensions()
    new_AdUpload_csv.assign_creative_name()
    new_AdUpload_csv.create_new_csv()

else: 
    new_AdUpload_csv.move_ias_trackers()
    new_AdUpload_csv.remove_gdpr_macro_dcm_imp_tag()
    new_AdUpload_csv.remove_img_wrapper_dcm_imp_tag()
    new_AdUpload_csv.assign_ad_type()
    new_AdUpload_csv.assign_ad_unit()
    new_AdUpload_csv.assign_ad_dimensions()
    new_AdUpload_csv.assign_creative_name()
    new_AdUpload_csv.create_new_csv()