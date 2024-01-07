import wood_design_package as wdp

beam_shear_list_2 = wdp.Analysis_Data_Load.column_shear_force_2(self=None,file_name="analysis_test_data.json")
beam_shear_list_3 = wdp.Analysis_Data_Load.column_shear_force_2(self=None,file_name="analysis_test_data.json")
beam_moment_list_2 = wdp.Analysis_Data_Load.column_moment_2(self=None,file_name="analysis_test_data.json")
beam_moment_list_3 = wdp.Analysis_Data_Load.column_moment_3(self=None,file_name="analysis_test_data.json")
proposed_sections_1=[]
proposed_sections_2=[]
print('\n*******************ANALYSIS VALUES*******************\n')
print("V2 values",wdp.Analysis_Data_Load.column_shear_force_2(self=None,file_name='analysis_test_data.json'),"\n")
print("V3 values",wdp.Analysis_Data_Load.column_shear_force_3(self=None,file_name='analysis_test_data.json'),"\n")
print("M2 values",wdp.Analysis_Data_Load.column_moment_2(self=None,file_name='analysis_test_data.json'),"\n")
print("M3 values",wdp.Analysis_Data_Load.column_moment_3(self=None,file_name='analysis_test_data.json'),"\n")
print("\n Around Axis 2 \n")
print('*********************************')
for i in range(len(beam_moment_list_2)):
    proposed_sections_1.append(wdp.Sawn_Lumber.section_proposal(self=None,M_r=beam_moment_list_2[i],V_r=beam_shear_list_2[i],Es_I=0, load_factor=1.4))
for i in range(len(beam_moment_list_2)):
    print('******************************\n Run No. {number}'.format(number=i+1))
    print('\nMr Values for Beam No. {number}:'.format(number=i+1),
          wdp.Sawn_Lumber.sorted_by_M_r(self=None,section_array=proposed_sections_1[i]))
    print('\nVr Values for Beam No. {number}:'.format(number=i + 1),
          wdp.Sawn_Lumber.sorted_by_V_r(self=None, section_array=proposed_sections_1[i]))
print("\n Around Axis 3 \n")
print('*********************************')
for i in range(len(beam_moment_list_2)):
    proposed_sections_2.append(wdp.Sawn_Lumber.section_proposal(self=None,M_r=beam_moment_list_3[i],V_r=beam_shear_list_3[i],Es_I=0, load_factor=1.4))
for i in range(len(beam_moment_list_2)):
    print('******************************\n Run No. {number}'.format(number=i + 1))
    print('\nMr Values for Beam No. {number}:'.format(number=i+1),
          wdp.Sawn_Lumber.sorted_by_M_r(self=None,section_array=proposed_sections_2[i]))
    print('\nVr Values for Beam No. {number}:'.format(number=i + 1),
          wdp.Sawn_Lumber.sorted_by_V_r(self=None, section_array=proposed_sections_2[i]))
