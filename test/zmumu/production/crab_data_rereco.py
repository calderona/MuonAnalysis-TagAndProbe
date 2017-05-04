
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'TnPTree_80XRereco_Run2016E_GoldenJSON_Run276098to276384'

config.section_('JobType')
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = '../tp_from_aod_Data.py'
#config.JobType.outputFiles = ['TnPTree_80XRereco_Run2016E_GoldenJSON_Run276098to276384.root']
config.JobType.maxJobRuntimeMin = 2750
config.JobType.allowUndistributedCMSSW = True  # To fix cmssw releases

config.section_('Data')
config.Data.inputDataset = '/SingleMuon/Run2016E-23Sep2016-v1/AOD'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'



#config.Data.runRange = '277070'
#config.Data.allowNonValidInputDataset = True

config.Data.splitting    = 'LumiBased'
config.Data.unitsPerJob  = 20  # Since files based, 10 files per job
config.Data.inputDBS     = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
config.Data.outLFNDirBase  = '/store/group/phys_muon/calderon/TnPNTuples/'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
#config.Data.ignoreLocality = True
#config.Site.ignoreGlobalBlacklist = True
#config.Site.whitelist = ['T2_ES_IFCA']
