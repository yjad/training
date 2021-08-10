rec = {'PmtId': {'InstrId': 'FT21220WVT2C', 'EndToEndId': 'FT21220WVT2C', 'TxId': 'FT21220WVT2C'}, 
    'IntrBkSttlmAmt': '75000.00', 'ChrgBr': 'SLEV', 
    'Dbtr': {'Nm': 'Ahmed AAAAlsayed Mohammed'}, 
    'DbtrAcct': {'Id': {'PrtryAcct': {'Id': 'EG130038008800000880000003160'}}}, 
    'DbtrAgt': {'FinInstnId': {'BIC': 'HDBKEGCAXXX'}, 'BrnchId': {'Id': '0088'}},
    'CdtrAgt': {'FinInstnId': {'BIC': 'CIBEEGCX'}, 'BrnchId': {'Id': '0039'}}, 
    'Cdtr': {'Nm': 'حامد مصطفي البسيونى'}, 
    'CdtrAcct': {'Id': {'PrtryAcct': {'Id': '100036556352'}}, 
    'Tp': {'Cd': 'CACC'}}, 
    'Purp': {'Cd': 'CASH'}, 
    'RmtInf': {'Ustrd': 'شحصى شراء موبيليات'}
    }

def dict_to_1L_dict(rec, parent):

   
    dic = {}
    if not parent: parent = list(rec)[0]
    for L0 in rec.items():
        
        # print (L0, L0[0], type (L0))
        
        if type(L0[1]) == str:
            L0_dict = {parent + '.'+ L0[0] :L0[1]}
            print (L0_dict)
            dic.update(L0_dict)
        else:
           
            dic_sub = dict_to_1L_dict(L0[1], parent)      # recursive
            parent = parent + '.' + list(L0)[0] + '.' 
            print ("-----------", dic_sub)
            dic.update(dic_sub)
           
    return dic


print (50*"-", dict_to_1L_dict(rec, ""))