# Literature Review

Approaches or solutions that have been tried before on similar projects.

**Summary of Each Work**:

- **Source 1**: Discovery and analysis of topographic features using learning algorithms: A seamount case study (2013)

  - https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/grl.50615

**Objective:**
To develop an automated method using neural networks to detect and catalog seamounts from global bathymetric data, overcoming challenges with traditional manual and model-based approaches.

**Methods:**
The study used autoencoder neural networks to encode and reconstruct bathymetric patches of seafloor data, minimizing reconstruction errors for seamount-like features. A systematic process was developed to train and test models using curated datasets of seamounts, with preprocessing steps including dimensionality reduction and spatial filtering.

**Outcomes:**
The method effectively identified seamounts with a lower false positive rate compared to traditional algorithms, particularly in regions with challenging tectonic fabric. The trained network demonstrated adaptability for different regions, although limitations existed in detecting smaller features due to data resolution constraints.

**Relation to the Project:**
This study provides insights into using learning algorithms for feature recognition in geospatial data. The method of leveraging autoencoders and preprocessing techniques is directly applicable to projects requiring automation of feature extraction, such as identifying terrain anomalies in seabed datasets.

- **Source 2**: New global seamount census from altimetry-derived gravity data (2011)

  - https://academic.oup.com/gji/article/186/2/615/588187?login=false

**Objective**:The Global Seamount Database: http://www.soest.hawaii.edu/PT/SMTS/main.html, To develop a refined global census of seamounts using vertical gravity gradient (VGG) data derived from satellite altimetry, aiming to improve detection accuracy and address previous overestimates.

**Methods:**
A non-linear inversion method was applied to VGG data, modeling potential seamounts as elliptical polynomial functions. Automated and manual inspections of potential seamounts were conducted, supplemented by statistical criteria like the Akaike Information Criterion for validation. Seamount parameters were estimated from bathymetric grids for a comprehensive census.

**Outcomes:**
The study identified 24,643 potential seamounts taller than 100 meters globally, with an estimated total seamount count of 40,000–55,000 when accounting for smaller features and missed detections. This census provides more accurate spatial distributions and size-frequency statistics compared to previous studies.

**Relation to the Project:**
This work demonstrates advanced methods for feature detection in geospatial data, which can be adapted to seabed terrain analysis for identifying significant topographic features. The approach highlights the importance of combining automated and manual methods for precise mapping, relevant to seabed image analysis tasks.

- **Source 3**: Seamount Detection Using SWOT-Derived Vertical Gravity Gradient: Advancements and Challenges (2024)

- https://academic.oup.com/gji/article/186/2/615/588187?login=false

**Objective:**
To explore the efficiency of the Surface Water and Ocean Topography (SWOT) satellite in detecting seamounts using simulated vertical gravity gradient (VGG) data.

**Methods:**
The study used simulated SWOT SSH data to derive VGG fields, employing an automatic algorithm (AIFS) to identify seamount centers and base polygons. Circular and elliptical seamounts were modeled, and VGG accuracy was compared with data from Jason-2 and Cryosat-2 altimeters.

**Outcomes:**
SWOT-derived VGGs demonstrated superior accuracy (RMSD: 1.33 Eötvös) compared to Jason-2 and Cryosat-2 (RMSD: 2.77–2.78 Eötvös). The AIFS algorithm effectively identified seamounts, although challenges remained in detecting elliptical seamounts. Merging SWOT data with high-resolution bathymetric data was suggested to improve results.

**Relation to the Project:**
This study provides insights into leveraging high-resolution satellite data and algorithms for seamount detection, offering methods and benchmarks relevant to projects focused on terrain analysis and feature identification in geospatial datasets.
