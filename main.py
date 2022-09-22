from AdUpload_class import AdUpload


# /Users/username/directory/folder_tags_are_in/tags_sheet_name.xls
# example: '/Users/ryanprince/Downloads/NEW ASSETS_TruFuel March-November 2022/Tags_TRUFUEL010CP_Cluep_Video_1x1s_092022.xls'
file_path = '/Users/ryanprince/Downloads/NEW ASSETS_IDPH - HHS SPF - Q3 2022/Tags_HHS001CP_HHS_FY23_SPF_Sept_Funds_ZLR_Ignition_-_Iowa_Health___Human_Services copy.xls'

# for US domains: domain_name.com OR domain_name.gov OR domain_name.net... etc.
# for non-US domains: domain_name.ca OR domain_name.fr OR domain_name.uk... etc.
# example: lexus.com
ad_domain = 'yourlifeiowa.org'

# standard DCM display tags should be 'dcm display tags'
# DV wrapped DCM dipslay tags should be 'dcm dv display tags'
# standard Sizmek display tags should be 'sizmek display tags'
# DV wrapped Sizmek dipslay tags should be 'sizmek dv display tags'
# DCM 1x1 tracking pixels for display placements should be 'dcm display tracking pixels'
# DCM 1x1 tracking pixels for video placements should be 'dcm video tracking pixels'
sheet_type = 'dcm video tracking pixels'

#arrays of sheet types for if/ else statement in create_new_ad_upload_csv()
dipslay_tag_sheet_types = ['dcm display tags', 'dcm dv display tags', 'sizmek display tags', 'sizmek dv display tags']
tracker_tag_sheet_types = ['dcm display tracking pixels', 'dcm video tracking pixels']


def new_display_tags_csv(file_path, ad_domain, sheet_type):
    new_ad_upload_csv = AdUpload(file_path=file_path, ad_domain=ad_domain, sheet_type=sheet_type)
    new_ad_upload_csv.remove_gdpr_macro_dcm_js_tag()
    new_ad_upload_csv.assign_ad_type()
    new_ad_upload_csv.assign_ad_unit()
    new_ad_upload_csv.assign_ad_dimensions()
    new_ad_upload_csv.assign_creative_name()
    new_ad_upload_csv.create_new_csv()

def new_tracking_tags_csv(file_path, ad_domain, sheet_type):
    new_ad_upload_csv = AdUpload(file_path=file_path, ad_domain=ad_domain, sheet_type=sheet_type)
    new_ad_upload_csv.move_ias_trackers()
    new_ad_upload_csv.remove_gdpr_macro_dcm_imp_tag()
    new_ad_upload_csv.remove_img_wrapper_dcm_imp_tag()
    new_ad_upload_csv.assign_ad_type()
    new_ad_upload_csv.assign_ad_unit()
    new_ad_upload_csv.assign_ad_dimensions()
    new_ad_upload_csv.assign_creative_name()
    new_ad_upload_csv.create_new_csv()

def create_new_ad_upload_csv(file_path, ad_domain, sheet_type):
    if sheet_type in dipslay_tag_sheet_types:
        new_display_tags_csv(file_path, ad_domain, sheet_type)

    elif sheet_type in tracker_tag_sheet_types:
        new_tracking_tags_csv(file_path, ad_domain, sheet_type)


create_new_ad_upload_csv(file_path, ad_domain, sheet_type)
