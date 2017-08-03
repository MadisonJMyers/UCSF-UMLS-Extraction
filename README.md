# UCSF-UMLS-Extraction
Extraction of Patient Identification and Unified Medical Language System (UMLS) Information from UCSF Clinical Notes

This script requires the installation of the UMLS Metathesaurus and QuickUMLS.

UMLS Metathesaurus download: https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html
QuickUMLS: https://github.com/Georgetown-IR-Lab/QuickUMLS
  Installation Instructions: https://github.com/Georgetown-IR-Lab/QuickUMLS#installation

Note from UMLS: Each UMLS release includes MetamorphoSys, required to install Knowledge Sources files, and to create, search and browse customized Metathesaurus subsets. MetamorphoSys requires a minimum of 30 GB of free hard disk and takes 2-10 hours to run on a range of platforms tested. The actual time will depend on your configuration, hardware and operating system platforms.

Requirements include:

  1. Python 3.0 or above
  2. UMLS Metathesaurus installed by MetamorphoSys
     https://www.nlm.nih.gov/pubs/factsheets/umlsmetamorph.html
  3. QuickUMLS dependencies: leveldb, numpy, spacy, unidecode
     install with QuickUMLS installation instructions or
     'python -m pip install <requirement>'
  4. QuickUMLS
  5. Text files
  
Please install the UMLS metathesaurus via the MetamorphoSys tool. Then install QuickUMLS, following the instructions closely and using the UMLS metathesaurus installation and destination paths. Then change the script to reflect the destination path. Move all text files into the same QuickUMLS file. After running, the script will output each text file name (in this use case the patient ID), each line that has non-negated UMLS terms and the UMLS information including CUI and description.

Please see the paper for more details. https://github.com/MadisonJMyers/UCSF-UMLS-Extraction/blob/master/ExtractingPatientIdentification.pdf

This script is a part of a short bioinformatics joint project with the Institute for Computational Health Sciences and the Baranzini Lab, UCSF.

For questions please contact madisonjmyers@gmail.com.

