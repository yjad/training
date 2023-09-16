import streamlit as st



# ld_options={'<Select ...>':None, 
#          '1- Resize Image':load_full_scan,
#          '2- Load IP scan files':load_IP_scan,
#          '3- Load VMWare data':load_VMs_data,
#          '4- Load VM Replciation Data':load_VMWare_replication_sheets,
#          '5- Load Power HMC sheets (DTS & HDB)':load_Power_sheets,
#          '6- Summerize IP scan files':summerize_IP_scan,
#          '7- Load CBE Security Alert':cbe.add_cbe_alert
#         #  '7- Load CBE Report':load_CBE_rep
# }

# rep_opt = st.sidebar.selectbox("Load Data Options:",ld_options.keys())
# if ld_options[rep_opt]:
#     ld_options[rep_opt]()