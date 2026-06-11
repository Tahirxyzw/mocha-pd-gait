---
license: cc-by-nc-nd-4.0
---
<!DOCTYPE html>
<html lang="en">
<body>

<h1>Overview</h1>
<h3> Please read carefully the terms and conditions and any accompanying documentation at <a href="https://neurips2025.care-pd.ca/terms-of-use.html" 
     target="_blank" 
     style="color:#0066cc; text-decoration:underline;">
     neurips2025.care-pd.ca/terms-of-use
  </a> before you download and/or use the CARE-PD dataset.
</h3>
<p>
Project page: <a href="https://neurips2025.care-pd.ca/" 
     target="_blank" 
     style="color:#0066cc; text-decoration:underline;">
     https://neurips2025.care-pd.ca/
  </a>
</p>
<p>
CARE-PD is the largest publicly available archive of 3D mesh gait data for Parkinson's Disease (PD) and the first to include data collected across multiple sites.  
The dataset aggregates 9 cohorts from 8 clinical sites, including 362 participants spanning a range of disease severity.  
All recordings—whether from RGB video or motion capture—are unified into anonymized SMPL body gait meshes through a curated harmonization pipeline.
</p>

<h3>This dataset enables two main benchmarks:</h3>
<ol>
    <li>Supervised clinical score prediction: Estimating UPDRS gait scores from 3D meshes</li>
    <li>Unsupervised motion pretext tasks for Parkinsonian gait representation learning</li>
</ol>

<h2>Dataset Contents</h2>
<p>CARE-PD consists of 9 harmonized datasets:</p>
<ol>
    <li>3DGait&nbsp;– Clinical gait recordings with UPDRS scores</li>
    <li>BMCLab&nbsp;– Gait recordings with medication status and UPDRS scores (original license: CC BY 4.0)</li>
    <li>DNE&nbsp;– Contains healthy, Parkinson's, and other neurological conditions (original license: CC BY 4.0)</li>
    <li>E-LC&nbsp;– Medication status (on/off) and PD subtypes</li>
    <li>KUL-DT-T&nbsp;– Freezer/non-freezer subtypes</li>
    <li>PD-GaM&nbsp;– Clinical gait recordings with UPDRS scores</li>
    <li>T-SDU&nbsp;– Ambient walking recordings</li>
    <li>T-SDU-PD&nbsp;– PD patient walking with UPDRS scores</li>
    <li>T-LTC&nbsp;– Ambient walking recordings</li>
</ol>

<h3>Canonicalized SMPL files</h3>
<p>
  <code>*_canonical.pkl</code> files in the
  <code>Canonicalized_SMPL_pickles</code> folder keep the same nested dataset
  format as the original pickles. The canonical versions change only the motion coordinates:
</p>
<p>
  <code>pose/trans</code> are rotated so the motion uses a shared coordinate system.
</p>
<pre><code>x = lateral
y = up
z = forward</code></pre>
<p>They also preprocess translation so:</p>
<ul>
  <li>The first frame starts at <code>x=0, z=0</code></li>
  <li>The body stands/walks on <code>y=0</code></li>
</ul>
<p>
  <b>Note:</b> <code>KUL-DT-T</code> and <code>E-LC</code> are the only datasets that are not purely straight walking sequences, so for these two datasets the subject is canonicalized to start facing <code>z+</code> in the first frame.
</p>

<h2>Data Structure</h2>
<p>The main SMPL datasets are provided in a standardized format:</p>
<pre><code>{
    "anonymized_subject_id": {
        "anonymized_walk_id": {
            "pose": array,      # SMPL pose parameters (shape varies by dataset)
            "trans": array,     # Translation data
            "beta": array,      # Body shape parameters (zeros for privacy)
            "fps": int,         # Frames per second (standardized)
            "UPDRS_GAIT": int,  # Clinical score (0-3) or None if unavailable
            "medication": str,  # Medication status or None if unavailable
            "other": str        # Additional labels or None if unavailable
        }
    }
}</code></pre>

<p>Additionally, we provide h36m, HumanML3D, and SMPL_6D formats.</p>

<h2>Getting Started</h2>
<p>Please refer to <a href="https://github.com/TaatiTeam/CARE-PD">https://github.com/TaatiTeam/CARE-PD</a> for getting started with the dataset.</p>

<h2>Benchmarks</h2>
<p>CARE-PD includes data splits to test generalization:</p>
<ol>
    <li>6-Fold (split per subject)</li>
    <li>Leave-one-subject-out</li>
    <li>Fixed train-test splits (split per subject)</li>
</ol>
<p>The former two are only provided for the supervised clinical score prediction task.</p>

<h2>Terms of Use</h2>
<p>
By accessing and using this database (the "Database"), users ("Users") acknowledge and agree to comply with the following conditions:
</p>

