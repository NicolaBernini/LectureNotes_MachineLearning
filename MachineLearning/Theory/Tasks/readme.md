
# Overview 

The typical Machine Learning Tasks 

# High Level Tasks 

This kind of tasks can be formalized in a context-agnostic way hence as purely Machine Learning related 

## Generic ML High Level Tasks 

List of Generic High Level Tasks 
- Object Recognition 
- Object Detection 
- Semantic Segmentation 

### Object Recognition 

- Input: Data 
- Output: Single Meaning Label 
- Details 
  - The Meaning Label is associated to the whole Input Data 


### Object Detection 

- Input: Data, set of Meaning Labels 
- Output: Subset of the Input Data associated to the Meaning Label 
- Details 
  - It performs a search inside the Input Data for each of the Meaning Labels 
  - Once one is identified, the subset of data associated with it "isolated" from the rest of the data 
  - Example 
    - In Computer Vision, it is equivalent to the problem of defining a bounding box for a specific element (e.g. car, other vehicles, pedestrian, ...)


### Semantic Segmentation 

- Input: Data, set of Meaning Labels 
- Output: Association between "Atomic Data Unit" and "Meaning Label"
- Details 
  - The "Meaning Label" Set must be suitable for the "Atomic Data Unit" Set
  - Examples 
    - In Computer Vision 
      - Atomic Data Unit = Pixel 
      - Possible Meaning Label Set = Background, Foreground 






