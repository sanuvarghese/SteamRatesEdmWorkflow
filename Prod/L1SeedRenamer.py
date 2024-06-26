import fileinput
import os
text = "hlt.py"
match = {
'L1_DoubleMu0er1p4_OQ_OS_dEta_Max1p6':'L1_SingleMuCosmics',
'L1_DoubleMu4p5er2p0_SQ_OS_Mass_7to18':'L1_DoubleMu4p5er2p0_SQ_OS_Mass7to18',
'L1_TripleMu_2_1p5_0OQ_Mass_Max15':'L1_TripleMu_2_1p5_0OQ_Mass_Max_15',
'L1_TripleMu_2SQ_1p5SQ_0OQ_Mass_Max15':'L1_TripleMu_2SQ_1p5SQ_0OQ_Mass_Max_15',
'L1_SingleMuShower_Nominal':'L1_ETMHF100 OR L1_ETMHF110 OR L1_ETM150 OR L1_ETMHF120 OR L1_ETMHF150',
'L1_SingleMuShower_Tight':'L1_ETMHF100 OR L1_ETMHF110 OR L1_ETM150 OR L1_ETMHF120 OR L1_ETMHF150',
'L1_DoubleMu3_OS_er2p3_Mass_Max14_DoubleEG7p5_er2p1_Mass_Max20':'L1_DoubleMu3_OS_DoubleEG7p5Upsilon',
'L1_DoubleMu5_OS_er2p3_Mass_8to14_DoubleEG3er2p1_Mass_Max20':'L1_DoubleMu5Upsilon_OS_DoubleEG3',
'L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5':'L1_DoubleIsoTau32er2p1',
'L1_IsoTau52er2p1_QuadJet36er2p5':'L1_QuadJet36er2p5_IsoTau52er2p1',
'L1_HTT280er_QuadJet_70_55_40_35_er2p5':'L1_HTT280er_QuadJet_70_55_40_35_er2p4',
'L1_HTT320er_QuadJet_70_55_40_40_er2p5':'L1_HTT320er_QuadJet_70_55_40_40_er2p4',
'L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p1':'L1_ETMHF90_SingleJet60er2p5_ETMHF90_DPHI_MIN2p094',
'L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p6':'L1_ETMHF90_SingleJet60er2p5_ETMHF90_DPHI_MIN2p618',
'L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p1':'L1_ETMHF90_SingleJet80er2p5_ETMHF90_DPHI_MIN2p094',
'L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p6':'L1_ETMHF90_SingleJet80er2p5_ETMHF90_DPHI_MIN2p618',
'L1_DoubleEG5_er1p2_dR_Max0p9':'L1_SingleMuCosmics',
'L1_DoubleEG5p5_er1p2_dR_Max0p8':'L1_SingleMuCosmics',
'L1_DoubleEG6_er1p2_dR_Max0p8':'L1_SingleMuCosmics',
'L1_DoubleEG6p5_er1p2_dR_Max0p8':'L1_SingleMuCosmics',
'L1_DoubleEG7_er1p2_dR_Max0p8':'L1_SingleMuCosmics',
'L1_DoubleEG7p5_er1p2_dR_Max0p7':'L1_SingleMuCosmics',
'L1_DoubleEG8_er1p2_dR_Max0p7':'L1_SingleMuCosmics',
'L1_DoubleEG8p5_er1p2_dR_Max0p7':'L1_SingleMuCosmics',
'L1_DoubleEG9_er1p2_dR_Max0p7':'L1_SingleMuCosmics',
'L1_DoubleEG9p5_er1p2_dR_Max0p6':'L1_SingleMuCosmics',
'L1_DoubleEG10_er1p2_dR_Max0p6':'L1_SingleMuCosmics',
'L1_DoubleEG10p5_er1p2_dR_Max0p6':'L1_SingleMuCosmics',
'L1_DoubleMu0_Upt6_IP_Min1_Upt4':'L1_SingleMuCosmics',
#'L1_DoubleMu0_upt6_IP_Min1_upt4"':'L1_DoubleMu0_upt6ip123_upt4',
'L1_DoubleMu18er2p1_SQ':'L1_DoubleMu18er2p1',
'L1_DoubleMu0_Upt15_Upt7': 'L1_SingleMuCosmics',
'L1_DoubleMu3er2p0_SQ_OS_dR_Max1p4': 'L1_SingleMuCosmics',
'L1_ETMHF90_SingleJet60er2p5_ETMHF90_DPHI_MIN2p094': 'L1_SingleMuCosmics',
#'L1_MuShower_OneNominal': 'L1_ETMHF100 OR L1_ETMHF110 OR L1_ETM150 OR L1_ETMHF120 OR L1_ETMHF150',
'L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p6':'L1_SingleMuCosmics',
'L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p5':'L1_SingleMuCosmics',
'L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5':'L1_SingleMuCosmics',
'L1_Mu18er2p1_Tau26er2p1_Jet70':'L1_SingleMuCosmics',
'L1_Mu18er2p1_Tau26er2p1_Jet55':'L1_SingleMuCosmics',
'L1_DoubleEG_LooseIso16_LooseIso12_er1p5':'L1_SingleMuCosmics',
'L1_DoubleEG4_er1p2_dR_Max0p9':'L1_SingleMuCosmics',
'L1_HTT120_SingleLLPJet40':'L1_SingleMuCosmics',
'L1_DoubleEG_LooseIso18_LooseIso12_er1p5':'L1_SingleMuCosmics',
'L1_HTT160_SingleLLPJet50':'L1_SingleMuCosmics',
'L1_HTT160_SingleLLPJet50':'L1_SingleMuCosmics',
'L1_TripleMu_2SQ_1p5SQ_0OQ_Mass_Max12':'L1_SingleMuCosmics',
'L1_DoubleEG4p5_er1p2_dR_Max0p9':'L1_SingleMuCosmics',
'L1_HTT200_SingleLLPJet60':'L1_SingleMuCosmics',
'L1_DoubleEG_LooseIso20_LooseIso12_er1p5':'L1_SingleMuCosmics',
'L1_HTT200_SingleLLPJet60':'L1_SingleMuCosmics',
'L1_DoubleJet35_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5':'L1_SingleMuCosmics',
'L1_DoubleEG_LooseIso22_LooseIso12_er1p5':'L1_SingleMuCosmics',
'L1_DoubleEG11_er1p2_dR_Max0p6':'L1_SingleMuCosmics',
'L1_DoubleEG_LooseIso25_LooseIso12_er1p5':'L1_SingleMuCosmics',
'L1_ETMHF70_HTT60er OR L1_ETMHF80_HTT60er OR L1_ETMHF90_HTT60er':'L1_ETMHF90_HTT60er',
'L1_ETMHF70 OR L1_ETMHF80 OR L1_ETMHF90 OR L1_ETMHF100':'L1_ETMHF100',
}

for line in fileinput.input(text, inplace=True):
    line = line.rstrip()
    if not line:
        continue
    for f_key, f_value in match.items():
        if f_key in line:
            line = line.replace(f_key, f_value)
    print(line)
    
import re


f = open("hlt.py","r")
data = f.read() # string of all file content

def replace_all(text, dic):
    for i, j in dic.items():
        text = re.sub(r"\b%s\b"%i, j, text) 
        # r"\b%s\b"% enables replacing by whole word matches only
    return text

data = replace_all(data,match)
print("Renaming Changes Undone") 