<ol>
    <li><strong>License and Attribution</strong>
        <ul>
            <li>The Database is publicly released under a Creative Commons Attribution-NonCommercial (CC&nbsp;BY-NC&nbsp;4.0) license.</li>
            <li>Users must provide appropriate attribution by citing the Database and the original publications associated with each dataset accessed from the Database.</li>
        </ul>
    </li>
    <li><strong>Data Privacy and Ethics</strong>
        <ul>
            <li>Users must not attempt to identify, contact, or otherwise compromise the anonymity of any individuals whose data is included in the Database.</li>
            <li>All use of the data must comply with applicable ethical guidelines and legal regulations, including privacy laws (e.g., GDPR, HIPAA, PIPEDA).</li>
        </ul>
    </li>
    <li><strong>Data Handling and Security</strong>
        <ul>
            <li>Users must maintain appropriate data security measures to prevent unauthorized access, sharing, or use of the data.</li>
            <li>Users are encouraged, but not required, to direct third parties to the original Database URL rather than re-hosting the data.</li>
        </ul>
    </li>
    <li><strong>Intellectual Property Notice</strong>
        <ul>
            <li>Copyright and other rights remain with the original data providers.</li>
        </ul>
    </li>
    <li><strong>Disclaimer of Warranty</strong>
        <ul>
            <li>Use of the Database is subject to Section&nbsp;5 (Disclaimer of Warranties and Limitation of Liability) of the CC&nbsp;BY-NC&nbsp;4.0 licence.</li>
        </ul>
    </li>
</ol>

<p>By using the Database, Users expressly acknowledge and agree to abide by these Terms of Use.</p>

<h2>Citation</h2>
<p>If you use CARE-PD in your research, please cite:</p>
<p>Adeli V, Klabučar I, Rajabi J, Filtjens B, Mehraban S, Wang D, Seo H, Hoang T-H, Do MN, Muller C, Neves de Oliveira C, Boari Coelho D, Ginis P, Gilat M, Nieuwboer A, Spildooren J, McKay JL, Kwon H, Clifford G, Esper CD, Factor SA, Genias I, Dadashzadeh A, Shum L, Whone A, Mirmehdi M, Iaboni A, Taati B.
CARE-PD: A Multi-Site Anonymized Clinical Dataset for Parkinson’s Disease Gait Assessment.
In: Advances in Neural Information Processing Systems (NeurIPS); 2025.</p>

<p>Additionally, please cite the relevant datasets:</p>
<ol>
    <li>3DGait
        <ul>
            <li>Diwei Wang, Chaima Zouaoui, Jinhyeok Jang, Hassen Drira, and Hyewon Seo. 2023. Video-Based Gait Analysis for Assessing Alzheimer’s Disease and Dementia with Lewy Bodies. In <em>Applications of Medical Artificial Intelligence: Second International Workshop, AMAI&nbsp;2023, Held in Conjunction with MICCAI&nbsp;2023</em>, Vancouver, BC, Canada, October&nbsp;8, 2023, Proceedings. Springer-Verlag, Berlin, Heidelberg, 72–82. https://doi.org/10.1007/978-3-031-47076-9_8</li>
        </ul>
    </li>
    <li>BMCLab
        <ul>
            <li>Shida TKF, Costa TM, de Oliveira CEN, de Castro Treza R, Hondo SM, Los Angeles E, Bernardo C, Dos Santos de Oliveira L, de Jesus Carvalho M, Coelho DB. A public data set of walking full-body kinematics and kinetics in individuals with Parkinson's disease. <em>Front Neurosci.</em> 2023 Feb&nbsp;16;17:992585. doi: 10.3389/fnins.2023.992585. PMID: 36875659; PMCID: PMC9978741.</li>
        </ul>
    </li>
    <li>DNE
        <ul>
            <li>Hoang TH, Zallek C, Do MN. Smartphone-Based Digitized Neurological Examination Toolbox for Multi-test Neurological Abnormality Detection and Documentation. <em>IEEE J Biomed Health Inform.</em> 2024 Aug&nbsp;26;PP. doi: 10.1109/JBHI.2024.3439492. Epub ahead of print. PMID: 39186431.</li>
