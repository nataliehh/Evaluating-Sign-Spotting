# You can adapt these paths in case you change any names, locations
root = '.'
cngt_data_root  =           root + '/CNGT_data/'
only_lmrks_root =           root + '/CNGT_data_only_lmrks/'
datasets_root   =           'D:/Thesis/datasets/'

PATHS = {
# Folders
'root': root,
'cngt_data_root':           cngt_data_root,
'only_lmrks_root':          only_lmrks_root, 
'datasets_root':            datasets_root, 
'cngt_eaf':                 "./CNGT_isolated_signers_eafs_only/",
'np_landmarks':             './CNGT_np_landmarks/', # only hands, pose landmarks
'np_landmarks_all':         datasets_root + 'CNGT_np_landmarks', # Includes face and video_dim numpy files
'signbank_vids':            datasets_root + 'Signbank-NGT-videos/',
'cngt_vids':                datasets_root + 'CNGT_isolated_signers/', # Confusingly, this contains both videos and the annotations
# Pickle files
'cngt_anns' :               cngt_data_root + 'CNGT_annotations.pkl',
'man_sim_hand_dist':        cngt_data_root + 'man_sim_hand_dist.pkl',
'signbank_cngt_intersect':  cngt_data_root + 'signbank_intersect.pkl',
'anns_with_tiers':          cngt_data_root + 'anns_with_tiers.pkl',
'dataset_anns':             cngt_data_root + 'dataset_anns.pkl',
'CNGT_split_ids' :          cngt_data_root + 'CNGT_split_ids.pkl',
'label_encoder':            cngt_data_root + 'label_encoder{}.pkl',
'missing_frames_signbank':  cngt_data_root + 'missing_frames_signbank.pkl',
'cngt_demographics':        cngt_data_root + 'cngt_demo.pkl',
# Numpy files
'top_signs':                cngt_data_root + 'top{}_signs.npy',
'present_ratios':           cngt_data_root + 'present_ratios.npy',
'out_of_range':             cngt_data_root + 'out_of_range.npy',
'data_linguistic':          cngt_data_root + 'CNGT_{}_{}{}_{}.npy',
'data_only_lmrks':          only_lmrks_root+ 'CNGT_{}_{}{}_{}.npy',
'masked_corrs':             cngt_data_root + 'masked_corrs{}.npy',
'test_vid_ids':             cngt_data_root + 'test_vid_ids.npy',
'features_data':            cngt_data_root + 'features_data{}.npy',
# Csv files
'signbank_dictionary_info': cngt_data_root + 'signbank_dictionary_info.csv',
'linguistic_distance_df' :  cngt_data_root + 'ling_dist.csv',
'linguistic_distance_df_v2':cngt_data_root + 'ling_dist_count_unknowns.csv',
'signbank_with_linguistics':cngt_data_root + 'signbank_with_linguistics.csv',
'signbank_minimal_pairs':   cngt_data_root + 'dictionary-export-minimalpairs.csv',
}
