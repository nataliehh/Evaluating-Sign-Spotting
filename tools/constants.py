# You can adapt these paths in case you change any names, locations
root = './' # root
cngt_data_root  =           root + 'CNGT_data/' 
only_lmrks_root =           root + 'CNGT_data_only_lmrks/' # contains the landmarks for each CNGT video (not used)
np_lmrks_root   =           root + 'CNGT_np_landmarks/' # only hands, pose landmarks
cngt_vid_root   =           root + 'CNGT_isolated_signers/' # contains both videos and annotations of CNGT

PATHS = {
# Folders
'root': root,
'cngt_data_root':           cngt_data_root,
'cngt_vids_and_eaf':        cngt_vid_root, 
'np_landmarks':             np_lmrks_root, 
'only_lmrks_root':          only_lmrks_root, 
# Pickle files
'anns_with_tiers':          cngt_data_root + 'anns_with_tiers.pkl',
'cngt_anns' :               cngt_data_root + 'CNGT_annotations.pkl', 
'cngt_demographics':        cngt_data_root + 'cngt_demo.pkl', 
'CNGT_split_ids' :          cngt_data_root + 'CNGT_split_ids.pkl', 
'dataset_anns':             cngt_data_root + 'dataset_anns.pkl', 
'label_encoder':            cngt_data_root + 'label_encoder{}.pkl', 
'man_sim_hand_dist':        cngt_data_root + 'man_sim_hand_dist.pkl', 
'missing_frames_signbank':  cngt_data_root + 'missing_frames_signbank.pkl', 
'signbank_cngt_intersect':  cngt_data_root + 'signbank_intersect.pkl', 
# Numpy files
'data_linguistic':          cngt_data_root + 'CNGT_{}_{}{}_{}.npy', 
'data_only_lmrks':          only_lmrks_root+ 'CNGT_{}_{}{}_{}.npy', 
'features_data':            cngt_data_root + 'features_data{}.npy', 
'masked_corrs':             cngt_data_root + 'masked_corrs{}.npy',  
'out_of_range':             cngt_data_root + 'out_of_range.npy', 
'present_ratios':           cngt_data_root + 'present_ratios.npy', 
'test_vid_ids':             cngt_data_root + 'test_vid_ids.npy', 
'top_signs':                cngt_data_root + 'top{}_signs.npy',
# Csv files
'linguistic_distance_df' :  cngt_data_root + 'ling_dist.csv', 
'linguistic_distance_df_v2':cngt_data_root + 'ling_dist_count_unknowns.csv', 
'signbank_dictionary_info': cngt_data_root + 'signbank_dictionary_info.csv', 
'signbank_minimal_pairs':   cngt_data_root + 'dictionary-export-minimalpairs.csv', 
'signbank_with_linguistics':cngt_data_root + 'signbank_with_linguistics.csv', 
}