<li>Hoang TH, Zehni M, Xu H, Heintz G, Zallek C, Do MN. Towards a Comprehensive Solution for a Vision-Based Digitized Neurological Examination. <em>IEEE J Biomed Health Inform.</em> 2022 Aug&nbsp;26(8):4020-4031. doi: 10.1109/JBHI.2022.3167927. Epub 2022 Aug 11. PMID: 35439148; PMCID: PMC9707344.</li>
        </ul>
    </li>
    <li>E-LC
        <ul>
            <li>Lucas McKay J, Goldstein FC, Sommerfeld B, Bernhard D, Perez Parra S, Factor SA. Freezing of Gait can persist after an acute levodopa challenge in Parkinson's disease. <em>NPJ Parkinsons Dis.</em> 2019 Nov&nbsp;22;5:25. doi: 10.1038/s41531-019-0099-z. PMID: 31799377; PMCID: PMC6874572.</li>
            <li>Kwon H, Clifford GD, Genias I, Bernhard D, Esper CD, Factor SA, McKay JL. An Explainable Spatial-Temporal Graphical Convolutional Network to Score Freezing of Gait in Parkinsonian Patients. <em>Sensors (Basel).</em> 2023 Feb&nbsp;4;23(4):1766. doi: 10.3390/s23041766. PMID: 36850363; PMCID: PMC9968199.</li>
        </ul>
    </li>
    <li>KUL-DT-T
        <ul>
            <li>Spildooren J, Vercruysse S, Desloovere K, Vandenberghe W, Kerckhofs E, Nieuwboer A. Freezing of gait in Parkinson's disease: the impact of dual-tasking and turning. <em>Mov Disord.</em> 2010 Nov&nbsp;15;25(15):2563–70. doi: 10.1002/mds.23327. PMID: 20632376.</li>
            <li>Filtjens B, Ginis P, Nieuwboer A, Slaets P, Vanrumste B. Automated freezing of gait assessment with marker-based motion capture and multi-stage spatial-temporal graph convolutional neural networks. <em>J Neuroeng Rehabil.</em> 2022 May&nbsp;21;19(1):48. doi: 10.1186/s12984-022-01025-3. PMID: 35597950; PMCID: PMC9124420.</li>
        </ul>
    </li>
    <li>PD-GaM
        <ul>
<li>Vida Adeli, Soroush Mehraban, Majid Mirmehdi, Alan Whone, Benjamin Filtjens, Amirhossein Dadashzadeh, Alfonso Fasano, and Andrea Iaboni, Babak Taati. GAITGen: Disentangled motion-pathology impaired gait generative model—bringing motion generation to the clinical domain. <em>arXiv</em> preprint arXiv:2503.22397, 2025.</li>
            <li>Amirhossein Dadashzadeh, Shuchao Duan, Alan Whone, and Majid Mirmehdi. PeCop: Parameter efficient continual pretraining for action quality assessment. In <em>Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision</em>, 42–52, 2024.</li>
        </ul>
    </li>
    <li>T-SDU
        <ul>
            <li>Adeli V, Klabučar I, Rajabi J, Filtjens B, Mehraban S, Wang D, Seo H, Hoang T-H, Do MN, Muller C, Neves de Oliveira C, Boari Coelho D, Ginis P, Gilat M, Nieuwboer A, Spildooren J, McKay JL, Kwon H, Clifford G, Esper CD, Factor SA, Genias I, Dadashzadeh A, Shum L, Whone A, Mirmehdi M, Iaboni A, Taati B.
CARE-PD: A Multi-Site Anonymized Clinical Dataset for Parkinson’s Disease Gait Assessment.
In: Advances in Neural Information Processing Systems (NeurIPS); 2025.</li>
        </ul>
    </li>
    <li>T-SDU-PD
        <ul>
            <li>Adeli V, Klabučar I, Rajabi J, Filtjens B, Mehraban S, Wang D, Seo H, Hoang T-H, Do MN, Muller C, Neves de Oliveira C, Boari Coelho D, Ginis P, Gilat M, Nieuwboer A, Spildooren J, McKay JL, Kwon H, Clifford G, Esper CD, Factor SA, Genias I, Dadashzadeh A, Shum L, Whone A, Mirmehdi M, Iaboni A, Taati B.
CARE-PD: A Multi-Site Anonymized Clinical Dataset for Parkinson’s Disease Gait Assessment.
In: Advances in Neural Information Processing Systems (NeurIPS); 2025.</li>
        </ul>
    </li>
    <li>T-LTC
        <ul>
            <li>Adeli V, Klabučar I, Rajabi J, Filtjens B, Mehraban S, Wang D, Seo H, Hoang T-H, Do MN, Muller C, Neves de Oliveira C, Boari Coelho D, Ginis P, Gilat M, Nieuwboer A, Spildooren J, McKay JL, Kwon H, Clifford G, Esper CD, Factor SA, Genias I, Dadashzadeh A, Shum L, Whone A, Mirmehdi M, Iaboni A, Taati B.
CARE-PD: A Multi-Site Anonymized Clinical Dataset for Parkinson’s Disease Gait Assessment.
In: Advances in Neural Information Processing Systems (NeurIPS); 2025.</li>
        </ul>
    </li>
</ol>

<h2>Acknowledgments</h2>
<p>We thank all participating research institutions and subjects who made this dataset possible.</p>

</body>
</html>