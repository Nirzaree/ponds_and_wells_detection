This repo contains exploration of logic for merging 2 different waterbodies layers: 1. larger surface waterbodies detected by Sentinel data, and 2. Small waterbodies (ponds) detected through high resolution images. 

Merging Logic: 
1. Load surface waterbodies layer
2. Load ponds layer 
3. Create merged geodataframe  
    a. Add standalone surface waterbodies (those that dont intersect with any ponds)  
    b. Add standalone ponds (those that dont intersect with any surface waterbodies)  
    c. Intersection cases:  

      ![alt text](<files/Screenshot from 2025-05-09 13-16-39.png>)  
        1. One swb intersects with one pond : final geometry = union of pond and swb geometries  
        2. One pond intersects with multiple SWBs : final geometry = swb geometry (because on visual inspection of these cases, they were mostly arising due to buffer operation being applied on ponds detection pipeline, resulting in geometries which are sometimes representing multiple ponds in a single boundary)  
        3. One swb intersects with multiple ponds (and corresponding pond intersects with only single swb) : final geometry =  union of pond and swb geometries  
        4. One swb intersects with multiple ponds (and corresponding pond intersects with more than one swb) :  union of pond and swb geometries  
    
How to run the code: 

### 1. Create a virtual environment  
```conda create --name .venv python=3.12.3```
### 2. Install requirements.txt
```
conda install pip 
pip install -r requirements.txt

```
### 3. Run any notebook
- final_merging_logic.ipynb runs with example data files in the files folder, and has the final merging logic
