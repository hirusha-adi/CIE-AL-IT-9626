---
title: 9. Graphics
---

All Past Paper Questions: https://docs.google.com/document/d/1Wx551YT0F35Ca0DI4uQ0bNIO0xf0-jFKEjCNY9tOkkE/edit?usp=sharing

## Bitmap Images

- compression
    - lossy
        - Images are reduced in quality
        - Information is lost forever
            - cannot be restored
        - algorithm removes areas with low detail more than areas of high detail
        - so image is changed from original
        - compression artefacts may appear
        - Image quality reduced with repeated compression
        - because at each compression, more image information is lost
    - lossless
        - no information is lost
        - Image is recreated with no difference from the original
        - Works well with images with blocks of similar pixels
        - because only need to store data for one pixel and number of pixels
        - No loss of quality
        - algorithms can reconstuct original pixels lost by compression


## Vector Images

- advantages
    - easier to edit
    - Editing does not affect the quality
        - does not pixelate on enlarging
    - have smaller file size
        - saves storage
    - download faster than bitmap image
    - so can be displayed on low-power devices
    - Edges are smooth(er)
    - producing a higher quality image
- disadvantages
    - Photographs are not realistic
    - surfaces are unrealistic
    - Small editing errors are more visible
    - reduces the image quality
    - hard to add special effects is more difficult
    - need powerful devices
        - to carry out calculations
        - when editing

- tools (/ techniques)
    - to change appearance of objects
        - Use of Bezier handles to change angle of line / control-point
        - Moving node to change the start/end points of
            - Bezier curves (that make up rounded shape)
        - Moving node from one position to another
        - Adding node to line to divide line into two and moving new node
        - Deleting nodes to join lines and remove curves
        - Group shapes to allow for movement of parts of images
        - Changing the colour/transparency/size/rotation of shape
        - Manually editing the code in the SVG XML file.

- files
    - svg (scalable vector graphics)
        - why
            - open-source
            - a W3C standard (World Wide Web Consortium)
            - based on XML which is standardized
            - can be imported into many graphics software
            - Format is scripting, so can be used with CCS
            - supported by web & print systems
            - No compression applied
            - Use of XML + mathematical calculations 
                - image can be scaled without quality loss
        - information stored
            - The font to be used.
            - shapes
                - dimensions
                - position on screen
                - style
                - colors to fill shape
            - lines
                - dimensions
                - position on screen
                - colors to draw line
    


## Common

### Editing

- tools
    - layer tool
        - To separate elements of image
            - to worked on independently
        - To overlay elements onto others 
            - each element can be moved independently of the others
        - allows editing of elements while leaving other elements untouched
        - do stuff to one element/layer (without affecting others)
        - allows transparency effects (of objects)
        - To insert text 
            - writing can be placed anywhere on the image
    - flatten tool
        - To merge all layers into one layer
        - To discard hidden layers 
            - make all layers are visible
        - To fill any transparent areas with white 'background colour'
        - to create pdf to print easily
        - To reduce the file size

### Conversions

- bitmap to vector
    - how
        - (Clearly defined) areas in the bitmap are automatically traced to create objects in the vector image
        - Nodes are added to the objects
        - Object manually corrected by user to merge shapes
        - Colour resolution (number of bits) reduced by user

### Comparisons

- bitmap vs vector

